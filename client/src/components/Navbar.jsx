import React, { useState, useRef, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useApp } from '../App';

function Navbar() {
  const { theme, toggleTheme, lang, setLang, languages, setSearchOpen } = useApp();
  const [langOpen, setLangOpen] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const langRef = useRef(null);
  const location = useLocation();

  // Close mobile menu on navigation
  useEffect(() => { setMobileOpen(false); }, [location]);

  // Close lang dropdown on outside click
  useEffect(() => {
    const handler = (e) => {
      if (langRef.current && !langRef.current.contains(e.target)) setLangOpen(false);
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  return (
    <nav className="navbar">
      <div className="navbar-inner">
        {/* Brand */}
        <Link to="/" className="navbar-brand">
          <span className="navbar-logo">📚</span>
          <div className="navbar-title">
            <span className="navbar-title-main">NCERT Smart Wiki</span>
            <span className="navbar-title-sub">Multilingual Knowledge Hub</span>
          </div>
        </Link>

        {/* Desktop Actions */}
        <div className={`navbar-actions ${mobileOpen ? 'open' : ''}`}>
          {/* Search */}
          <button className="navbar-btn search-btn" onClick={() => setSearchOpen(true)} title="Search (Ctrl+K)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <span className="search-label">Search</span>
            <kbd className="search-kbd">⌘K</kbd>
          </button>

          {/* Language */}
          <div className="lang-selector" ref={langRef}>
            <button className="navbar-btn lang-btn" onClick={() => setLangOpen(!langOpen)}>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
              <span>{languages[lang]}</span>
            </button>
            {langOpen && (
              <div className="lang-dropdown">
                {Object.entries(languages).map(([code, name]) => (
                  <button
                    key={code}
                    className={`lang-option ${code === lang ? 'active' : ''}`}
                    onClick={() => { setLang(code); setLangOpen(false); }}
                  >
                    <span className="lang-name">{name}</span>
                    <span className="lang-code">{code.toUpperCase()}</span>
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Theme */}
          <button className="navbar-btn theme-btn" onClick={toggleTheme} title="Toggle theme">
            {theme === 'light' ? (
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
            ) : (
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
            )}
          </button>
        </div>

        {/* Mobile hamburger */}
        <button className="navbar-hamburger" onClick={() => setMobileOpen(!mobileOpen)}>
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>
  );
}

export default Navbar;
