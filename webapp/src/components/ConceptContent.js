'use client';
import { useEffect, useRef } from 'react';

/**
 * Renders a generated concept page and typesets its maths.
 *
 * The HTML is built on the server (lib/markdown.js); this component exists only to run
 * KaTeX over it once it is in the DOM. KaTeX and its auto-render extension are loaded
 * from a CDN in layout.js, so both may be absent — offline, or if the CDN is blocked —
 * and the page must still read correctly with `$…$` showing as plain text.
 */
export default function ConceptContent({ html }) {
  const ref = useRef(null);

  useEffect(() => {
    const el = ref.current;
    if (!el || typeof window === 'undefined' || !window.renderMathInElement) return;
    try {
      window.renderMathInElement(el, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
        ],
        // A malformed formula should show as text, not replace the page with an error.
        throwOnError: false,
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
      });
    } catch {
      /* leave the source text visible */
    }
  }, [html]);

  return <div ref={ref} dangerouslySetInnerHTML={{ __html: html }} />;
}
