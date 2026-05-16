import { useState, useEffect, useRef, useCallback, useMemo } from 'react';
import ForceGraph2D from 'react-force-graph-2d';
import './App.css';

// ── Colour palette ─────────────────────────────────────────────────────────
function hslToHex(h, s, l) {
  h /= 360; s /= 100; l /= 100;
  let r, g, b;
  if (s === 0) { r = g = b = l; }
  else {
    const hue2rgb = (p, q, t) => {
      if (t < 0) t += 1; if (t > 1) t -= 1;
      if (t < 1/6) return p + (q - p) * 6 * t;
      if (t < 1/2) return q;
      if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
      return p;
    };
    const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
    const p = 2 * l - q;
    r = hue2rgb(p, q, h + 1/3);
    g = hue2rgb(p, q, h);
    b = hue2rgb(p, q, h - 1/3);
  }
  return `#${Math.round(r*255).toString(16).padStart(2,'0')}${Math.round(g*255).toString(16).padStart(2,'0')}${Math.round(b*255).toString(16).padStart(2,'0')}`;
}

function buildPalette(areas) {
  return Object.fromEntries(areas.map((a, i) => {
    const h = (i * 360 / areas.length + 10) % 360;
    const s = (h > 30 && h < 70) ? 72 : 80;
    const l = (h > 30 && h < 70) ? 62 : 58;
    return [a, hslToHex(h, s, l)];
  }));
}

// ── Graph data transform ───────────────────────────────────────────────────
function buildGraphData(raw, activeGrades, activeAreas) {
  const concepts = raw.concepts;
  const palette = buildPalette([...new Set(Object.values(concepts).map(c => c.area))].sort());

  // Degree count for node size
  const degree = {};
  for (const e of raw.edges) {
    degree[e.from] = (degree[e.from] || 0) + 1;
    degree[e.to]   = (degree[e.to]   || 0) + 1;
  }

  const nodeIds = new Set(
    Object.keys(concepts).filter(id => {
      const c = concepts[id];
      return activeAreas.has(c.area) && c.grades.some(g => activeGrades.has(g));
    })
  );

  const nodes = [...nodeIds].map(id => {
    const c = concepts[id];
    return {
      id,
      label: c.canonical_name,
      area: c.area,
      grades: c.grades,
      description: c.description || '',
      prerequisites: c.prerequisites || [],
      leads_to: c.leads_to || [],
      color: palette[c.area] || '#818cf8',
      val: 1 + Math.min((degree[id] || 0) * 0.4, 4),
    };
  });

  const links = raw.edges
    .filter(e => nodeIds.has(e.from) && nodeIds.has(e.to))
    .map(e => ({ source: e.from, target: e.to }));

  return { nodes, links, palette };
}

