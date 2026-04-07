import React, { createContext, useState, useContext, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import SearchModal from './components/SearchModal';
import Home from './pages/Home';
import Grade from './pages/Grade';
import Subject from './pages/Subject';
import Chapter from './pages/Chapter';
import NotFound from './pages/NotFound';

// ── Global Context ─────────────────────────────────────────
export const AppContext = createContext();

export function useApp() {
  return useContext(AppContext);
}

const LANGUAGES = {
  en: 'English',
  hi: 'हिन्दी',
  te: 'తెలుగు',
  or: 'ଓଡ଼ିଆ',
};

function App() {
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') || 'light');
  const [lang, setLang] = useState(() => localStorage.getItem('lang') || 'en');
  const [searchOpen, setSearchOpen] = useState(false);

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  useEffect(() => {
    localStorage.setItem('lang', lang);
  }, [lang]);

  // Keyboard shortcut: Ctrl+K to open search
  useEffect(() => {
    const handler = (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        setSearchOpen(true);
      }
      if (e.key === 'Escape') {
        setSearchOpen(false);
      }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, []);

  const toggleTheme = () => setTheme(t => (t === 'light' ? 'dark' : 'light'));

  const ctx = {
    theme, toggleTheme,
    lang, setLang,
    languages: LANGUAGES,
    searchOpen, setSearchOpen,
  };

  return (
    <AppContext.Provider value={ctx}>
      <Router>
        <div className="app">
          <Navbar />
          <SearchModal />
          <main className="main">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/grade/:gradeId" element={<Grade />} />
              <Route path="/grade/:gradeId/:subject" element={<Subject />} />
              <Route path="/grade/:gradeId/:subject/chapter/:chapterId" element={<Chapter />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </AppContext.Provider>
  );
}

export default App;
