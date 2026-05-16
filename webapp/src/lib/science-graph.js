import { readFileSync } from 'fs';
import { join } from 'path';

let _cache = null;

export function getScienceGraph() {
  if (_cache) return _cache;
  const filePath = join(process.cwd(), 'public', 'science.json');
  const raw = readFileSync(filePath, 'utf-8');
  _cache = JSON.parse(raw);
  return _cache;
}

export function getScienceGrades() {
  const graph = getScienceGraph();
  const grades = new Set();
  for (const concept of Object.values(graph.concepts)) {
    for (const g of concept.grades) grades.add(g);
  }
  return [...grades].sort((a, b) => a - b);
}

export function getScienceConceptsForGrade(grade) {
  const graph = getScienceGraph();
  return Object.values(graph.concepts).filter(c => c.grades.includes(grade));
}

export function getScienceConcept(slug) {
  const graph = getScienceGraph();
  return graph.concepts[slug] || null;
}

export function getScienceAreaGroups(grade) {
  const concepts = getScienceConceptsForGrade(grade);
  const groups = {};
  for (const c of concepts) {
    const area = c.area || 'General';
    if (!groups[area]) groups[area] = [];
    groups[area].push(c);
  }
  return groups;
}

export function getAllScienceAreas() {
  const graph = getScienceGraph();
  const areas = new Set();
  for (const c of Object.values(graph.concepts)) {
    areas.add(c.area || 'General');
  }
  return [...areas].sort();
}

export function getScienceEntryPoints(grade) {
  const gradeConcepts = getScienceConceptsForGrade(grade);
  const gradeSlugSet = new Set(gradeConcepts.map(c => c.slug));
  return gradeConcepts.filter(c => {
    const prereqs = c.prerequisites || [];
    return prereqs.length === 0 || !prereqs.some(p => gradeSlugSet.has(p));
  });
}

export function searchScienceConcepts(query, limit = 20) {
  if (!query || query.length < 2) return [];
  const graph = getScienceGraph();
  const q = query.toLowerCase().trim();
  const scored = [];

  for (const concept of Object.values(graph.concepts)) {
    let score = 0;
    const name  = (concept.canonical_name || '').toLowerCase();
    const desc  = (concept.description   || '').toLowerCase();
    const area  = (concept.area          || '').toLowerCase();

    if (name === q)            score += 100;
    else if (name.startsWith(q)) score += 80;
    else if (name.includes(q))   score += 60;
    else if (area.includes(q))   score += 30;
    else if (desc.includes(q))   score += 20;

    if (score === 0) {
      const words = q.split(/\s+/);
      const matchCount = words.filter(w => name.includes(w) || desc.includes(w) || area.includes(w)).length;
      if (matchCount > 0) score += matchCount * 15;
    }

    if (score > 0) scored.push({ concept, score });
  }

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, limit).map(s => s.concept);
}

