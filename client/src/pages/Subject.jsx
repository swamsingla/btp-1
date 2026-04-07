import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { fetchSubject } from '../api';
import Breadcrumb from '../components/Breadcrumb';
import Loader from '../components/Loader';

function Subject() {
  const { gradeId, subject: subjectKey } = useParams();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetchSubject(gradeId, subjectKey)
      .then(setData)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [gradeId, subjectKey]);

  if (loading) return <Loader />;
  if (!data) return <div className="error-state">Subject not found</div>;

  const { subject } = data;
  let currentPart = null;

  return (
    <div className="subject-page">
      <Breadcrumb items={[
        { label: `Grade ${gradeId}`, href: `/grade/${gradeId}` },
        { label: subject.name },
      ]} />

      <div className="page-header">
        <div className="page-header-content">
          <span className="page-header-icon">{subject.icon}</span>
          <div>
            <h1 className="page-title">{subject.name}</h1>
            <p className="page-subtitle">Grade {gradeId} • {subject.totalChapters} Chapters</p>
          </div>
        </div>
      </div>

      <div className="chapters-list">
        {subject.chapters.map((ch, i) => {
          let partHeader = null;
          if (ch.part && ch.part !== currentPart) {
            currentPart = ch.part;
            partHeader = (
              <div className="part-divider" key={`part-${ch.part}`}>
                <span className="part-label">{ch.part}</span>
              </div>
            );
          }

          return (
            <React.Fragment key={ch.number}>
              {partHeader}
              <Link
                to={`/grade/${gradeId}/${subjectKey}/chapter/${ch.number}`}
                className="chapter-row"
              >
                <div className="chapter-row-num">
                  <span>{ch.number}</span>
                </div>
                <div className="chapter-row-body">
                  <h3 className="chapter-row-title">Chapter {ch.number}</h3>
                  <p className="chapter-row-meta">
                    {ch.part && `${ch.part} • `}{subject.name} • Grade {gradeId}
                  </p>
                </div>
                <div className="chapter-row-badge">
                  <span className="status-badge pending">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                    Pending
                  </span>
                </div>
                <svg className="chapter-row-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
              </Link>
            </React.Fragment>
          );
        })}
      </div>

      <div className="back-nav">
        <Link to={`/grade/${gradeId}`} className="btn btn-secondary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="15 18 9 12 15 6"/></svg>
          Back to Grade {gradeId}
        </Link>
      </div>
    </div>
  );
}

export default Subject;
