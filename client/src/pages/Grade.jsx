import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { fetchGrade } from '../api';
import Breadcrumb from '../components/Breadcrumb';
import Loader from '../components/Loader';

function Grade() {
  const { gradeId } = useParams();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetchGrade(gradeId)
      .then(setData)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [gradeId]);

  if (loading) return <Loader />;
  if (!data) return <div className="error-state">Grade not found</div>;

  return (
    <div className="grade-page">
      <Breadcrumb items={[{ label: `Grade ${data.grade}` }]} />

      <div className="page-header">
        <div className="page-header-content">
          <div className="page-title-badge">{data.grade}</div>
          <div>
            <h1 className="page-title">Grade {data.grade}</h1>
            <p className="page-subtitle">
              {data.totalSubjects} subject{data.totalSubjects > 1 ? 's' : ''} • {data.totalChapters} chapters
            </p>
          </div>
        </div>
      </div>

      <div className="subjects-grid">
        {data.subjects.map(subject => (
          <Link
            to={`/grade/${data.grade}/${subject.key}`}
            className="subject-card"
            key={subject.key}
            style={{ '--subject-color': subject.color }}
          >
            <div className="subject-card-header">
              <span className="subject-card-icon">{subject.icon}</span>
              <span className="subject-card-count">{subject.totalChapters} chapters</span>
            </div>
            <h2 className="subject-card-title">{subject.name}</h2>
            <div className="subject-card-chapters">
              {subject.chapters.slice(0, 8).map(ch => (
                <span className="ch-pill" key={ch.number}>Ch {ch.number}</span>
              ))}
              {subject.chapters.length > 8 && (
                <span className="ch-pill ch-pill-more">+{subject.chapters.length - 8}</span>
              )}
            </div>
            {subject.hasParts && (
              <div className="subject-card-parts">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                Multiple Parts
              </div>
            )}
            <div className="subject-card-arrow">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Grade;
