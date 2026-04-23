'use client';
import { useState } from 'react';
import TopicContent from './TopicContent';
import LanguageSwitch from './LanguageSwitch';

export default function TopicPageClient({ topic, translations, initialLang }) {
  const availableLangs = ['en', ...Object.keys(translations || {})];

  // Use initial language from URL ?lang= parameter (passed from server)
  const startLang = initialLang && availableLangs.includes(initialLang) ? initialLang : 'en';
  const [lang, setLang] = useState(startLang);

  const content = lang === 'en'
    ? topic.content
    : translations[lang]?.content || topic.content;

  return (
    <>
      {availableLangs.length > 1 && (
        <div className="flex justify-end mb-4">
          <LanguageSwitch
            currentLang={lang}
            availableLangs={availableLangs}
            onChange={setLang}
          />
        </div>
      )}
      <TopicContent html={content} lang={lang} key={lang} />
    </>
  );
}
