/**
 * Minimal Markdown → HTML for generated concept pages.
 *
 * Deliberately small rather than a dependency: these pages come from one generator
 * with a fixed shape (h1, h2 sections, paragraphs, bullets, bold, and LaTeX), so the
 * subset is known and stable.
 *
 * It walks LINES, not blank-line-separated blocks. A model writes
 *
 *     ## Key points
 *     *   A number is divisible by 10 if ...
 *
 * with no blank line between heading and list, and a block-based reader turns that
 * whole thing into one paragraph with literal "##" and "*" in it. Nobody reviews 900
 * pages by hand, so the renderer has to cope with ordinary formatting variation.
 *
 * Maths is passed through untouched — `$…$` and `$$…$$` reach the browser as text and
 * KaTeX's auto-render (loaded in layout.js) turns them into equations. HTML is escaped
 * first, which is safe for KaTeX because it reads text content, where the entities have
 * already decoded back to the original characters.
 */

import katex from 'katex';

const escapeHtml = (s) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

/**
 * Typeset one formula to HTML, here on the server.
 *
 * This used to be left to KaTeX's auto-render in the browser, loaded from a CDN. That
 * meant every page shipped its maths as raw "$\frac{1}{2}$" text — 541 such spans on the
 * Fractions page alone — and whether a reader ever saw an equation depended on the CDN
 * answering AND on the one useEffect that calls renderMathInElement finding the global
 * already defined, with no retry if it did not. Rendering here puts real markup in the
 * HTML instead, so the maths is there before any script runs and does not depend on the
 * network at all.
 *
 * A formula that will not parse is returned as its own source text rather than throwing,
 * because one bad expression must not blank the page.
 */
/** Drop the `$$` fences from a display block before the expression is typeset. */
const stripDollars = (s) => s.trim().replace(/^\$\$/, '').replace(/\$\$$/, '');

function tex(expr, displayMode) {
  try {
    return katex.renderToString(expr.trim(), {
      displayMode,
      throwOnError: false,
      strict: false,
      output: 'html',
    });
  } catch {
    return escapeHtml(expr);
  }
}

const HEADING = /^(#{1,4})\s+(.*)$/;
const BULLET = /^\s*([-*•]|\d+[.)])\s+(.*)$/;

const HEADING_CLASS = {
  1: 'text-3xl font-bold mt-10 mb-4',
  2: 'text-2xl font-bold mt-8 mb-3',
  3: 'text-xl font-semibold mt-6 mb-2',
  4: 'text-lg font-semibold mt-4 mb-2',
};

/**
 * Bold, italic and inline maths. Anything heavier belongs in the generator, not here.
 *
 * The text is split on `$…$` first so that each part is handled by the right rule: prose
 * is escaped and marked up, a formula is typeset. Escaping the whole line first would turn
 * a backslash-heavy expression into entities before KaTeX ever saw it, and running the
 * bold rule over a formula would eat the asterisks in something like $2 * 3$.
 */
function inline(text) {
  const markup = (s) => escapeHtml(s)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*\n]+)\*/g, '$1<em>$2</em>');

  const parts = text.split(/(\$[^$\n]+\$)/g);
  return parts
    .map((part) => (part.startsWith('$') && part.endsWith('$') && part.length > 2
      ? tex(part.slice(1, -1), false)
      : markup(part)))
    .join('');
}

export function renderMarkdown(markdown, { skipFirstHeading = true } = {}) {
  // Put a complete `$$ … $$` on a line of its own before walking lines. The generator
  // often writes the equation and then keeps going on the SAME line:
  //
  //     $$ 90 = 3 \times 3 \times 2 \times 5 $$ The number 90 could also be ...
  //
  // The walker below decides a block is unterminated when the line does not END with
  // `$$`, so it started collecting maths and never stopped: every remaining line of the
  // page was swallowed into the equation and emitted as escaped text, which is why the
  // Prime Factorisation page showed literal "##" headings and "*" bullets from its first
  // equation onwards. Splitting the line first keeps the equation whole and lets the
  // trailing prose be an ordinary paragraph.
  const normalised = markdown
    .replace(/\r\n/g, '\n')
    .replace(/(\$\$[^\n$](?:[^\n$]|\$(?!\$))*\$\$)/g, '\n$1\n');
  const lines = normalised.split('\n');
  const html = [];
  let para = [];          // lines of the paragraph being collected
  let list = null;        // { ordered, items } while inside a list
  let math = null;        // lines of a $$ … $$ block
  let droppedHeading = false;

  const flushPara = () => {
    if (para.length) {
      html.push(`<p class="my-4 leading-7 text-gray-700 dark:text-gray-300">` +
        `${inline(para.join(' '))}</p>`);
      para = [];
    }
  };
  const flushList = () => {
    if (list) {
      const tag = list.ordered ? 'ol' : 'ul';
      const style = list.ordered ? 'list-decimal' : 'list-disc';
      html.push(`<${tag} class="${style} pl-6 my-4 text-gray-700 dark:text-gray-300">` +
        list.items.map((i) => `<li class="mb-1.5">${inline(i)}</li>`).join('') +
        `</${tag}>`);
      list = null;
    }
  };
  const flush = () => { flushPara(); flushList(); };

  for (const raw of lines) {
    const line = raw.trimEnd();

    // Display maths spans several lines and must be kept whole, delimiters included.
    if (math !== null) {
      // A real display block never contains a blank line, so a blank line means the
      // opening `$$` was never closed. Give up on it here: an unterminated delimiter then
      // costs one odd-looking paragraph instead of every heading and bullet that follows.
      if (!line.trim()) {
        para.push(...math.map((l) => l.trim()));
        math = null;
        flush();
        continue;
      }
      math.push(line);
      if (line.trim().endsWith('$$') && math.length > 1) {
        html.push(`<div class="my-6 overflow-x-auto text-center">` +
          `${tex(stripDollars(math.join('\n')), true)}</div>`);
        math = null;
      }
      continue;
    }
    if (line.trim().startsWith('$$')) {
      flush();
      const body = line.trim();
      // a one-line $$ … $$ closes immediately; an opening delimiter alone does not
      if (body.length > 2 && body.endsWith('$$')) {
        html.push(`<div class="my-6 overflow-x-auto text-center">${tex(stripDollars(body), true)}</div>`);
      } else {
        math = [line];
      }
      continue;
    }

    if (!line.trim()) { flush(); continue; }

    const heading = line.match(HEADING);
    if (heading) {
      flush();
      const level = heading[1].length;
      // The page already shows the concept name as its title, so the document's own
      // opening h1 would just repeat it.
      if (level === 1 && skipFirstHeading && !droppedHeading) {
        droppedHeading = true;
        continue;
      }
      html.push(`<h${level} class="${HEADING_CLASS[level]} text-gray-900 ` +
        `dark:text-gray-100">${inline(heading[2])}</h${level}>`);
      continue;
    }

    const bullet = line.match(BULLET);
    if (bullet) {
      flushPara();
      const ordered = /\d/.test(bullet[1]);
      if (!list || list.ordered !== ordered) { flushList(); list = { ordered, items: [] }; }
      list.items.push(bullet[2]);
      continue;
    }

    // A plain line while a list is open is that item continuing onto a second line.
    if (list) { list.items[list.items.length - 1] += ' ' + line.trim(); continue; }
    para.push(line.trim());
  }

  if (math) html.push(`<div class="my-6 overflow-x-auto text-center">` +
    `${tex(stripDollars(math.join('\n')), true)}</div>`);
  flush();
  return html.join('\n');
}
