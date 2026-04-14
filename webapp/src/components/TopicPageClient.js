'use client';
import { useState } from 'react';
import TopicContent from './TopicContent';
import LanguageSwitch from './LanguageSwitch';

export default function TopicPageClient({ topic, translations }) {
  const availableLangs = ['en', ...Object.keys(translations || {})];
  const [lang, setLang] = useState('en');

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
      <TopicContent html={content} key={lang} />
    </>
  );
}
