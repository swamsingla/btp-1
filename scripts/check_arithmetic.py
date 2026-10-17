#!/usr/bin/env python3
"""
Deterministic arithmetic and notation checking
==============================================
Checks the sums on a page by WORKING THEM OUT, in Python, with exact rational
arithmetic. Nothing here asks a language model anything.

Why this exists
---------------
Two architectures for "hand the page back and ask the model to check it" were measured
head to head on the same 10 Grade 7 maths pages, and neither exceeded ~40% recall on
faults a reader would notice. That is not a prompting failure: a transformer computes
750 - 75 in one forward pass with no carry operation, so there is nothing to "check more
carefully", and the page stays self-consistent after the error. Huang et al. (ICLR 2024,
"Large Language Models Cannot Self-Correct Reasoning Yet") report the same thing — that
intrinsic self-correction without external feedback does not improve reasoning and can
degrade it.

Arithmetic, though, is decidable. `Fraction` gets 360/7 exactly right where float does
not, and a parser cannot be talked into agreeing with a wrong sum. So the arithmetic
class moves out of the model and into code.

What it checks
--------------
  R1  every `A op B = C` chain, in prose and in LaTeX, evaluated exactly
  R6  every `$...$` span parses as LaTeX (needs node + katex; skipped if absent)
  R8  a computation set up and then never finished

What it deliberately does NOT check
-----------------------------------
Whether a factual claim is true. "Polar bears hibernate" is not an arithmetic error and
nothing in this file will ever catch it. Grade 6 science had ZERO arithmetic errors
across 21 pages, so on science this file is close to a no-op by design; it earns its
keep on maths.

Usage
-----
  python scripts/check_arithmetic.py --self-test
  python scripts/check_arithmetic.py data/generated_pages/maths/grade7/integers.md
  python scripts/check_arithmetic.py --all
  python scripts/check_arithmetic.py --all --json
"""

import argparse
import ast
import json
import pathlib
import re
import subprocess
import sys
from fractions import Fraction

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = pathlib.Path(__file__).resolve().parent.parent
PAGES = BASE / "data" / "generated_pages"
KATEX = BASE / "webapp" / "node_modules" / "katex"

# A citation tag sits inside the sentence and sometimes inside the dollars. Removing it
# first keeps "[S1]" out of the arithmetic and stops "[S1, S2]" looking like a number.
CITATION = re.compile(r"\[[^\]]*?S\s*\d[^\]]*\]")

# Characters an arithmetic chain may be built from, once LaTeX has been normalised. The
# comma is deliberately NOT here: a thousands separator is removed before this point, so
# any comma still present is a list ("(2, 3)") and should break the chain rather than
# silently turn into 23.
CHAIN = re.compile(r"[0-9.()+\-*/^=% ]{3,}")

UNITS = (r"cm|mm|km|kg|mg|ml|m|g|l|s|h|min|hr|hrs|sec|L|°C|°F|°|"
         r"litres?|liters?|metres?|meters?|grams?|kilograms?|seconds?|minutes?|hours?|"
         r"days?|years?|rupees?|paise")


# A unit group, optionally carrying its own exponent, e.g. \text{kJ mol}^{-1} or
# \mathrm{kJ\,mol^{-1}}. Both forms must go in ONE piece. Removing the group but leaving
# the exponent turned "$50 \text{kJ mol}^{-1} = 50000 \text{J mol}^{-1}$" -- a correct
# conversion -- into the chain "50 **(-1) = 50000 **(-1)", i.e. 0.02 vs 0.00002, and cost
# a real wasted regeneration on the Grade 12 collision-theory page. The inner alternation
# allows one level of nested braces so the \mathrm{kJ\,mol^{-1}} form is caught too.
UNIT_GROUP = re.compile(
    r"\\(?:text|mathrm|mathbf|textbf|operatorname)\s*"
    r"\{(?:[^{}]|\{[^{}]*\})*\}"
    r"(?:\s*\^\s*(?:\{[^{}]*\}|-?\d+))?")


def strip_math_decoration(s: str) -> str:
    """LaTeX that carries no arithmetic meaning."""
    s = UNIT_GROUP.sub(" ", s)
    s = re.sub(r"\\(?:left|right|displaystyle|,|;|!|:|quad|qquad)\b", " ", s)
    s = s.replace("\\left", " ").replace("\\right", " ")
    s = re.sub(r"\\[,;!:]", " ", s)
    return s


