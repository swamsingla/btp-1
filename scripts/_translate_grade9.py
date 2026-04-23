"""
Translation pipeline for Grade 9 Mathematics (Chapters 1-3).

Pipeline:
  Phase 1 — Term extraction: Upload .md files to cluster, run Qwen3-8B to
             extract technical terms, download results as JSON.
  Phase 2 — Glossary build: Translate each unique term once via Sarvam API
             for all 3 target languages.
  Phase 3 — Content translation: Translate each .md file via Sarvam API with
             glossary-placeholder replacement for consistency.
  Phase 4 — MongoDB upload: Convert translated markdown to HTML and update
             topic.translations in MongoDB.

Usage:
  python scripts/_translate_grade9.py
  python scripts/_translate_grade9.py --skip-extraction   # if terms already downloaded
  python scripts/_translate_grade9.py --skip-glossary     # if glossary already built
"""
import json
import os
import re
import sys
import time
from pathlib import Path

import paramiko

# ── Cluster config (same as batch_orchestrate.py) ───────────────────────────
ADA_HOST = "ada.iiit.ac.in"
ADA_USER = "shubhamcvit"
ADA_PASS = "0410@Shubham"
GPU_NODE = "gnode047"
SCRATCH = "/ssd_scratch/shubhamcvit/btp"
VENV_PYTHON = "/ssd_scratch/shubhamcvit/venv/bin/python3"
ADA_HOME = f"/home2/{ADA_USER}"

# ── Translation config ───────────────────────────────────────────────────────
SARVAM_API_KEY = "sk_hl4v83rj_S08tXKfP5VeVO0o1M5Gwm2Pq"
TARGET_LANGS = ["hi", "te", "od"]
LANG_CODES = {"hi": "hi-IN", "te": "te-IN", "od": "od-IN"}
LANG_NAMES = {"hi": "Hindi", "te": "Telugu", "od": "Odia"}

GRADE = 9
CHAPTERS = [1, 2, 3]
SUBJECT = "maths"

# ── Local paths ──────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
MD_ROOT = ROOT / "data" / "output" / f"grade{GRADE}" / SUBJECT
INTERMEDIATE = ROOT / "data" / "intermediate"
INTERMEDIATE.mkdir(parents=True, exist_ok=True)

TERMS_JSON = INTERMEDIATE / "grade9_terms.json"
GLOSSARY_JSON = INTERMEDIATE / "grade9_glossary.json"
TRANSLATIONS_JSON = INTERMEDIATE / "grade9_translations.json"   # Phase 3 cache

# ── Skip flags ────────────────────────────────────────────────────────────────
SKIP_EXTRACTION = "--skip-extraction" in sys.argv
SKIP_GLOSSARY = "--skip-glossary" in sys.argv or SKIP_EXTRACTION
SKIP_TRANSLATION = "--skip-translation" in sys.argv


# ════════════════════════════════════════════════════════════════════
# SSH HELPERS
# ════════════════════════════════════════════════════════════════════

def ssh_connect_ada():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ADA_HOST, username=ADA_USER, password=ADA_PASS, timeout=30)
    return client


def ssh_connect_gnode(ada):
    """Direct SSH connection to GPU_NODE using ada as a ProxyJump."""
    transport = ada.get_transport()
    channel = transport.open_channel("direct-tcpip", (GPU_NODE, 22), ("127.0.0.1", 0))
    gnode = paramiko.SSHClient()
    gnode.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    gnode.connect(GPU_NODE, username=ADA_USER, password=ADA_PASS, sock=channel, timeout=30)
    return gnode


def run_on_client(client, cmd, timeout=60):
    _, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    return out.strip(), err.strip()


# Keep alias for ada commands
run_on_ada = run_on_client


