import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useApp } from '../App';
import { fetchCatalog } from '../api';
import Loader from '../components/Loader';

const GRADE_GROUPS = [
  { label: 'Middle School', range: [6, 7, 8], emoji: '🏫' },
  { label: 'Secondary', range: [9, 10], emoji: '🎓' },
  { label: 'Senior Secondary', range: [11, 12], emoji: '🎯' },
];

function Home() {
  const [catalog, setCatalog] = useState(null);
  const [loading, setLoading] = useState(true);
  const { setSearchOpen } = useApp();

  useEffect(() => {
    fetchCatalog()
      .then(setCatalog)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Loader />;
  if (!catalog) return <div className="error-state">Failed to load catalog</div>;

  const { grades, summary } = catalog;

  return (
    <div className="home-page">
      {/* ── Hero ──────────────────────────────────────────── */}
      <section className="hero">
        <div className="hero-bg">
          <div className="hero-shape hero-shape-1"></div>
          <div className="hero-shape hero-shape-2"></div>
          <div className="hero-shape hero-shape-3"></div>
        </div>
        <div className="hero-content">
          <div className="hero-badge">📚 NCERT Curriculum Aligned</div>
          <h1 className="hero-title">
            NCERT Multilingual<br />
            <span className="hero-highlight">Smart Wiki</span>
          </h1>
          <p className="hero-subtitle">
            A structured digital knowledge platform for students in grades 6–12.
            Explore NCERT textbooks in <strong>English</strong>, <strong>हिन्दी</strong>, <strong>తెలుగు</strong> &amp; <strong>ଓଡ଼ିଆ</strong>.
          </p>
          <div className="hero-actions">
            <a href="#grades" className="btn btn-primary btn-lg">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
              Start Exploring
            </a>
            <button className="btn btn-glass btn-lg" onClick={() => setSearchOpen(true)}>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              Search Topics
            </button>
          </div>
        </div>

        {/* Stats */}
        <div className="hero-stats">
          <div className="stat-card">
            <span className="stat-number">{summary.totalGrades}</span>
            <span className="stat-label">Grades</span>
          </div>
          <div className="stat-card">
            <span className="stat-number">{summary.totalSubjects}</span>
            <span className="stat-label">Subjects</span>
          </div>
          <div className="stat-card">
            <span className="stat-number">{summary.totalChapters}</span>
            <span className="stat-label">Chapters</span>
          </div>
          <div className="stat-card">
            <span className="stat-number">4</span>
            <span className="stat-label">Languages</span>
          </div>
        </div>
      </section>

      {/* ── Features ─────────────────────────────────────── */}
      <section className="features">
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">🌐</div>
            <h3>Multilingual</h3>
            <p>Content in English, Hindi, Telugu &amp; Odia with seamless language switching</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">📐</div>
            <h3>Math Support</h3>
            <p>Beautiful LaTeX/KaTeX rendering for complex formulas and equations</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🎯</div>
            <h3>Curriculum Aligned</h3>
            <p>Strictly follows NCERT with Grade → Subject → Chapter → Topic hierarchy</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Instant Access</h3>
            <p>Pre-generated content served instantly — zero latency, zero hallucinations</p>
          </div>
        </div>
      </section>

      {/* ── Grade Selection ──────────────────────────────── */}
      <section className="grades-section" id="grades">
        <div className="section-header">
          <h2 className="section-title">Select Your Grade</h2>
          <p className="section-subtitle">Choose a grade to explore subjects and chapters</p>
        </div>

        {GRADE_GROUPS.map(group => {
          const groupGrades = grades.filter(g => group.range.includes(g.grade));
          if (groupGrades.length === 0) return null;

          return (
            <div className="grade-group" key={group.label}>
              <h3 className="grade-group-title">
                <span>{group.emoji}</span> {group.label}
              </h3>
              <div className="grades-grid">
                {groupGrades.map(g => (
                  <Link to={`/grade/${g.grade}`} className="grade-card" key={g.grade}>
                    <div className="grade-card-num">{g.grade}</div>
                    <div className="grade-card-body">
                      <span className="grade-card-title">Grade {g.grade}</span>
                      <span className="grade-card-meta">
                        {g.totalSubjects} subject{g.totalSubjects > 1 ? 's' : ''} • {g.totalChapters} chapters
                      </span>
                      <div className="grade-card-subjects">
                        {g.subjects.map(s => (
                          <span className="subject-pill" key={s.key}>{s.icon} {s.name}</span>
                        ))}
                      </div>
                    </div>
                    <svg className="grade-card-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
                  </Link>
                ))}
              </div>
            </div>
          );
        })}
      </section>
    </div>
  );
}

export default Home;
