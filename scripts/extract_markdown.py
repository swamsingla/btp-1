#!/usr/bin/env python3
"""
NCERT PDF -> Markdown with formulas as LaTeX (MinerU, fully local)
===================================================================
Replaces the PyMuPDF text layer, which breaks maths ("1/5" -> "1 5",
"7^2" -> "72") and misses whole equations in the science books.

Every PDF under data/input/ is parsed by a LOCAL MinerU parse-server and
written to the same relative path under data/intermediate/markdown/:
  data/input/grade11/physics/part1/chapter2.pdf
    -> data/intermediate/markdown/grade11/physics/part1/chapter2.md

Before parsing, the script refuses to run unless MinerU is configured for
local parsing (parse_server.local.mode = managed) and telemetry is disabled,
so no document ever leaves the machine. Existing outputs are skipped, so the
run can be stopped and resumed. Timings go to _extraction_log.jsonl.

Setup (once):
  mineru-models-download --tier standard
  mineru server start
  mineru telemetry disable
  mineru config set parse_server.local.mode managed

Usage:
  python scripts/extract_markdown.py                      # all PDFs
  python scripts/extract_markdown.py --only grade10/maths # subset (path prefix)
  python scripts/extract_markdown.py --mineru C:/path/to/mineru.exe
"""

import argparse
import itertools
import json
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "intermediate" / "markdown"
LOG_PATH = OUTPUT_DIR / "_extraction_log.jsonl"

PARSE_TIMEOUT_SEC = 3600
WARMUP_RETRIES = 20      # first requests after a server start return "not ready"
WARMUP_WAIT_SEC = 30


def run_mineru(mineru: str, *args: str, timeout: int = 120) -> subprocess.CompletedProcess:
    return subprocess.run(
        [mineru, *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout,
    )


def check_local_only(mineru: str) -> None:
    """Exit unless MinerU parses on this machine and telemetry is off.

    Two local setups are allowed:
      managed      - MinerU starts its own parse-server (single GPU)
      self_hosted  - a parse-server/router we started, but only at localhost
    """
    run_mineru(mineru, "server", "start", timeout=300)
    mode = run_mineru(mineru, "config", "get", "parse_server.local.mode").stdout
    url = run_mineru(mineru, "config", "get", "parse_server.local.self_hosted_url").stdout
    telemetry = run_mineru(mineru, "telemetry", "status").stdout

    problems = []
    if "managed" in mode:
        pass
    elif "self_hosted" in mode:
        if not any(host in url for host in ("127.0.0.1", "localhost", "0.0.0.0")):
            problems.append(f"self_hosted_url is not local: {url.strip()}")
    else:
        problems.append("parse_server.local.mode is neither 'managed' nor 'self_hosted' "
                        "(run: mineru config set parse_server.local.mode managed)")
    if "state: disabled" not in telemetry:
        problems.append("telemetry is not disabled (run: mineru telemetry disable)")
    if problems:
        sys.exit("Refusing to parse:\n  - " + "\n  - ".join(problems))


def main() -> None:
    p = argparse.ArgumentParser(description="Extract NCERT PDFs to Markdown+LaTeX with local MinerU")
    p.add_argument("--mineru", default="mineru", help="Path to the mineru executable")
    p.add_argument("--only", default="", help="Only PDFs whose path under data/input starts with this")
    p.add_argument("--tier", default="standard", choices=["basic", "standard"])
    p.add_argument("--workers", type=int, default=1,
                   help="PDFs to parse at once (use ~1 per GPU when a router fans out across GPUs)")
    args = p.parse_args()

    pdfs = sorted(
        pdf for pdf in INPUT_DIR.rglob("*.pdf")
        if pdf.relative_to(INPUT_DIR).as_posix().startswith(args.only)
    )
    todo = [pdf for pdf in pdfs if not (OUTPUT_DIR / pdf.relative_to(INPUT_DIR)).with_suffix(".md").exists()]
    print(f"{len(pdfs)} PDFs matched, {len(pdfs) - len(todo)} already extracted, {len(todo)} to do")
    if not todo:
        return

    check_local_only(args.mineru)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    log_lock = threading.Lock()
    done = itertools.count(1)
    failed = 0

    def extract(pdf: Path) -> bool:
        rel = pdf.relative_to(INPUT_DIR)
        out = (OUTPUT_DIR / rel).with_suffix(".md")
        out.parent.mkdir(parents=True, exist_ok=True)

        start = time.time()
        # The parse-server loads its models lazily, so the first requests after a
        # restart come back "not ready". Wait it out instead of failing the file.
        for attempt in range(WARMUP_RETRIES):
            try:
                result = run_mineru(
                    args.mineru, "parse", str(pdf),
                    "--tier", args.tier, "--pages", "all",
                    "--wait", str(PARSE_TIMEOUT_SEC), "--output", str(out), "--json",
                    timeout=PARSE_TIMEOUT_SEC + 120,
                )
                ok = result.returncode == 0 and out.exists() and out.stat().st_size > 0
                error = "" if ok else (result.stderr or result.stdout)[-500:]
            except subprocess.TimeoutExpired:
                ok, error = False, "timeout"
            if ok or not any(s in error for s in ("engine_unavailable", "not ready", "engine_starting")):
                break
            time.sleep(WARMUP_WAIT_SEC)
        seconds = round(time.time() - start, 1)

        if not ok:
            out.unlink(missing_ok=True)  # don't leave a partial file that would be skipped next run
        with log_lock:
            with LOG_PATH.open("a", encoding="utf-8") as log:
                log.write(json.dumps({"pdf": rel.as_posix(), "ok": ok, "seconds": seconds, "error": error}) + "\n")
            print(f"[{next(done)}/{len(todo)}] {'ok  ' if ok else 'FAIL'} {rel.as_posix()} ({seconds}s)", flush=True)
        return ok

    if args.workers > 1:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            failed = sum(1 for ok in pool.map(extract, todo) if not ok)
    else:
        failed = sum(1 for pdf in todo if not extract(pdf))

    print(f"Done: {len(todo) - failed} extracted, {failed} failed. Log: {LOG_PATH.relative_to(BASE_DIR)}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