// ── Detail Panel ───────────────────────────────────────────────────────────
function DetailPanel({ node, allNodes, onClose, onNavigate }) {
  if (!node) return null;
  const lookup = id => allNodes.find(n => n.id === id);
  return (
    <div className="detail-panel open">
      <div className="detail-header">
        <div className="detail-title">{node.label}</div>
        <button className="detail-close" onClick={onClose}>✕</button>
      </div>
      <div className="detail-body">
        <div className="detail-meta">
          <span className="badge area" style={{ borderColor: node.color, color: node.color }}>{node.area}</span>
          {node.grades.map(g => <span key={g} className="badge">Grade {g}</span>)}
        </div>
        {node.description && <p className="detail-desc">{node.description}</p>}

        {node.prerequisites.length > 0 && (
          <div className="rel-section">
            <h4>Prerequisites</h4>
            <div className="rel-chips">
              {node.prerequisites.map(id => {
                const n = lookup(id);
                return (
                  <span key={id} className="rel-chip" onClick={() => n && onNavigate(n)}>
                    {n ? n.label : id}
                  </span>
                );
              })}
            </div>
          </div>
        )}

        {node.leads_to.length > 0 && (
          <div className="rel-section">
            <h4>Leads To</h4>
            <div className="rel-chips">
              {node.leads_to.map(id => {
                const n = lookup(id);
                return (
                  <span key={id} className="rel-chip" onClick={() => n && onNavigate(n)}>
                    {n ? n.label : id}
                  </span>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

// ── Main App ───────────────────────────────────────────────────────────────
const SUBJECTS = [
  { key: 'maths',   label: 'Mathematics', file: '/maths.json',   icon: '∑',  accent: '#818cf8' },
  { key: 'science', label: 'Science',     file: '/science.json', icon: '⚛', accent: '#34d399' },
];

const ALL_GRADES = [6, 7, 8, 9, 10, 11, 12];

export default function App() {
  const [subjectKey, setSubjectKey] = useState('maths');
  const [rawData, setRawData]       = useState(null);
  const [loading, setLoading]       = useState(true);
  const [activeGrades, setActiveGrades] = useState(new Set(ALL_GRADES));
  const [activeAreas,  setActiveAreas]  = useState(new Set());
  const [search,   setSearch]   = useState('');
  const [selected, setSelected] = useState(null);
  const [dims, setDims]         = useState({ w: window.innerWidth, h: window.innerHeight });

  const fgRef = useRef();
  const subject = SUBJECTS.find(s => s.key === subjectKey);

  // Window resize
  useEffect(() => {
    const onResize = () => setDims({ w: window.innerWidth, h: window.innerHeight });
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);

  // Load data when subject changes
  useEffect(() => {
    setLoading(true);
    setSelected(null);
    setSearch('');
    fetch(subject.file)
      .then(r => r.json())
      .then(data => {
        const areas = [...new Set(Object.values(data.concepts).map(c => c.area))].sort();
        setActiveAreas(new Set(areas));
        setActiveGrades(new Set(ALL_GRADES));
        setRawData(data);
        setLoading(false);
      });
  }, [subjectKey]);

  // Build graph data
  const { nodes, links, palette } = useMemo(() => {
    if (!rawData) return { nodes: [], links: [], palette: {} };
    return buildGraphData(rawData, activeGrades, activeAreas);
  }, [rawData, activeGrades, activeAreas]);

  // Search highlight
  const graphData = useMemo(() => {
    const q = search.trim().toLowerCase();
    return {
      nodes: nodes.map(n => ({
        ...n,
        __dimmed: q && !n.label.toLowerCase().includes(q),
      })),
      links,
    };
  }, [nodes, links, search]);

  // Node painting
  const paintNode = useCallback((node, ctx, globalScale) => {
    const r = Math.sqrt(node.val) * 4;
    const dimmed = node.__dimmed;
    ctx.globalAlpha = dimmed ? 0.08 : 1;
    ctx.beginPath();
    ctx.arc(node.x, node.y, r, 0, 2 * Math.PI);
    ctx.fillStyle = node.color;
    ctx.fill();

    // Label at zoom > 2
    if (globalScale > 2 && !dimmed) {
      ctx.globalAlpha = 1;
      const fontSize = Math.max(8, 11 / globalScale * 1.6);
      ctx.font = `${fontSize}px Inter`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillStyle = '#e2e8f0';
      ctx.fillText(node.label, node.x, node.y + r + 2);
    }

    // Always show label for selected
    if (node.id === selected?.id) {
      ctx.globalAlpha = 1;
      const fontSize = Math.max(10, 12 / globalScale * 1.6);
      ctx.font = `600 ${fontSize}px Inter`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillStyle = '#ffffff';
      ctx.fillText(node.label, node.x, node.y + r + 2);
      // ring
      ctx.beginPath();
      ctx.arc(node.x, node.y, r + 3, 0, 2 * Math.PI);
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1.5 / globalScale;
      ctx.stroke();
    }

    ctx.globalAlpha = 1;
  }, [selected]);

  const linkColor = useCallback(link => {
    const sId = typeof link.source === 'object' ? link.source.id : link.source;
    const tId = typeof link.target === 'object' ? link.target.id : link.target;
    const q = search.trim().toLowerCase();
    if (q) {
      const sn = nodes.find(n => n.id === sId);
      const tn = nodes.find(n => n.id === tId);
      if (sn?.__dimmed || tn?.__dimmed) return 'rgba(45,63,85,0.15)';
    }
    return 'rgba(45,63,85,0.75)';
  }, [search, nodes]);

  const handleNodeClick = useCallback(node => {
    setSelected(node);
    fgRef.current?.centerAt(node.x, node.y, 600);
    fgRef.current?.zoom(3, 600);
  }, []);

  const areas = useMemo(() => palette ? Object.keys(palette) : [], [palette]);

  const toggleGrade = g => {
    setActiveGrades(prev => {
      const next = new Set(prev);
      if (next.has(g)) { if (next.size > 1) next.delete(g); }
      else next.add(g);
      return next;
    });
  };

  const toggleArea = a => {
    setActiveAreas(prev => {
      const next = new Set(prev);
      if (next.has(a)) { if (next.size > 1) next.delete(a); }
      else next.add(a);
      return next;
    });
  };

  const SIDEBAR_W = 272;
  const TOPBAR_H  = 56;

  return (
    <div className="app">
      {/* ── TOPBAR ── */}
      <div className="topbar">
        <div className="subject-tabs">
          {SUBJECTS.map(s => (
            <button
              key={s.key}
              className={`subj-tab ${subjectKey === s.key ? 'active' : ''}`}
              style={subjectKey === s.key ? { '--accent': s.accent } : {}}
              onClick={() => { setSubjectKey(s.key); }}
            >
              <span className="subj-icon">{s.icon}</span> {s.label}
            </button>
          ))}
        </div>
        <div className="stats">
          {rawData && <>
            <span className="stat-pill"><b>{rawData.total_concepts}</b> concepts</span>
            <span className="stat-pill"><b>{rawData.total_edges}</b> edges</span>
            <span className="stat-pill"><b>{areas.length}</b> areas</span>
          </>}
        </div>
        <div className="spacer" />
        <div className="search-wrap">
          <span className="search-icon">🔍</span>
          <input
            className="search-input"
            type="text"
            placeholder="Search concepts…"
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
        </div>
        <button className="reset-btn" onClick={() => {
          setActiveGrades(new Set(ALL_GRADES));
          setActiveAreas(new Set(Object.keys(palette)));
          setSearch('');
          setSelected(null);
          fgRef.current?.zoomToFit(600, 40);
        }}>Reset</button>
      </div>

      {/* ── SIDEBAR ── */}
      <div className="sidebar">
        <div className="sidebar-section">
          <h3 className="sidebar-heading">Filter by Grade</h3>
          <div className="grade-chips">
            {ALL_GRADES.map(g => (
              <span
                key={g}
                className={`grade-chip ${activeGrades.has(g) ? 'active' : ''}`}
                onClick={() => toggleGrade(g)}
              >Grade {g}</span>
            ))}
          </div>
        </div>
        <div className="sidebar-section flex1">
          <h3 className="sidebar-heading">Subject Areas</h3>
          <div className="legend">
            {areas.map(a => (
              <div
                key={a}
                className={`legend-row ${activeAreas.has(a) ? 'active' : ''}`}
                onClick={() => toggleArea(a)}
              >
                <span className="ldot" style={{ background: palette[a] }} />
                <span className="lname">{a}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* ── CANVAS ── */}
      <div className="canvas-wrap">
        {loading && (
          <div className="loading-overlay">
            <div className="spinner" style={{ '--accent': subject.accent }} />
            <h2>{subject.icon} Loading {subject.label}…</h2>
          </div>
        )}
        {!loading && (
          <ForceGraph2D
            ref={fgRef}
            width={dims.w - SIDEBAR_W}
            height={dims.h - TOPBAR_H}
            graphData={graphData}
            nodeCanvasObject={paintNode}
            nodeCanvasObjectMode={() => 'replace'}
            linkColor={linkColor}
            linkWidth={1.2}
            linkDirectionalArrowLength={4}
            linkDirectionalArrowRelPos={1}
            linkDirectionalArrowColor={() => 'rgba(100,120,160,0.6)'}
            linkCurvature={0.1}
            onNodeClick={handleNodeClick}
            backgroundColor="#0b1120"
            cooldownTicks={200}
            onEngineStop={() => fgRef.current?.zoomToFit(400, 40)}
            nodeLabel={node => node.label}
          />
        )}
      </div>

      {/* ── DETAIL PANEL ── */}
      <DetailPanel
        node={selected}
        allNodes={nodes}
        onClose={() => setSelected(null)}
        onNavigate={n => handleNodeClick(n)}
      />
    </div>
  );
}