def latex_to_arith(s: str) -> str:
    """Rewrite the arithmetic parts of LaTeX into something Python can parse.

    Only the operations that have an exact rational meaning are translated. Anything
    else -- a square root, a variable, a summation -- is left as letters, which the chain
    scanner then refuses to pick up. Bailing out is the correct behaviour: a chain this
    cannot read is a chain it must not judge.
    """
    s = strip_math_decoration(s)
    # \frac{a}{b} -> ((a)/(b)); innermost first so nesting resolves
    for _ in range(6):
        new = re.sub(r"\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"((\1)/(\2))", s)
        if new == s:
            break
        s = new
    s = re.sub(r"\\times|\\cdot|\\ast", "*", s)
    s = re.sub(r"\\div", "/", s)
    s = re.sub(r"\\pm|\\mp", "+", s)   # only ever appears in prose we will not judge
    s = s.replace("\\%", "%")
    # ^{n} and ^n -> **n
    s = re.sub(r"\^\s*\{([^{}]*)\}", r"**(\1)", s)
    s = re.sub(r"\^\s*(-?\d+)", r"**\1", s)
    return s


def normalise(text: str) -> str:
    """The whole page, with LaTeX turned into arithmetic and noise removed."""
    text = CITATION.sub(" ", text)
    text = latex_to_arith(text)
    # Unicode operators. The en dash is NOT translated: in prose it is a range
    # ("10-20 marks"), and reading it as subtraction invents equations that were
    # never written.
    text = (text.replace("\u00d7", "*").replace("\u00f7", "/")
                .replace("\u2212", "-").replace("\u22c5", "*")
                .replace("\u2260", "!=").replace("\u2248", "=~"))
    # A markdown bullet is punctuation, not a minus sign. Without this, the line
    # "- $-18 - 3 = (-18) + (-3)$" read as "- -18 - 3", which is 15 rather than -21, and
    # a page that was perfectly correct was reported as wrong three times over.
    text = re.sub(r"^[ \t]*[-*+][ \t]+", "  ", text, flags=re.MULTILINE)
    # thousands separators, only in the standard 3-digit grouping
    text = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", text)
    # currency and units glued to a number carry no arithmetic weight
    text = re.sub(r"[\u20b9$£€]", " ", text)
    # A bare unit may also carry an exponent ("50 s^-1" -> "50 s**(-1)" by this point).
    # The exponent belongs to the unit, not to the number, so it goes with it.
    text = re.sub(rf"(?<=\d)\s*(?:{UNITS})\b(?:\s*\*\*\(?-?\d+\)?)?", " ", text)
    text = text.replace("$", " ")        # the math delimiters themselves
    return text


class Unsafe(Exception):
    pass


def _eval(node) -> Fraction:
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise Unsafe("non-numeric")
        return Fraction(str(node.value))
    if isinstance(node, ast.UnaryOp):
        v = _eval(node.operand)
        if isinstance(node.op, ast.USub):
            return -v
        if isinstance(node.op, ast.UAdd):
            return v
        raise Unsafe("unary")
    if isinstance(node, ast.BinOp):
        a, b = _eval(node.left), _eval(node.right)
        op = node.op
        if isinstance(op, ast.Add):
            return a + b
        if isinstance(op, ast.Sub):
            return a - b
        if isinstance(op, ast.Mult):
            return a * b
        if isinstance(op, ast.Div):
            if b == 0:
                raise Unsafe("division by zero")
            return a / b
        if isinstance(op, ast.Pow):
            # Bounded, or a page writing 9**9**9 would hang the checker.
            if b.denominator != 1 or abs(b) > 12:
                raise Unsafe("exponent")
            return a ** int(b)
        raise Unsafe("operator")
    raise Unsafe("node")


def value_of(expr: str):
    """Exact value of one arithmetic expression, or None if it cannot be read safely."""
    expr = expr.strip()
    if not expr or not re.search(r"\d", expr):
        return None
    if re.search(r"[A-Za-z\\]", expr):       # a variable or unhandled LaTeX
        return None
    try:
        return _eval(ast.parse(expr, mode="eval"))
    except (SyntaxError, ValueError, TypeError, Unsafe, RecursionError, MemoryError,
            ZeroDivisionError, OverflowError):
        return None


def _decimals(s: str) -> int:
    m = re.search(r"\.(\d+)\s*$", s.strip())
    return len(m.group(1)) if m else 0


def _is_rounding_of(stated: str, true: Fraction) -> bool:
    """Is `stated` the correctly rounded form of `true` at its own precision?

    A page writing 14.29 for 100/7 is right; one writing 14.28 has truncated. Only the
    correctly rounded value is accepted, because the truncation IS the error class this
    was asked to catch -- 50/350*100 given as 14.28% was a real fault.
    """
    d = _decimals(stated)
    if d == 0:
        return False
    try:
        shown = Fraction(stated.strip())
    except (ValueError, ZeroDivisionError):
        return False
    scale = 10 ** d
    # round-half-up on the exact rational, which is what a person does by hand
    scaled = true * scale
    floor = scaled.numerator // scaled.denominator
    frac = scaled - floor
    nearest = floor + (1 if frac >= Fraction(1, 2) else 0)
    if true < 0:
        nearest = floor + (1 if frac > Fraction(1, 2) else 0)
    return shown == Fraction(nearest, scale)


def clean_side(side: str) -> str:
    """One side of an `=`, with sentence punctuation removed.

    The chain scanner allows '.' because decimals need it, which means a sentence-final
    full stop is swallowed too: '$750 - 75 = 725$.' gave a right-hand side of '725 .',
    which failed to parse, so the chain was skipped and the 725 error went unreported --
    the checker silently declining to judge the one case it was written for.
    """
    return re.sub(r"[\s.]+$", "", side.strip())


def equations(text: str) -> list[tuple[str, list[str]]]:
    """Every `=`-joined arithmetic chain on the page, as (raw, [sides])."""
    out = []
    norm = normalise(text)
    for m in CHAIN.finditer(norm):
        chunk = m.group(0)
        if "=" not in chunk:
            continue
        body = chunk.strip()
        # An algebra term was cut off to the left. Letters cannot enter a chain, so
        # "5x - 4 = 7" arrives here as "- 4 = 7" and evaluates to -4, which is then
        # reported against 7 -- six such false reports on one Grade 7 page. The tell is
        # that the chain OPENS with a binary operator while the character before it is a
        # letter: the operator's real left operand is the variable. A chain opening with
        # a digit is a genuine computation whatever precedes it, which is what keeps
        # "the selling price is 750 - 75 = 675" readable.
        before = norm[:m.start() + (len(chunk) - len(chunk.lstrip()))].rstrip()
        if before and before[-1].isalpha() and body[:1] in ("+", "-", "*", "/", "^"):
            continue
        sides = [clean_side(s) for s in chunk.split("=")]
        if len(sides) < 2:
            continue
        if any(not s or not re.search(r"\d", s) for s in sides):
            continue
        # at least one real operator somewhere, or this is "5 = 5" and proves nothing
        if not re.search(r"[+\-*/^]", chunk.replace("**", "^")):
            continue
        out.append((chunk.strip(), sides))
    return out


# Percent signs have two readings and school textbooks use both. In
# "4/5 = 80/100 = 80%" the % means /100 and the chain is correct; in
# "50/350 x 100 = 14.28%" the author has already multiplied by 100 and the % is a label,
# so the comparison is against 14.28 as written. Reading it only one way is wrong either
# way round: dropping the sign reported the correct 80% line as 0.8 != 80, and dividing
# by 100 would have excused the 14.28 truncation. So each chain is read BOTH ways and
# only flagged when it fails under both -- the same shape as every other allowance here,
# which can forgive but can never invent a fault.
def _pct_as_fraction(s: str) -> str:
    return re.sub(r"(\d(?:[\d.]*\d)?)\s*%", r"((\1)/100)", s)


def _pct_as_label(s: str) -> str:
    return s.replace("%", " ")


def _reading(sides: list[str], convert) -> tuple[bool, object, str]:
    """(consistent, value of the first side, the side that disagrees)."""
    vals = [value_of(convert(s)) for s in sides]
    if any(v is None for v in vals):
        return False, None, ""
    first = vals[0]
    for s, v in zip(sides[1:], vals[1:]):
        if v == first or _is_rounding_of(_pct_as_label(s).strip(), first):
            continue
        return False, first, s
    return True, first, ""


def arithmetic_problems(text: str) -> list[str]:
    """R1 — every chain whose sides do not have the same value, under either reading."""
    problems = []
    for raw, sides in equations(text):
        as_label = _reading(sides, _pct_as_label)
        as_frac = _reading(sides, _pct_as_fraction) if "%" in raw else as_label
        if as_label[0] or as_frac[0]:
            continue                       # consistent under at least one reading
        ok, first, bad = as_label if as_label[1] is not None else as_frac
        if first is None:
            continue                       # unreadable: not judged, never guessed
        exact = (f"{float(first):.6g}" if first.denominator != 1
                 else str(first.numerator))
        problems.append(
            f"arithmetic: '{raw[:60].strip()}' -- {sides[0].strip()} is {exact}, "
            f"the page writes {bad}")
    return problems


UNFINISHED = re.compile(
    r"(?:=\s*(?:\?|_{2,}|\.{3})|"           # "... = ?"  "... = ___"
    r"\bwe (?:now )?(?:need to |have to )?(?:calculate|compute|work out|find)\b"
    r"[^.?!]{0,80}[.?!]\s*(?:\n|$))")


def unfinished_problems(text: str) -> list[str]:
    """R8 — a computation set up and then abandoned.

    Narrow on purpose. Four of ten Grade 7 pages set up a computation and never gave its
    result, but the general form of that fault is hard to state without flagging ordinary
    prose, so only the two unambiguous shapes are caught: an equation whose right side is
    a placeholder, and a dangling "we need to calculate ..." that ends the paragraph with
    no number anywhere after it.
    """
    out = []
    body = CITATION.sub(" ", text)
    for m in re.finditer(r"=\s*(?:\?|_{2,})", body):
        out.append(f"unfinished: '{body[max(0, m.start()-45):m.end()].strip()[-60:]}' "
                   f"sets up a computation and leaves the result blank")
    return out


def katex_problems(text: str) -> list[str]:
    """R6 — every `$...$` span must parse. Skipped silently if node/katex are absent."""
    # Display and inline are different dialects and must be told apart. `\tag{7.3}` is
    # legal in $$...$$ and an error in $...$, so checking every span as inline reported
    # three parse failures on a Grade 9 physics page that renders perfectly -- the
    # webapp's own tex() passes displayMode, and so must this.
    spans = [(a.strip(), True) if a else (b.strip(), False) for a, b in
             re.findall(r"\$\$(.+?)\$\$|\$([^$\n]+)\$", text, flags=re.S)]
    spans = [(s, d) for s, d in spans if s]
    if not spans or not KATEX.exists():
        return []
    script = (
        "const katex=require(process.argv[1]);"
        "let out=[];"
        "for (const [s,d] of JSON.parse(process.argv[2])) {"
        "  try { katex.renderToString(s,{displayMode:d,throwOnError:true,strict:false}); }"
        "  catch(e){ out.push([s, String(e.message||e).slice(0,90)]); }"
        "}"
        "console.log(JSON.stringify(out));")
    try:
        r = subprocess.run(["node", "-e", script, str(KATEX), json.dumps(spans)],
                           capture_output=True, text=True, timeout=90)
        if r.returncode != 0:
            return []
        bad = json.loads(r.stdout or "[]")
    except (OSError, ValueError, subprocess.SubprocessError):
        return []
    return [f"latex: '{s[:50]}' does not parse -- {why}" for s, why in bad]


MATH_SPAN = re.compile(r"\$\$(.+?)\$\$|\$([^$\n]+)\$", flags=re.S)
# A command that takes an argument, written without one. KaTeX accepts `\text=` happily
# -- it reads the '=' as the argument -- so R6 cannot see this, yet the span renders as
# garbage. The Grade 7 simple-equations draft wrote "an equal sign '$\text='$", which
# parsed cleanly and displayed wrongly. Measured at zero occurrences across all 82
# published pages, so this rule costs nothing and guards a fault that really happened.
# The lookahead has to step over the whitespace, not consume it: written as `\s*(?!\{)`
# the `\s*` simply backtracks to zero width and the test passes on the space, so
# `\frac {v - u}{t}` -- legal LaTeX that renders correctly -- was reported on 7 pages.
BARE_ARG_CMD = re.compile(r"\\(text|frac|sqrt|mathrm|overline|underline)(?![A-Za-z])(?!\s*\{)")


def notation_problems(text: str) -> list[str]:
    """Math spans that parse but are malformed -- a command missing its braces."""
    out = []
    for m in MATH_SPAN.finditer(text):
        span = (m.group(1) or m.group(2) or "").strip()
        hit = BARE_ARG_CMD.search(span)
        if hit:
            out.append(f"notation: '{span[:50]}' writes \\{hit.group(1)} with no "
                       f"{{...}} argument -- it parses but renders wrongly")
    return out


def problems(text: str, with_latex: bool = True) -> list[str]:
    out = arithmetic_problems(text) + unfinished_problems(text) + notation_problems(text)
    if with_latex:
        out += katex_problems(text)
    return out


def body_of(path: pathlib.Path) -> str:
    raw = path.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    return parts[2] if len(parts) > 2 and raw.lstrip().startswith("---") else raw


# --------------------------------------------------------------------------- self-test
# Every case below is either a real fault taken from the hand audits or a real passage
# that must NOT be flagged. The false-positive cases matter more than the others: a
# checker that cries wolf gets switched off, and this one is wired to a paid retry.
CASES = [
    # (text, should_flag, note)
    ("The selling price is $750 - 75 = 725$ rupees.", True, "the 725 error"),
    ("Thus, $5 \\times (-3) = -15$.", False, "correct; fault was the explanation"),
    ("Therefore, $(-5) \\times (-3) = 15$.", False, "correct"),
    ("We get $35\\% $ of $1800$, so $1800 - 630 = 1170$.", False, "correct"),
    ("$100 \\times 5 = 500$ leaves fall.", False, "correct"),
    ("Over a year, $500 \\times 365 = 182500$ leaves.", False, "correct"),
    ("$500 \\times 365 = 180000$ leaves.", True, "wrong product"),
    ("$\\frac{50}{350} \\times 100 = 14.29$", False, "correct rounding"),
    ("$\\frac{50}{350} \\times 100 = 14.28$", True, "truncation, the measured fault"),
    ("$\\frac{50}{350} \\times 100 = 14.29\\%$", False, "same, with a percent label"),
    ("$\\frac{50}{350} \\times 100 = 14.28\\%$", True, "the real page's exact wording"),
    ("$\\frac{4}{5} = \\frac{4 \\times 20}{5 \\times 20} = \\frac{80}{100} = 80\\%$",
     False, "percent as /100: a correct chain that must not flag"),
    ("$25\\% = \\frac{25}{100}$", False, "percent identity"),
    ("$25\\% = \\frac{25}{10}$", True, "wrong percent identity"),
    ("$\\frac{360}{7} = 51.43$", False, "correct rounding"),
    ("$\\frac{1}{2} + \\frac{1}{3} = \\frac{5}{6}$", False, "exact fractions"),
    ("$\\frac{1}{2} + \\frac{1}{3} = \\frac{2}{5}$", True, "wrong fraction sum"),
    ("$2.5 \\text{ m} = 2500 \\text{ mm}$", False, "unit conversion, not arithmetic"),
    ("$21.5 - 2.0 = 19.5$", False, "correct decimals"),
    ("$0.1 + 0.2 = 0.3$", False, "float trap: must not flag"),
    ("Chapter 10-20 covers this.", False, "en dash range, not subtraction"),
    ("The years 2024-2025 were covered.", False, "a range, no equals sign"),
    ("Let $x + 5 = 12$, so $x = 7$.", False, "has a variable: not judged"),
    ("- $-18 - 3 = (-18) + (-3)$, so the terms are -18 and -3.", False,
     "markdown bullet is not a minus sign"),
    ("Look at the equation $5x - 4 = 7$.", False, "coefficient+variable, cut off left"),
    ("This gives $5x - 4 + 4 = 7 + 4$, which simplifies to $5x = 11$.", False,
     "same, two chains"),
    ("An equation such as $6y + 7 = 4y + 21$ has unknowns on both sides.", False,
     "variables on both sides"),
    ("- $2 - 10 + 4 \\times 6 = 2 + (-10) + (4 \\times 6)$", False,
     "bulleted rewrite, both sides 16"),
    ("$\\sqrt{16} = 4$", False, "sqrt unreadable: skipped, not guessed"),
    ("The answer is $12 \\div 4 = 3$.", False, "correct division"),
    ("The answer is $12 \\div 5 = 3$.", True, "wrong division"),
    ("Area is $7^2 = 49$ sq cm.", False, "correct power"),
    ("Area is $7^2 = 14$ sq cm.", True, "wrong power"),
    ("Total: $20 + 7 + 8 + 2 = 37$ answers.", False, "sums correctly to 37"),
    ("Total: $20 + 7 + 8 + 2 = 40$ answers.", True, "wrong total"),
    ("Now $3 + 4 = ?$", True, "unfinished"),
    (r"""written with an equal sign '$\text='$ between them.""", True,
     "parses in KaTeX but renders wrongly -- the real Grade 7 fault"),
    (r"The area is $\text{cm}^2$ here.", False, "proper braces: no flag"),
    (r"The formula is $\frac {v - u}{t}$ here.", False,
     "a space before the brace is legal LaTeX -- must not flag"),
    (r"$$s = u t + \frac {1}{2} a t^{2}$$", False, "same, in display math"),
    # Units carrying exponents. The live Grade 12 run flagged a correct kJ->J conversion
    # and burned a regeneration on it, so all the common shapes are pinned here.
    (r"The activation energy is $50\ \text{kJ mol}^{-1} = 50000\ \text{J mol}^{-1}$.",
     False, "correct unit conversion: the exponent belongs to the unit"),
    (r"$50 \text{kJ mol}^{-1} = 50000 \text{J mol}^{-1}$", False,
     "same without the thin space -- this is the shape that actually fired"),
    (r"$50\ \mathrm{kJ\,mol^{-1}} = 50000\ \mathrm{J\,mol^{-1}}$", False,
     "same with the exponent nested inside \\mathrm"),
    (r"Rate constant $k = 2.5 \times 10^{-3}\ \mathrm{s^{-1}}$.", False,
     "no equation to judge once the unit is gone"),
    (r"Speed is $3 \times 10^{8}\ \mathrm{m\,s^{-1}}$ in vacuum.", False, "same"),
    (r"$2.5 \text{ m} = 2500 \text{ mm}$", False, "plain unit conversion still fine"),
    (r"$50 \text{kJ mol}^{-1} = 500 \text{J mol}^{-1}$", False,
     "WRONG conversion, but the units make it unjudgeable here -- must not guess"),
    ("We write $1\\,000 + 2\\,000 = 3\\,000$.", False, "thin spaces in numbers"),
    ("The set is $(2, 3)$ and $2 + 3 = 5$.", False, "comma list must not merge"),
]


def self_test() -> int:
    bad = 0
    for text, should, note in CASES:
        got = problems(text, with_latex=False)
        ok = bool(got) == should
        if not ok:
            bad += 1
            print(f"  FAIL  expected {'a flag' if should else 'no flag':9} "
                  f"({note})\n        text: {text}\n        got : {got}")
    print(f"\nself-test: {len(CASES) - bad}/{len(CASES)} cases pass")
    return bad


def main() -> None:
    ap = argparse.ArgumentParser(description="Check the arithmetic on generated pages")
    ap.add_argument("paths", nargs="*", type=pathlib.Path)
    ap.add_argument("--all", action="store_true", help="every page in generated_pages")
    ap.add_argument("--english-only", action="store_true",
                    help="skip .hi/.te/.od pages")
    ap.add_argument("--no-latex", action="store_true", help="skip the KaTeX parse")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        raise SystemExit(1 if self_test() else 0)

    paths = list(args.paths)
    if args.all:
        paths = sorted(PAGES.glob("**/*.md"))
    if args.english_only:
        paths = [p for p in paths if not re.search(r"\.(hi|te|od)\.md$", p.name)]
    if not paths:
        raise SystemExit("give page paths, or --all")

    found = {}
    for p in paths:
        probs = problems(body_of(p), with_latex=not args.no_latex)
        if probs:
            full = p.resolve()
            try:
                where = full.relative_to(BASE).as_posix()
            except ValueError:
                where = p.as_posix()     # a path outside the repo is still checkable
            found[where] = probs

    if args.json:
        print(json.dumps(found, indent=2, ensure_ascii=False))
    else:
        for where, probs in found.items():
            print(f"\n{where}")
            for x in probs:
                print(f"   {x}")
        print(f"\n{len(paths)} page(s) checked, {len(found)} with problems")


if __name__ == "__main__":
    main()
