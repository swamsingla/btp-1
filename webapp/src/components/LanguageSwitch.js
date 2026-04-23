'use client';
import { useState } from 'react';

const LANGUAGES = {
  en: { name: 'English', flag: '🇬🇧' },
  hi: { name: 'Hindi', flag: '🇮🇳' },
  te: { name: 'Telugu', flag: '🇮🇳' },
  od: { name: 'Odia', flag: '🇮🇳' },
};

export default function LanguageSwitch({ currentLang, availableLangs, onChange }) {
  const [open, setOpen] = useState(false);

  if (!availableLangs || availableLangs.length <= 1) return null;

  const current = LANGUAGES[currentLang] || LANGUAGES.en;

  return (
    <div className="relative">
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-2 px-3 py-1.5 bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-lg text-sm transition-colors"
      >
        <span>{current.flag}</span>
        <span className="font-medium">{current.name}</span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <polyline points="6 9 12 15 18 9" />
        </svg>
      </button>
      {open && (
        <div className="absolute right-0 mt-1 bg-white dark:bg-gray-800 rounded-lg shadow-lg border dark:border-gray-700 py-1 min-w-[140px] z-50">
          {availableLangs.map(lang => {
            const info = LANGUAGES[lang] || { name: lang, flag: '🌐' };
            return (
              <button
                key={lang}
                onClick={() => { onChange(lang); setOpen(false); }}
                className={`w-full text-left px-3 py-2 text-sm hover:bg-gray-100 dark:hover:bg-gray-700 flex items-center gap-2 ${
                  lang === currentLang ? 'font-semibold text-blue-600 dark:text-blue-400' : ''
                }`}
              >
                <span>{info.flag}</span> {info.name}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}