// ── Science area colour palette ────────────────────────────────────────────
export const SCIENCE_AREA_COLORS = {
  // Physics
  'Mechanics':                { bg: 'bg-blue-50',     border: 'border-blue-200',     text: 'text-blue-700',     badge: 'bg-blue-100 text-blue-700',     dot: '#3b82f6' },
  'Fluid Mechanics':          { bg: 'bg-sky-50',      border: 'border-sky-200',      text: 'text-sky-700',      badge: 'bg-sky-100 text-sky-700',      dot: '#0ea5e9' },
  'Gravitation':              { bg: 'bg-indigo-50',   border: 'border-indigo-200',   text: 'text-indigo-700',   badge: 'bg-indigo-100 text-indigo-700',   dot: '#6366f1' },
  'Heat and Thermodynamics':  { bg: 'bg-orange-50',   border: 'border-orange-200',   text: 'text-orange-700',   badge: 'bg-orange-100 text-orange-700',   dot: '#f97316' },
  'Waves and Sound':          { bg: 'bg-cyan-50',     border: 'border-cyan-200',     text: 'text-cyan-700',     badge: 'bg-cyan-100 text-cyan-700',     dot: '#06b6d4' },
  'Optics':                   { bg: 'bg-yellow-50',   border: 'border-yellow-200',   text: 'text-yellow-700',   badge: 'bg-yellow-100 text-yellow-700',   dot: '#eab308' },
  'Electricity and Magnetism':{ bg: 'bg-violet-50',   border: 'border-violet-200',   text: 'text-violet-700',   badge: 'bg-violet-100 text-violet-700',   dot: '#8b5cf6' },
  'Modern Physics':           { bg: 'bg-purple-50',   border: 'border-purple-200',   text: 'text-purple-700',   badge: 'bg-purple-100 text-purple-700',   dot: '#a855f7' },
  'Oscillations':             { bg: 'bg-teal-50',     border: 'border-teal-200',     text: 'text-teal-700',     badge: 'bg-teal-100 text-teal-700',     dot: '#14b8a6' },
  'Units and Measurement':    { bg: 'bg-slate-50',    border: 'border-slate-200',    text: 'text-slate-700',    badge: 'bg-slate-100 text-slate-700',    dot: '#64748b' },
  // Chemistry
  'Matter and Classification':{ bg: 'bg-emerald-50',  border: 'border-emerald-200',  text: 'text-emerald-700',  badge: 'bg-emerald-100 text-emerald-700',  dot: '#10b981' },
  'Atomic Structure':         { bg: 'bg-lime-50',     border: 'border-lime-200',     text: 'text-lime-700',     badge: 'bg-lime-100 text-lime-700',     dot: '#84cc16' },
  'Periodic Classification':  { bg: 'bg-green-50',    border: 'border-green-200',    text: 'text-green-700',    badge: 'bg-green-100 text-green-700',    dot: '#22c55e' },
  'Chemical Bonding':         { bg: 'bg-amber-50',    border: 'border-amber-200',    text: 'text-amber-700',    badge: 'bg-amber-100 text-amber-700',    dot: '#f59e0b' },
  'Chemical Reactions':       { bg: 'bg-rose-50',     border: 'border-rose-200',     text: 'text-rose-700',     badge: 'bg-rose-100 text-rose-700',     dot: '#f43f5e' },
  'Acids Bases and Salts':    { bg: 'bg-red-50',      border: 'border-red-200',      text: 'text-red-700',      badge: 'bg-red-100 text-red-700',      dot: '#ef4444' },
  'Organic Chemistry':        { bg: 'bg-fuchsia-50',  border: 'border-fuchsia-200',  text: 'text-fuchsia-700',  badge: 'bg-fuchsia-100 text-fuchsia-700',  dot: '#d946ef' },
  'Thermochemistry':          { bg: 'bg-orange-50',   border: 'border-orange-200',   text: 'text-orange-700',   badge: 'bg-orange-100 text-orange-700',   dot: '#fb923c' },
  'Chemical Kinetics':        { bg: 'bg-pink-50',     border: 'border-pink-200',     text: 'text-pink-700',     badge: 'bg-pink-100 text-pink-700',     dot: '#ec4899' },
  'Electrochemistry':         { bg: 'bg-violet-50',   border: 'border-violet-200',   text: 'text-violet-700',   badge: 'bg-violet-100 text-violet-700',   dot: '#7c3aed' },
  'Solutions':                { bg: 'bg-sky-50',      border: 'border-sky-200',      text: 'text-sky-700',      badge: 'bg-sky-100 text-sky-700',      dot: '#38bdf8' },
  'Solid State':              { bg: 'bg-stone-50',    border: 'border-stone-200',    text: 'text-stone-700',    badge: 'bg-stone-100 text-stone-700',    dot: '#78716c' },
  'Surface Chemistry':        { bg: 'bg-yellow-50',   border: 'border-yellow-200',   text: 'text-yellow-700',   badge: 'bg-yellow-100 text-yellow-700',   dot: '#ca8a04' },
  'Environmental Chemistry':  { bg: 'bg-green-50',    border: 'border-green-200',    text: 'text-green-700',    badge: 'bg-green-100 text-green-700',    dot: '#16a34a' },
  // Biology
  'Cell Biology':             { bg: 'bg-teal-50',     border: 'border-teal-200',     text: 'text-teal-700',     badge: 'bg-teal-100 text-teal-700',     dot: '#0d9488' },
  'Diversity of Life':        { bg: 'bg-emerald-50',  border: 'border-emerald-200',  text: 'text-emerald-700',  badge: 'bg-emerald-100 text-emerald-700',  dot: '#059669' },
  'Plant Biology':            { bg: 'bg-lime-50',     border: 'border-lime-200',     text: 'text-lime-700',     badge: 'bg-lime-100 text-lime-700',     dot: '#65a30d' },
  'Human Physiology':         { bg: 'bg-rose-50',     border: 'border-rose-200',     text: 'text-rose-700',     badge: 'bg-rose-100 text-rose-700',     dot: '#e11d48' },
  'Nutrition and Digestion':  { bg: 'bg-amber-50',    border: 'border-amber-200',    text: 'text-amber-700',    badge: 'bg-amber-100 text-amber-700',    dot: '#d97706' },
  'Health and Disease':       { bg: 'bg-red-50',      border: 'border-red-200',      text: 'text-red-700',      badge: 'bg-red-100 text-red-700',      dot: '#dc2626' },
  'Genetics and Evolution':   { bg: 'bg-purple-50',   border: 'border-purple-200',   text: 'text-purple-700',   badge: 'bg-purple-100 text-purple-700',   dot: '#9333ea' },
  'Reproduction':             { bg: 'bg-pink-50',     border: 'border-pink-200',     text: 'text-pink-700',     badge: 'bg-pink-100 text-pink-700',     dot: '#db2777' },
  'Ecology':                  { bg: 'bg-green-50',    border: 'border-green-200',    text: 'text-green-700',    badge: 'bg-green-100 text-green-700',    dot: '#15803d' },
  'Biomolecules':             { bg: 'bg-cyan-50',     border: 'border-cyan-200',     text: 'text-cyan-700',     badge: 'bg-cyan-100 text-cyan-700',     dot: '#0891b2' },
  'Biotechnology':            { bg: 'bg-indigo-50',   border: 'border-indigo-200',   text: 'text-indigo-700',   badge: 'bg-indigo-100 text-indigo-700',   dot: '#4f46e5' },
};

export const SCIENCE_DEFAULT_COLOR = { bg: 'bg-gray-50', border: 'border-gray-200', text: 'text-gray-700', badge: 'bg-gray-100 text-gray-700', dot: '#6b7280' };

export function scienceAreaColor(area) {
  return SCIENCE_AREA_COLORS[area] || SCIENCE_DEFAULT_COLOR;
}