def run_nohup_launch(client, cmd, wait_for="LAUNCHED_PID=", timeout=30):
    """Fire a background nohup command and read until the marker line appears."""
    _, stdout, _ = client.exec_command(cmd)
    deadline = time.time() + timeout
    out = ""
    while time.time() < deadline:
        if stdout.channel.recv_ready():
            chunk = stdout.channel.recv(4096).decode("utf-8", errors="replace")
            out += chunk
            if wait_for in out:
                break
        elif stdout.channel.exit_status_ready():
            try:
                out += stdout.channel.recv(4096).decode("utf-8", errors="replace")
            except Exception:
                pass
            break
        time.sleep(0.2)
    return out.strip()


def sftp_put(client, local_path: str, remote_path: str):
    sftp = client.open_sftp()
    try:
        sftp.put(local_path, remote_path)
    finally:
        sftp.close()


def sftp_get(client, remote_path: str, local_path: str):
    sftp = client.open_sftp()
    try:
        sftp.get(remote_path, local_path)
    finally:
        sftp.close()


# ════════════════════════════════════════════════════════════════════
# PHASE 1 — TERM EXTRACTION VIA CLUSTER
# ════════════════════════════════════════════════════════════════════

def collect_md_files() -> dict:
    """Collect grade9 ch1-3 .md file contents as {relative_key: content}."""
    files = {}
    for ch in CHAPTERS:
        ch_dir = MD_ROOT / f"chapter{ch}"
        for md_file in sorted(ch_dir.glob("*.md")):
            key = f"grade{GRADE}/{SUBJECT}/chapter{ch}/{md_file.name}"
            files[key] = md_file.read_text(encoding="utf-8")
    return files


def run_extraction_on_cluster():
    """Upload .md files + extractor script, run on gnode047, download results."""
    print("\n[Phase 1] Term extraction via Qwen3-8B on gnode047")

    # Build input JSON locally
    files = collect_md_files()
    print(f"  Collected {len(files)} topic .md files")

    input_json_local = INTERMEDIATE / "grade9_input_for_extraction.json"
    with open(input_json_local, "w", encoding="utf-8") as f:
        json.dump(files, f, ensure_ascii=False)

    # Connect to cluster
    print("  Connecting to ada.iiit.ac.in...")
    ada = ssh_connect_ada()
    print("  Connected")

    # Direct connection to gnode via ProxyJump
    print(f"  Connecting to {GPU_NODE} via ProxyJump...")
    try:
        gnode = ssh_connect_gnode(ada)
        print(f"  {GPU_NODE} reachable")
    except Exception as e:
        print(f"  ERROR: Cannot reach {GPU_NODE}: {e}")
        ada.close()
        sys.exit(1)

    # Create working dirs
    work_dir = f"{ADA_HOME}/btp_translate"
    run_on_ada(ada, f"mkdir -p {work_dir}")

    scratch_work = f"{SCRATCH}/translate_work"
    run_on_client(gnode, f"mkdir -p {scratch_work}")

    # Upload input JSON to ada home via SFTP, then scp to gnode scratch
    print("  Uploading input JSON (~{:.0f} KB)...".format(
        input_json_local.stat().st_size / 1024))
    remote_input_ada = f"{work_dir}/grade9_input.json"
    sftp_put(ada, str(input_json_local), remote_input_ada)

    extractor_local = Path(__file__).parent / "_grade9_term_extractor.py"
    remote_extractor_ada = f"{work_dir}/_grade9_term_extractor.py"
    sftp_put(ada, str(extractor_local), remote_extractor_ada)

    # Copy from ada home to gnode scratch (run scp on ada)
    run_on_ada(ada, f"scp {remote_input_ada} {GPU_NODE}:{scratch_work}/grade9_input.json")
    run_on_ada(ada, f"scp {remote_extractor_ada} {GPU_NODE}:{scratch_work}/_grade9_term_extractor.py")

    # Run extraction — use run_nohup_launch for proper non-blocking fire-and-forget
    remote_output = f"{scratch_work}/grade9_terms.json"
    launch_cmd = (
        f"cd {scratch_work} && "
        f"nohup {VENV_PYTHON} _grade9_term_extractor.py "
        f"grade9_input.json grade9_terms.json "
        f"> {scratch_work}/extract_log.txt 2>&1 </dev/null & disown; echo LAUNCHED_PID=$!"
    )
    print("  Launching extraction on gnode047 (this takes ~3-5 min)...")
    out = run_nohup_launch(gnode, launch_cmd, wait_for="LAUNCHED_PID=", timeout=30)
    if "LAUNCHED_PID=" in out:
        pid = out.split("LAUNCHED_PID=")[-1].strip()
        print(f"  Process launched (PID={pid})")
    else:
        print(f"  Launch output: {out!r}")

    # Poll until done
    print("  Waiting for extraction to complete", end="", flush=True)
    max_wait = 600  # 10 min
    start = time.time()
    while time.time() - start < max_wait:
        time.sleep(20)
        check, _ = run_on_client(gnode, f"test -f {remote_output} && echo DONE || echo WAIT")
        if "DONE" in check:
            print(" done!")
            break
        # Show last log line
        log, _ = run_on_client(gnode, f"tail -1 {scratch_work}/extract_log.txt 2>/dev/null || echo '...'")
        print(f"\r  Waiting... [{log[:60]}]", end="", flush=True)
    else:
        print("\n  TIMEOUT: Extraction did not complete in 10 min")
        log, _ = run_on_client(gnode, f"tail -5 {scratch_work}/extract_log.txt 2>/dev/null")
        print(f"  Last log:\n{log}")
        gnode.close()
        ada.close()
        sys.exit(1)

    # Download result: scp from gnode to ada home, then sftp to local
    run_on_ada(ada, f"scp {GPU_NODE}:{remote_output} {work_dir}/grade9_terms.json")
    print(f"  Downloading terms JSON...")
    sftp_get(ada, f"{work_dir}/grade9_terms.json", str(TERMS_JSON))

    # Print quick summary from log
    log, _ = run_on_client(gnode, f"tail -3 {scratch_work}/extract_log.txt 2>/dev/null")
    print(f"  Cluster log:\n{log}")

    gnode.close()
    ada.close()
    print(f"  Terms saved to: {TERMS_JSON}")


