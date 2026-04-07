import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { useApp } from '../App';
import { searchContent } from '../api';

function SearchModal() {
  const { searchOpen, setSearchOpen, lang } = useApp();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selected, setSelected] = useState(0);
  const inputRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (searchOpen && inputRef.current) {
      inputRef.current.focus();
      setQuery('');
      setResults([]);
      setSelected(0);
    }
  }, [searchOpen]);

  // Debounced search
  useEffect(() => {
    if (!query || query.length < 2) {
      setResults([]);
      return;
    }
    const timer = setTimeout(async () => {
      setLoading(true);
      try {
        const data = await searchContent(query, lang);
        setResults(data.results || []);
        setSelected(0);
      } catch {
        setResults([]);
      }
      setLoading(false);
    }, 300);
    return () => clearTimeout(timer);
  }, [query, lang]);

  const handleKeyDown = useCallback((e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelected(s => Math.min(s + 1, results.length - 1));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelected(s => Math.max(s - 1, 0));
    } else if (e.key === 'Enter' && results[selected]) {
      const r = results[selected];
      navigate(`/grade/${r.grade}/${r.subject}/chapter/${r.chapter}`);
      setSearchOpen(false);
    }
  }, [results, selected, navigate, setSearchOpen]);

  if (!searchOpen) return null;

  return (
    <div className="search-overlay" onClick={() => setSearchOpen(false)}>
      <div className="search-modal" onClick={(e) => e.stopPropagation()}>
        <div className="search-input-wrap">
          <svg className="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
          </svg>
          <input
            ref={inputRef}
            type="text"
            className="search-input"
            placeholder="Search chapters, topics, concepts..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button className="search-close" onClick={() => setSearchOpen(false)}>
            <kbd>ESC</kbd>
          </button>
        </div>

        <div className="search-results">
          {loading && (
            <div className="search-loading">
              <div className="spinner"></div>
              <span>Searching...</span>
            </div>
          )}
          {!loading && query.length >= 2 && results.length === 0 && (
            <div className="search-empty">
              <p>No results found for "<strong>{query}</strong>"</p>
            </div>
          )}
          {!loading && results.map((r, i) => (
            <button
              key={`${r.grade}-${r.subject}-${r.chapter}-${i}`}
              className={`search-result ${i === selected ? 'selected' : ''}`}
              onClick={() => {
                navigate(`/grade/${r.grade}/${r.subject}/chapter/${r.chapter}`);
                setSearchOpen(false);
              }}
              onMouseEnter={() => setSelected(i)}
            >
              <span className="search-result-icon">{r.subjectIcon}</span>
              <div className="search-result-body">
                <span className="search-result-title">{r.title}</span>
                <span className="search-result-meta">
                  Grade {r.grade} • {r.subjectName}
                  {r.topic && ` • ${r.topic}`}
                </span>
                {r.snippet && <span className="search-result-snippet">{r.snippet.substring(0, 120)}...</span>}
              </div>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
            </button>
          ))}
          {!query && (
            <div className="search-hints">
              <p className="search-hint-title">Quick Search</p>
              <div className="search-hint-items">
                <span>Try: "chapter", "physics", "biology"</span>
              </div>
              <p className="search-hint-keys">
                <kbd>↑↓</kbd> Navigate &nbsp; <kbd>↵</kbd> Open &nbsp; <kbd>ESC</kbd> Close
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default SearchModal;
