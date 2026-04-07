import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import { useApp } from '../App';
import { fetchContent, fetchSubject } from '../api';
import Breadcrumb from '../components/Breadcrumb';
import Loader from '../components/Loader';

function Chapter() {
  const { gradeId, subject: subjectKey, chapterId } = useParams();
  const { lang, setLang, languages } = useApp();
  const [content, setContent] = useState(null);
  const [subjectData, setSubjectData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [activeTopic, setActiveTopic] = useState(1);
  const contentRef = useRef(null);

  useEffect(() => {
    setLoading(true);
    Promise.all([
      fetchContent(gradeId, subjectKey, chapterId, lang),
      fetchSubject(gradeId, subjectKey),
    ])
      .then(([contentData, subjData]) => {
        setContent(contentData);
        setSubjectData(subjData);
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [gradeId, subjectKey, chapterId, lang]);

  // Render KaTeX after content loads
  useEffect(() => {
    if (content && contentRef.current && window.renderMathInElement) {
      window.renderMathInElement(contentRef.current, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\(', right: '\\)', display: false },
          { left: '\\[', right: '\\]', display: true },
        ],
        throwOnError: false,
      });
    }
  }, [content]);

  // Intersection observer for active topic tracking
  useEffect(() => {
    if (!content) return;
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = parseInt(entry.target.dataset.topicId, 10);
            if (id) setActiveTopic(id);
          }
        });
      },
      { rootMargin: '-20% 0px -60% 0px' }
    );

    document.querySelectorAll('.topic-section').forEach(el => observer.observe(el));
    return () => observer.disconnect();
  }, [content]);

  if (loading) return <Loader />;
  if (!content) return <div className="error-state">Chapter not found</div>;

  const chapters = subjectData?.subject?.chapters || [];
  const currentIndex = chapters.findIndex(c => c.number === parseInt(chapterId));
  const prevChapter = currentIndex > 0 ? chapters[currentIndex - 1] : null;
  const nextChapter = currentIndex < chapters.length - 1 ? chapters[currentIndex + 1] : null;
  const subjectName = subjectData?.subject?.name || subjectKey;
  const subjectIcon = subjectData?.subject?.icon || '📖';

  return (
    <div className="chapter-page">
      <Breadcrumb items={[
        { label: `Grade ${gradeId}`, href: `/grade/${gradeId}` },
        { label: subjectName, href: `/grade/${gradeId}/${subjectKey}` },
        { label: content.title },
      ]} />

      <div className="chapter-layout">
        {/* ── Sidebar ──────────────────────────────────── */}
        <aside className={`chapter-sidebar ${sidebarOpen ? 'open' : ''}`}>
          <div className="sidebar-header">
            <h3>Contents</h3>
            <button className="sidebar-close" onClick={() => setSidebarOpen(false)}>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>

          {/* Chapter list */}
          <div className="sidebar-section">
            <label className="sidebar-label">Chapters</label>
            <div className="sidebar-ch-list">
              {chapters.map(ch => (
                <Link
                  key={ch.number}
                  to={`/grade/${gradeId}/${subjectKey}/chapter/${ch.number}`}
                  className={`sidebar-ch-link ${ch.number === parseInt(chapterId) ? 'active' : ''}`}
                >
                  <span className="sidebar-ch-num">{ch.number}</span>
                  Chapter {ch.number}
                </Link>
              ))}
            </div>
          </div>

          {/* Topic list */}
          <div className="sidebar-section">
            <label className="sidebar-label">Topics</label>
            <div className="sidebar-topic-list">
              {content.topics.map(topic => (
                <a
                  key={topic.id}
                  href={`#topic-${topic.id}`}
                  className={`sidebar-topic-link ${activeTopic === topic.id ? 'active' : ''}`}
                  onClick={() => setSidebarOpen(false)}
                >
                  <span className="sidebar-topic-num">{topic.id}</span>
                  {topic.title}
                </a>
              ))}
            </div>
          </div>
        </aside>

        {/* ── Main Content ─────────────────────────────── */}
        <div className="chapter-main" ref={contentRef}>
          {/* Chapter header */}
          <div className="chapter-header">
            <div className="chapter-header-top">
              <div className="chapter-meta">
                <span className="meta-tag">{subjectIcon} {subjectName}</span>
                <span className="meta-tag">Grade {gradeId}</span>
                {content.chapterMeta?.part && <span className="meta-tag">{content.chapterMeta.part}</span>}
                {content.status === 'pending' && <span className="meta-tag meta-tag-warn">⏳ Pipeline Pending</span>}
              </div>
              <div className="chapter-lang-switch">
                {Object.entries(languages).map(([code, name]) => (
                  <button
                    key={code}
                    className={`lang-pill ${code === lang ? 'active' : ''}`}
                    onClick={() => setLang(code)}
                  >
                    {name}
                  </button>
                ))}
              </div>
            </div>
            <h1 className="chapter-title">{content.title}</h1>
            {content.summary && (
              <div className="chapter-summary">
                <p>{content.summary}</p>
              </div>
            )}
          </div>

          {/* Mobile TOC toggle */}
          <button className="sidebar-toggle" onClick={() => setSidebarOpen(true)}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
            Table of Contents
          </button>

          {/* Topics */}
          <div className="topics-list">
            {content.topics.map(topic => (
              <section
                key={topic.id}
                className="topic-section"
                id={`topic-${topic.id}`}
                data-topic-id={topic.id}
              >
                <div className="topic-header">
                  <span className="topic-num">{topic.id}</span>
                  <h2 className="topic-title">{topic.title}</h2>
                </div>
                <div
                  className="topic-content prose"
                  dangerouslySetInnerHTML={{ __html: topic.content }}
                />
                {topic.subtopics && topic.subtopics.length > 0 && (
                  <div className="subtopics">
                    {topic.subtopics.map((sub, i) => (
                      <div key={i} className="subtopic">
                        <h3 className="subtopic-title">{sub.title}</h3>
                        <div
                          className="subtopic-content prose"
                          dangerouslySetInnerHTML={{ __html: sub.content }}
                        />
                      </div>
                    ))}
                  </div>
                )}
              </section>
            ))}
          </div>

          {/* Chapter Navigation */}
          <div className="chapter-nav">
            {prevChapter ? (
              <Link to={`/grade/${gradeId}/${subjectKey}/chapter/${prevChapter.number}`} className="chapter-nav-btn prev">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="15 18 9 12 15 6"/></svg>
                <div>
                  <span className="chapter-nav-label">Previous</span>
                  <span className="chapter-nav-name">Chapter {prevChapter.number}</span>
                </div>
              </Link>
            ) : <div />}
            {nextChapter ? (
              <Link to={`/grade/${gradeId}/${subjectKey}/chapter/${nextChapter.number}`} className="chapter-nav-btn next">
                <div>
                  <span className="chapter-nav-label">Next</span>
                  <span className="chapter-nav-name">Chapter {nextChapter.number}</span>
                </div>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
              </Link>
            ) : <div />}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Chapter;