# ════════════════════════════════════════════════════════════════════
# PHASE 2 — BUILD GLOSSARY VIA SARVAM API
# ════════════════════════════════════════════════════════════════════

def sarvam_translate_term(client, term: str, tgt_code: str) -> str:
    """Translate a single term via Sarvam API with retries."""
    for attempt in range(5):
        try:
            resp = client.text.translate(
                input=term,
                source_language_code="en-IN",
                target_language_code=tgt_code,
                model="sarvam-translate:v1",
            )
            return resp.translated_text.strip()
        except Exception as e:
            err = str(e)
            if "429" in err or "rate_limit" in err.lower():
                wait = 2 ** attempt
                print(f"\r  [rate limit] waiting {wait}s...", end="", flush=True)
                time.sleep(wait)
            else:
                print(f"\n  WARN: Sarvam error for '{term}': {e}")
                return term  # fallback to original
    return term


def build_glossary():
    """Translate all unique terms via Sarvam API and save master glossary."""
    print("\n[Phase 2] Building glossary via Sarvam API")

    with open(TERMS_JSON, encoding="utf-8") as f:
        terms_by_topic = json.load(f)

    # Collect all unique terms
    all_terms = set()
    for terms in terms_by_topic.values():
        all_terms.update(t.lower().strip() for t in terms if t.strip())
    all_terms = sorted(all_terms)

    print(f"  {len(all_terms)} unique terms to translate")

    try:
        from sarvamai import SarvamAI
    except ImportError:
        print("  ERROR: sarvamai not installed. Run: pip install sarvamai")
        sys.exit(1)

    client = SarvamAI(api_subscription_key=SARVAM_API_KEY)

    glossary = {}  # {term: {hi: "...", te: "...", od: "..."}}

    for i, term in enumerate(all_terms):
        trans = {}
        for lang in TARGET_LANGS:
            tgt_code = LANG_CODES[lang]
            translated = sarvam_translate_term(client, term, tgt_code)
            trans[lang] = translated
            time.sleep(0.3)  # rate limit

        glossary[term] = trans
        print(f"  [{i+1}/{len(all_terms)}] '{term}' → hi:'{trans['hi']}' te:'{trans['te']}' od:'{trans['od']}'")

    with open(GLOSSARY_JSON, "w", encoding="utf-8") as f:
        json.dump(glossary, f, indent=2, ensure_ascii=False)

    print(f"  Glossary saved to: {GLOSSARY_JSON}")
    return glossary


