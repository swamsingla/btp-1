'use client';
import { useEffect, useRef } from 'react';

export default function TopicContent({ html }) {
  const ref = useRef(null);

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

  return (
    <div
      ref={ref}
      className="prose max-w-none"
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
