import { readFileSync, existsSync, readdirSync } from 'fs';
import { join } from 'path';

/**
 * Generated page content lives outside the app, next to the pipeline that writes it:
 *   <repo>/data/generated_pages/<stream>/grade<N>/<slug>[.<lang>].md
 *
 * Routes are /maths/... and /science/..., but science pages are filed under the stream
 * the concept belongs to (physics, chemistry, biology), so a science slug has to be
 * looked for in each of them. English has no suffix; every other language does.
 */
const CONTENT_ROOT = join(process.cwd(), '..', 'data', 'generated_pages');
const STREAMS = { maths: ['maths'], science: ['physics', 'chemistry', 'biology', 'science'] };

/** Display names, in the language itself — a reader looking for Odia looks for ଓଡ଼ିଆ. */
export const LANGUAGES = {
  en: { label: 'English', native: 'English' },
  hi: { label: 'Hindi', native: 'हिन्दी' },
  te: { label: 'Telugu', native: 'తెలుగు' },
  od: { label: 'Odia', native: 'ଓଡ଼ିଆ' },
};

const fileFor = (slug, lang) => (lang && lang !== 'en' ? `${slug}.${lang}.md` : `${slug}.md`);

/** Parse the JSON front matter written by scripts/generate_pages.py. */
function splitFrontMatter(raw) {
  const match = raw.match(/^---\s*\n([\s\S]*?)\n---\s*\n?([\s\S]*)$/);
  if (!match) return { meta: null, body: raw.trim() };
  try {
    return { meta: JSON.parse(match[1]), body: match[2].trim() };
  } catch {
    // A page with unreadable front matter is still worth showing.
    return { meta: null, body: match[2].trim() };
  }
}

/**
 * The generated page for a concept in one language, or null when there isn't one.
 * Returning null is normal: only a fraction of the 900 concepts have pages so far.
 */
export function getGeneratedPage(subject, grade, slug, lang = 'en') {
  for (const stream of STREAMS[subject] ?? []) {
    const file = join(CONTENT_ROOT, stream, `grade${grade}`, fileFor(slug, lang));
    if (existsSync(file)) return splitFrontMatter(readFileSync(file, 'utf-8'));
  }
  return null;
}

/**
 * Which languages this concept has been generated in, in a stable display order.
 * The switcher offers only these, so it never links to a page that does not exist.
 */
export function getAvailableLanguages(subject, grade, slug) {
  const found = new Set();
  for (const stream of STREAMS[subject] ?? []) {
    const dir = join(CONTENT_ROOT, stream, `grade${grade}`);
    if (!existsSync(dir)) continue;
    for (const f of readdirSync(dir)) {
      if (f === `${slug}.md`) found.add('en');
      const m = f.match(new RegExp(`^${slug}\\.([a-z]{2})\\.md$`));
      if (m) found.add(m[1]);
    }
  }
  return Object.keys(LANGUAGES).filter((code) => found.has(code));
}

/** Slugs that have a generated page, for showing which concepts are ready. */
export function getGeneratedSlugs(subject, grade) {
  const found = new Set();
  for (const stream of STREAMS[subject] ?? []) {
    const dir = join(CONTENT_ROOT, stream, `grade${grade}`);
    if (!existsSync(dir)) continue;
    for (const f of readdirSync(dir)) {
      if (f.endsWith('.md')) found.add(f.replace(/(\.[a-z]{2})?\.md$/, ''));
    }
  }
  return found;
}