# ════════════════════════════════════════════════════════════════════
# PHASE 3 — TRANSLATE .MD FILES WITH GLOSSARY
# ════════════════════════════════════════════════════════════════════

# LaTeX split pattern (same as translator.py)
_LATEX_SPLIT = re.compile(r"(\$\$[^$]+\$\$|\$[^$]+\$)")

_SKIP_PATTERNS = [
    re.compile(r"^\s*$"),
    re.compile(r"^\s*---\s*$"),
    re.compile(r"^\s*```"),
    re.compile(r"^\$\$.*\$\$\s*$"),
    re.compile(r"^\s*!\["),
    re.compile(r"^\s*\[.*\]\(.*\)\s*$"),
]

_MD_PREFIX = re.compile(
    r"^(#{1,6}\s+|>\s*|\s*[-*]\s+|\s*\d+\.\s+|"
    r"\s*[\U0001F534\U0001F7E0\U0001F7E1\U0001F7E2\U0001F7E3\U0001F535]\s*|"
    r"\*\*[^*]+:\*\*\s*)"
)


def _should_skip(line: str) -> bool:
    return any(p.match(line) for p in _SKIP_PATTERNS)


def _split_latex(text: str):
    """Split text into [(segment, is_latex), ...]."""
    parts = []
    last = 0
    for m in _LATEX_SPLIT.finditer(text):
        if m.start() > last:
            parts.append((text[last:m.start()], False))
        parts.append((m.group(0), True))
        last = m.end()
    if last < len(text):
        parts.append((text[last:], False))
    return parts or [(text, False)]


def _apply_glossary_placeholders(text: str, sorted_terms: list) -> tuple:
    """Replace glossary terms with {{T_N}} placeholders.

    Returns (modified_text, {placeholder: term}) mapping.
    """
    mapping = {}  # {placeholder: original_term}
    modified = text
    for i, term in enumerate(sorted_terms):
        # Word-boundary pattern, case-insensitive
        try:
            pattern = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
        except re.error:
            continue
        if pattern.search(modified):
            ph = f"{{{{T{i}}}}}"
            modified = pattern.sub(ph, modified)
            mapping[ph] = term
    return modified, mapping


def _restore_placeholders(translated: str, mapping: dict, glossary: dict, lang: str) -> str:
    """Replace {{T_N}} placeholders with the pre-translated canonical terms."""
    result = translated
    for ph, term in mapping.items():
        canonical = glossary.get(term, {}).get(lang, term)
        # Try exact match first
        if ph in result:
            result = result.replace(ph, canonical)
        else:
            # Sarvam may have added/removed spaces around braces
            alt = ph.replace("{{", "{ {").replace("}}", "} }")
            result = result.replace(alt, canonical)
            # Last resort: match just the number pattern
            num = re.search(r"\d+", ph)
            if num:
                patterns_to_try = [
                    f"{{T{num.group(0)}}}",
                    f"T{num.group(0)}",
                    f"{{{{T{num.group(0)}}}}}",
                ]
                for p in patterns_to_try:
                    if p in result:
                        result = result.replace(p, canonical)
                        break
    return result


