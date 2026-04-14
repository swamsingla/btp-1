'use client';
import Link from 'next/link';
import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'next/navigation';
import { useTheme } from './ThemeProvider';

export default function Navbar() {
  const [searchOpen, setSearchOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [gradeFilter, setGradeFilter] = useState('');
  const [subjectFilter, setSubjectFilter] = useState('');
  const [chapterFilter, setChapterFilter] = useState('');
  const inputRef = useRef(null);
  const router = useRouter();
  const debounceRef = useRef(null);
  const { theme, toggle } = useTheme();

  useEffect(() => {
    const handler = (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        setSearchOpen(true);
      }
      if (e.key === 'Escape') setSearchOpen(false);
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, []);

  useEffect(() => {
    if (searchOpen && inputRef.current) inputRef.current.focus();
  }, [searchOpen]);

  useEffect(() => {
    if (!query.trim() || query.length < 2) { setResults([]); return; }
    clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(async () => {
      setLoading(true);
      try {
        const params = new URLSearchParams({ q: query });
        if (gradeFilter) params.set('grade', gradeFilter);
        if (subjectFilter) params.set('subject', subjectFilter);
        if (chapterFilter) params.set('chapter', chapterFilter);
        const res = await fetch(`/api/search?${params}`);
        const data = await res.json();
        setResults(data.results || []);
      } catch { setResults([]); }
      setLoading(false);
    }, 300);
  }, [query, gradeFilter, subjectFilter, chapterFilter]);

  const goTo = (r) => {
    setSearchOpen(false);
    setQuery('');
    if (r.topicId) {
      router.push(`/grade/${r.grade}/${r.subject}/chapter/${r.chapter}/topic/${r.topicId}`);
    } else {
      router.push(`/grade/${r.grade}/${r.subject}/chapter/${r.chapter}`);
    }
  };

  return (
    <>
      <nav className="sticky top-0 z-50 bg-white/80 dark:bg-gray-900/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-2 text-xl font-bold text-blue-600 dark:text-blue-400">
            <span className="text-2xl">📚</span> NCERT Learn
          </Link>
          <div className="flex items-center gap-3">
            <button
              onClick={() => setSearchOpen(true)}
              className="flex items-center gap-2 px-3 py-1.5 bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-lg text-sm text-gray-500 dark:text-gray-400 transition-colors"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              Search
              <kbd className="hidden sm:inline-block ml-2 px-1.5 py-0.5 bg-white dark:bg-gray-700 rounded text-xs border dark:border-gray-600">⌘K</kbd>
            </button>
            <button
              onClick={toggle}
              className="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 text-gray-500 dark:text-gray-400 transition-colors"
              aria-label="Toggle dark mode"
            >
              {theme === 'dark' ? (
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
              ) : (
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
              )}
            </button>
          </div>
        </div>
      </nav>

      {searchOpen && (
        <div className="fixed inset-0 z-[100] bg-black/50 flex items-start justify-center pt-[10vh]" onClick={() => setSearchOpen(false)}>
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-2xl w-full max-w-xl mx-4 overflow-hidden" onClick={e => e.stopPropagation()}>
            <div className="flex items-center px-4 border-b dark:border-gray-700">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#9ca3af" strokeWidth="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input
                ref={inputRef}
                value={query}
                onChange={e => setQuery(e.target.value)}
                placeholder="Search topics, chapters..."
                className="flex-1 px-3 py-4 text-base outline-none bg-transparent dark:text-gray-100"
              />
              <button onClick={() => setSearchOpen(false)} className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 text-sm">ESC</button>
            </div>
            <div className="flex items-center gap-2 px-4 py-2 border-b dark:border-gray-700 bg-gray-50 dark:bg-gray-750">
              <select value={gradeFilter} onChange={e => setGradeFilter(e.target.value)} className="text-xs px-2 py-1 rounded-md border border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-300 outline-none">
                <option value="">All Grades</option>
                {[6,7,8,9,10,11,12].map(g => <option key={g} value={g}>Grade {g}</option>)}
              </select>
              <select value={subjectFilter} onChange={e => setSubjectFilter(e.target.value)} className="text-xs px-2 py-1 rounded-md border border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-300 outline-none">
                <option value="">All Subjects</option>
                <option value="maths">Mathematics</option>
                <option value="science">Science</option>
              </select>
              <select value={chapterFilter} onChange={e => setChapterFilter(e.target.value)} className="text-xs px-2 py-1 rounded-md border border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-300 outline-none">
                <option value="">All Chapters</option>
                {[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15].map(c => <option key={c} value={c}>Ch {c}</option>)}
              </select>
            </div>
            <div className="max-h-80 overflow-y-auto">
              {loading && <div className="p-4 text-center text-gray-400">Searching...</div>}
              {!loading && query.length >= 2 && results.length === 0 && (
                <div className="p-4 text-center text-gray-400">No results found</div>
              )}
              {results.map((r, i) => (
                <button key={i} onClick={() => goTo(r)} className="w-full text-left px-4 py-3 hover:bg-blue-50 dark:hover:bg-gray-700 flex items-start gap-3 border-b border-gray-100 dark:border-gray-700 transition-colors">
                  <span className="text-lg mt-0.5">{r.subjectIcon || '📖'}</span>
                  <div className="flex-1 min-w-0">
                    <div className="font-medium text-sm text-gray-900 dark:text-gray-100 truncate">
                      {r.topicTitle || r.chapterTitle}
                    </div>
                    <div className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                      Grade {r.grade} · {r.subjectName} · Chapter {r.chapter}
                    </div>
                    {r.snippet && <div className="text-xs text-gray-400 dark:text-gray-500 mt-1 line-clamp-2">{r.snippet}</div>}
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}
    </>
  );
}
