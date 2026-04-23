'use client';
import { useEffect, useRef } from 'react';
import { useRouter } from 'next/navigation';

export default function TopicContent({ html, lang }) {
  const ref = useRef(null);
  const router = useRouter();

  useEffect(() => {
    if (!ref.current) return;
    const tryRender = () => {
      if (window.renderMathInElement) {
        window.renderMathInElement(ref.current, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true },
          ],
          throwOnError: false,
        });
      } else {
        setTimeout(tryRender, 200);
      }
    };
    tryRender();
  }, [html]);

  useEffect(() => {
    if (!ref.current || !lang || lang === 'en') return;
    const handleClick = (e) => {
      const a = e.target.closest('a.related-link');
      if (!a) return;
      e.preventDefault();
      const href = a.getAttribute('href');
      const url = new URL(href, window.location.origin);
      url.searchParams.set('lang', lang);
      router.push(url.pathname + url.search);
    };
    ref.current.addEventListener('click', handleClick);
    return () => ref.current?.removeEventListener('click', handleClick);
  }, [lang, router]);

  return (
    <div
      ref={ref}
      className="prose max-w-none"
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