def _sarvam_translate_batch(texts: list, tgt_code: str, client) -> list:
    """Translate a list of text strings via Sarvam API."""
    results = []
    for text in texts:
        if not text.strip():
            results.append(text)
            continue
        for attempt in range(5):
            try:
                resp = client.text.translate(
                    input=text,
                    source_language_code="en-IN",
                    target_language_code=tgt_code,
                    model="sarvam-translate:v1",
                )
                results.append(resp.translated_text)
                time.sleep(0.25)
                break
            except Exception as e:
                err = str(e)
                if "429" in err or "rate_limit" in err.lower():
                    wait = 2 ** attempt
                    time.sleep(wait)
                else:
                    print(f"\n  WARN: Sarvam error: {e}")
                    results.append(text)
                    break
        else:
            results.append(text)
    return results


def translate_md_with_glossary(content: str, lang: str, glossary: dict,
                                sorted_terms: list, sarvam_client) -> str:
    """Translate markdown content while preserving LaTeX and using glossary.

    1. Split into lines
    2. For each translatable line:  split into [text, latex] segments
       → apply glossary placeholders to text segments
    3. Batch-translate all text segments via Sarvam
    4. Restore placeholders with canonical glossary translations
    5. Reassemble
    """
    tgt_code = LANG_CODES[lang]
    lines = content.split("\n")
    result_lines = list(lines)

    translatable = []   # [(line_idx, prefix, segments, [{ph: term}])]
    text_segs_flat = []  # flat list of (text_with_placeholders, {ph: term})

    in_math_block = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "$$":
            in_math_block = not in_math_block
            continue
        if in_math_block:
            continue
        if _should_skip(line):
            continue
        # Extract markdown prefix
        m = _MD_PREFIX.match(line)
        prefix = m.group(0) if m else ""
        text = line[len(prefix):]

        if not text.strip():
            continue

        segments = _split_latex(text)
        text_only = "".join(s for s, is_latex in segments if not is_latex).strip()
        if not text_only:
            continue
        if re.match(r"^[\d\s.,;:!?()\-–—|/\\]+$", text_only):
            continue

        # Apply glossary placeholders to each text segment
        processed_segs = []
        seg_mappings = []
        for seg_text, is_latex in segments:
            if is_latex:
                processed_segs.append((seg_text, is_latex))
                seg_mappings.append({})
            else:
                modified, mapping = _apply_glossary_placeholders(seg_text, sorted_terms)
                processed_segs.append((modified, is_latex))
                seg_mappings.append(mapping)

        entry_idx = len(translatable)
        translatable.append((idx, prefix, processed_segs, seg_mappings))

        for seg_idx, (seg_text, is_latex) in enumerate(processed_segs):
            if not is_latex and seg_text.strip():
                text_segs_flat.append((seg_text, seg_mappings[seg_idx], entry_idx, seg_idx))

    if not text_segs_flat:
        return content

    # Batch translate
    texts_to_send = [x[0] for x in text_segs_flat]
    translated = _sarvam_translate_batch(texts_to_send, tgt_code, sarvam_client)

    # Restore placeholders in translated segments
    restored = []
    for i, (orig_text, mapping, _, _) in enumerate(text_segs_flat):
        trans = translated[i] if i < len(translated) else orig_text
        if mapping:
            trans = _restore_placeholders(trans, mapping, glossary, lang)
        restored.append(trans)

    # Map restored back to entries
    flat_map = {}  # (entry_idx, seg_idx) -> restored_text
    for flat_i, (_, _, entry_idx, seg_idx) in enumerate(text_segs_flat):
        flat_map[(entry_idx, seg_idx)] = restored[flat_i]

    # Reassemble lines
    for entry_idx, (line_idx, prefix, segs, _) in enumerate(translatable):
        parts = []
        prev_latex = False
        for seg_idx, (seg_text, is_latex) in enumerate(segs):
            if is_latex:
                if parts and parts[-1] and parts[-1][-1] not in " \t([":
                    parts[-1] = parts[-1].rstrip() + " "
                parts.append(seg_text)
                prev_latex = True
            else:
                key = (entry_idx, seg_idx)
                trans_text = flat_map.get(key, seg_text)
                if prev_latex and trans_text and trans_text[0] not in " \t,.;:!?)]\n":
                    trans_text = " " + trans_text.lstrip()
                parts.append(trans_text)
                prev_latex = False
        result_lines[line_idx] = prefix + "".join(parts)

    return "\n".join(result_lines)


def translate_all_chapters(glossary: dict):
    """Translate all grade9 ch1-3 .md files and return translated content."""
    print("\n[Phase 3] Translating .md files via Sarvam API")

    # Sort terms by length (longest first for correct substitution order)
    sorted_terms = sorted(glossary.keys(), key=len, reverse=True)
    print(f"  Glossary: {len(sorted_terms)} terms")

    try:
        from sarvamai import SarvamAI
    except ImportError:
        print("ERROR: sarvamai not installed")
        sys.exit(1)

    client = SarvamAI(api_subscription_key=SARVAM_API_KEY)

    # {(chapter, topic_stem, lang): translated_md}
    results = {}

    for ch in CHAPTERS:
        ch_dir = MD_ROOT / f"chapter{ch}"
        md_files = sorted(ch_dir.glob("*.md"))
        print(f"\n  Chapter {ch}: {len(md_files)} topics")

        for md_file in md_files:
            content = md_file.read_text(encoding="utf-8")
            print(f"    [{md_file.stem}]", end="", flush=True)

            for lang in TARGET_LANGS:
                print(f" {lang.upper()}", end="", flush=True)
                translated = translate_md_with_glossary(
                    content, lang, glossary, sorted_terms, client
                )
                results[(ch, md_file.stem, lang)] = translated
            print()

    print(f"\n  Translated {len(results)} (topic × language) combinations")

    # Save to disk cache — keys are "ch|stem|lang"
    cache = {f"{ch}|{stem}|{lang}": md for (ch, stem, lang), md in results.items()}
    with open(TRANSLATIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False)
    print(f"  Translations cached to: {TRANSLATIONS_JSON}")

    return results


# ════════════════════════════════════════════════════════════════════
# PHASE 4 — UPLOAD TO MONGODB
# ════════════════════════════════════════════════════════════════════

def md_to_html_simple(content: str) -> str:
    """Simplified markdown → HTML for translated content.

    Handles the most common markdown structures used in the generated content.
    LaTeX ($...$, $$...$$) is passed through for client-side KaTeX rendering.
    """
    # Protect LaTeX from markdown processing
    latex_blocks = []

    def stash(m):
        idx = len(latex_blocks)
        latex_blocks.append(m.group(0))
        return f"LXBLK{idx}LXEND"

    content = re.sub(r"\$\$(.+?)\$\$", stash, content, flags=re.DOTALL)
    content = re.sub(r"\$([^\$\n]+?)\$", stash, content)

    lines = content.split("\n")
    html = []
    in_ul = in_ol = in_blockquote = False
    in_code = False
    in_table = False
    table_has_header = False

    def flush():
        nonlocal in_ul, in_ol, in_blockquote, in_table, table_has_header
        if in_ul:
            html.append("</ul>")
            in_ul = False
        if in_ol:
            html.append("</ol>")
            in_ol = False
        if in_blockquote:
            html.append("</blockquote>")
            in_blockquote = False
        if in_table:
            html.append("</table></div>")
            in_table = False
            table_has_header = False

    def inline(s):
        s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"~~(.+?)~~", r"<del>\1</del>", s)
        return s

    for line in lines:
        stripped = line.strip()

        # Code fence
        if stripped.startswith("```"):
            flush()
            in_code = not in_code
            if in_code:
                html.append('<pre><code>')
            else:
                html.append('</code></pre>')
            continue
        if in_code:
            html.append(line)
            continue

        # Empty line
        if not stripped:
            flush()
            continue

        # Horizontal rule
        if re.match(r"^-{3,}$", stripped):
            flush()
            html.append("<hr>")
            continue

        # Headers
        m = re.match(r"^(#{1,6})\s+(.*)", stripped)
        if m:
            flush()
            level = len(m.group(1))
            html.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue

        # Blockquote
        if stripped.startswith(">"):
            if not in_blockquote:
                flush()
                html.append("<blockquote>")
                in_blockquote = True
            text = re.sub(r"^>\s*", "", stripped)
            html.append(f"<p>{inline(text)}</p>")
            continue
        elif in_blockquote:
            html.append("</blockquote>")
            in_blockquote = False

        # Ordered list
        m = re.match(r"^\d+\.\s+(.*)", stripped)
        if m:
            if not in_ol:
                flush()
                html.append("<ol>")
                in_ol = True
            html.append(f"<li>{inline(m.group(1))}</li>")
            continue

        # Unordered list
        m = re.match(r"^[-*]\s+(.*)", stripped)
        if m:
            if not in_ul:
                flush()
                html.append("<ul>")
                in_ul = True
            html.append(f"<li>{inline(m.group(1))}</li>")
            continue

        # Markdown table
        if stripped.startswith("|") and stripped.endswith("|"):
            # Separator row (|---|---|)
            if re.match(r"^\|[\s:_-]+(\|[\s:_-]+)+\|$", stripped):
                table_has_header = True
                continue

            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not in_table:
                flush()
                html.append('<div class="table-wrap"><table class="key-formulas">')
                in_table = True
                # First row — treat as header
                html.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells) + "</tr>")
            else:
                html.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
            continue

        # Regular paragraph
        flush()
        html.append(f"<p>{inline(stripped)}</p>")

    flush()
    result = "\n".join(html)

    # Restore LaTeX
    for idx, block in enumerate(latex_blocks):
        result = result.replace(f"LXBLK{idx}LXEND", block)

    # Restore difficulty badges
    result = result.replace(
        "🟢 Easy",
        '<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold difficulty-easy">🟢 Easy</span>',
    )
    result = result.replace(
        "🟡 Medium",
        '<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold difficulty-medium">🟡 Medium</span>',
    )
    result = result.replace(
        "🔴 Hard",
        '<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold difficulty-hard">🔴 Hard</span>',
    )

    return result


def get_mongo_uri():
    uri = os.environ.get("MONGODB_URI")
    if uri:
        return uri
    env_file = ROOT / "webapp" / ".env.local"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("MONGODB_URI="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError("No MONGODB_URI found")


def upload_translations(translated_results: dict):
    """Convert translated md to HTML and update MongoDB topic.translations."""
    print("\n[Phase 4] Uploading translations to MongoDB")

    try:
        from pymongo import MongoClient
    except ImportError:
        print("ERROR: pymongo not installed")
        sys.exit(1)

    uri = get_mongo_uri()
    client = MongoClient(uri)
    db = client["btp-1"]
    topics_col = db["topics"]

    # Group results by (chapter, topic_stem)
    # Find matching MongoDB topics by grade/subject/chapter and topic_number
    updated = 0
    skipped = 0

    # Build a lookup: (chapter, topic number) -> topic document
    topic_lookup = {}
    for ch in CHAPTERS:
        docs = list(topics_col.find(
            {"grade": GRADE, "subject": SUBJECT, "chapter": ch},
            {"_id": 1, "order": 1, "title": 1}
        ))
        for doc in docs:
            topic_lookup[(ch, doc["order"])] = doc

    print(f"  Found {len(topic_lookup)} topics in MongoDB for grade{GRADE} ch{CHAPTERS}")

    # Group results by (chapter, topic_stem) → gather all langs
    topic_translations = {}  # {(ch, stem): {lang: html}}
    for (ch, stem, lang), md_content in translated_results.items():
        key = (ch, stem)
        if key not in topic_translations:
            topic_translations[key] = {}
        html_content = md_to_html_simple(md_content)
        topic_translations[key][lang] = html_content

    for (ch, stem), lang_content in topic_translations.items():
        # Parse topic number from stem (e.g., "1.2_Irrational_Numbers" → 2 within ch1)
        # The topic field in MongoDB is the sequential topic number
        # Stem is like "1.2_Irrational_Numbers" — first number after dot is the topic sub-number
        topic_num = None
        m = re.match(r"^(\d+)\.(\d+)_", stem)
        if m:
            topic_num = int(m.group(2))

        if topic_num is None:
            print(f"  SKIP: Cannot parse topic number from '{stem}'")
            skipped += 1
            continue

        # Find the topic document
        topic_doc = None
        for (t_ch, t_num), doc in topic_lookup.items():
            if t_ch == ch and t_num == topic_num:
                topic_doc = doc
                break

        if topic_doc is None:
            print(f"  SKIP: No MongoDB doc for ch{ch} topic{topic_num} (stem={stem})")
            skipped += 1
            continue

        # Build translations update
        trans_update = {}
        for lang, html in lang_content.items():
            trans_update[f"translations.{lang}"] = {"content": html}

        result = topics_col.update_one(
            {"_id": topic_doc["_id"]},
            {"$set": trans_update}
        )

        lang_list = ", ".join(lang_content.keys())
        print(f"  Grade{GRADE} Ch{ch} Topic{topic_num} ({stem[:30]}): updated [{lang_list}]")
        updated += result.modified_count

    print(f"\n  Done: {updated} topics updated, {skipped} skipped")
    client.close()


# ════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("Grade 9 Translation Pipeline")
    print("=" * 60)
    print(f"Target: Grade {GRADE} | Chapters {CHAPTERS} | {SUBJECT}")
    print(f"Languages: {', '.join(LANG_NAMES[l] for l in TARGET_LANGS)}")

    # Phase 1: Extract terms
    if not SKIP_EXTRACTION:
        if TERMS_JSON.exists():
            print(f"\n[Phase 1] Terms already at {TERMS_JSON} — skipping extraction")
            print("  (use --skip-extraction flag or delete the file to re-run)")
        else:
            run_extraction_on_cluster()
    else:
        print("\n[Phase 1] Skipped (--skip-extraction)")

    if not TERMS_JSON.exists():
        print(f"ERROR: {TERMS_JSON} not found. Cannot proceed.")
        sys.exit(1)

    # Phase 2: Build glossary
    if not SKIP_GLOSSARY:
        if GLOSSARY_JSON.exists():
            print(f"\n[Phase 2] Glossary already at {GLOSSARY_JSON} — skipping")
            print("  (delete the file to rebuild glossary)")
            with open(GLOSSARY_JSON, encoding="utf-8") as f:
                glossary = json.load(f)
        else:
            glossary = build_glossary()
    else:
        print("\n[Phase 2] Skipped (--skip-glossary)")
        if GLOSSARY_JSON.exists():
            with open(GLOSSARY_JSON, encoding="utf-8") as f:
                glossary = json.load(f)
        else:
            print(f"ERROR: {GLOSSARY_JSON} not found. Cannot proceed.")
            sys.exit(1)

    # Phase 3: Translate content
    if SKIP_TRANSLATION and TRANSLATIONS_JSON.exists():
        print(f"\n[Phase 3] Loading cached translations from {TRANSLATIONS_JSON}")
        with open(TRANSLATIONS_JSON, encoding="utf-8") as f:
            cache = json.load(f)
        translated = {}
        for key, md in cache.items():
            parts = key.split("|", 2)
            translated[(int(parts[0]), parts[1], parts[2])] = md
        print(f"  Loaded {len(translated)} (topic × language) combinations")
    elif TRANSLATIONS_JSON.exists() and not SKIP_TRANSLATION:
        print(f"\n[Phase 3] Cache found at {TRANSLATIONS_JSON}")
        print("  Use --skip-translation to reuse it, or delete the file to retranslate.")
        translated = translate_all_chapters(glossary)
    else:
        translated = translate_all_chapters(glossary)

    # Phase 4: Upload to MongoDB
    upload_translations(translated)

    print("\n" + "=" * 60)
    print("Translation pipeline complete!")
    print(f"Glossary: {GLOSSARY_JSON}")
    print(f"Terms: {TERMS_JSON}")
    print("=" * 60)


if __name__ == "__main__":
    main()
