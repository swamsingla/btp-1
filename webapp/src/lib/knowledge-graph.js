import { readFileSync } from 'fs';
import { join } from 'path';

let _cache = null;

export function getGraph() {
  if (_cache) return _cache;
  const filePath = join(process.cwd(), 'public', 'maths_v2.json');
  const raw = readFileSync(filePath, 'utf-8');
  _cache = JSON.parse(raw);
  return _cache;
}

/** All grades that appear in the graph */
export function getGrades() {
  const graph = getGraph();
  const grades = new Set();
  for (const concept of Object.values(graph.concepts)) {
    for (const g of concept.grades) grades.add(g);
  }
  return [...grades].sort((a, b) => a - b);
}

/** All concepts for a given grade */
export function getConceptsForGrade(grade) {
  const graph = getGraph();
  return Object.values(graph.concepts).filter(c => c.grades.includes(grade));
}

/** Single concept by slug (grade-agnostic) */
export function getConcept(slug) {
  const graph = getGraph();
  return graph.concepts[slug] || null;
}

/** Concepts grouped by area for a grade */
export function getAreaGroups(grade) {
  const concepts = getConceptsForGrade(grade);
  const groups = {};
  for (const c of concepts) {
    const area = c.area || 'General';
    if (!groups[area]) groups[area] = [];
    groups[area].push(c);
  }
  return groups;
}

/** All unique areas across the entire graph */
export function getAllAreas() {
  const graph = getGraph();
  const areas = new Set();
  for (const c of Object.values(graph.concepts)) {
    areas.add(c.area || 'General');
  }
  return [...areas].sort();
}

/** Concepts in a specific area (all grades) */
export function getConceptsByArea(area) {
  const graph = getGraph();
  return Object.values(graph.concepts).filter(c => (c.area || 'General') === area);
}

/** Resolve related concept slugs to full concept objects */
export function getRelatedConcepts(slug) {
  const concept = getConcept(slug);
  if (!concept) return [];
  const related = concept.related || [];
  return related.map(s => getConcept(s)).filter(Boolean);
}

/** Entry points: concepts with no in-graph prerequisites for a given grade */
export function getEntryPoints(grade) {
  const gradeConcepts = getConceptsForGrade(grade);
  const gradeSlugSet = new Set(gradeConcepts.map(c => c.slug));
  return gradeConcepts.filter(c => {
    const prereqs = c.prerequisites || [];
    return prereqs.length === 0 || !prereqs.some(p => gradeSlugSet.has(p));
  });
}

/** Search concepts by query string — fuzzy match on name, description, area */
export function searchConcepts(query, limit = 20) {
  if (!query || query.length < 2) return [];
  const graph = getGraph();
  const q = query.toLowerCase().trim();
  const scored = [];

  for (const concept of Object.values(graph.concepts)) {
    let score = 0;
    const name = (concept.canonical_name || '').toLowerCase();
    const desc = (concept.description || '').toLowerCase();
    const area = (concept.area || '').toLowerCase();
    const aliases = (concept.aliases || []).map(a => a.toLowerCase());

    // Exact name match
    if (name === q) score += 100;
    // Name starts with query
    else if (name.startsWith(q)) score += 80;
    // Name contains query
    else if (name.includes(q)) score += 60;
    // Alias match
    else if (aliases.some(a => a.includes(q))) score += 50;
    // Area match
    else if (area.includes(q)) score += 30;
    // Description match
    else if (desc.includes(q)) score += 20;

    // Word-level matching for multi-word queries
    if (score === 0) {
      const words = q.split(/\s+/);
      const matchCount = words.filter(w => name.includes(w) || desc.includes(w) || area.includes(w)).length;
      if (matchCount > 0) score += matchCount * 15;
    }

    if (score > 0) {
      scored.push({ concept, score });
    }
  }

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, limit).map(s => s.concept);
}

/** Colour palette per area */
export const AREA_COLORS = {
  'Number Systems':        { bg: 'bg-blue-50',   border: 'border-blue-200',   text: 'text-blue-700',   badge: 'bg-blue-100 text-blue-700',   dot: '#3b82f6' },
  'Number Theory':         { bg: 'bg-violet-50',  border: 'border-violet-200', text: 'text-violet-700', badge: 'bg-violet-100 text-violet-700', dot: '#8b5cf6' },
  'Algebra':               { bg: 'bg-emerald-50', border: 'border-emerald-200',text: 'text-emerald-700',badge: 'bg-emerald-100 text-emerald-700', dot: '#10b981' },
  'Geometry':              { bg: 'bg-orange-50',  border: 'border-orange-200', text: 'text-orange-700', badge: 'bg-orange-100 text-orange-700', dot: '#f97316' },
  'Mensuration':           { bg: 'bg-yellow-50',  border: 'border-yellow-200', text: 'text-yellow-700', badge: 'bg-yellow-100 text-yellow-700', dot: '#eab308' },
  'Trigonometry':          { bg: 'bg-pink-50',    border: 'border-pink-200',   text: 'text-pink-700',   badge: 'bg-pink-100 text-pink-700',   dot: '#ec4899' },
  'Statistics':            { bg: 'bg-cyan-50',    border: 'border-cyan-200',   text: 'text-cyan-700',   badge: 'bg-cyan-100 text-cyan-700',   dot: '#06b6d4' },
  'Probability':           { bg: 'bg-teal-50',    border: 'border-teal-200',   text: 'text-teal-700',   badge: 'bg-teal-100 text-teal-700',   dot: '#14b8a6' },
  'Calculus':              { bg: 'bg-red-50',     border: 'border-red-200',    text: 'text-red-700',    badge: 'bg-red-100 text-red-700',     dot: '#ef4444' },
  'Linear Algebra':        { bg: 'bg-indigo-50',  border: 'border-indigo-200', text: 'text-indigo-700', badge: 'bg-indigo-100 text-indigo-700', dot: '#6366f1' },
  'Vectors':               { bg: 'bg-purple-50',  border: 'border-purple-200', text: 'text-purple-700', badge: 'bg-purple-100 text-purple-700', dot: '#a855f7' },
  'Set Theory':            { bg: 'bg-lime-50',    border: 'border-lime-200',   text: 'text-lime-700',   badge: 'bg-lime-100 text-lime-700',   dot: '#84cc16' },
  'Combinatorics':         { bg: 'bg-amber-50',   border: 'border-amber-200',  text: 'text-amber-700',  badge: 'bg-amber-100 text-amber-700', dot: '#f59e0b' },
  'Coordinate Geometry':   { bg: 'bg-sky-50',     border: 'border-sky-200',    text: 'text-sky-700',    badge: 'bg-sky-100 text-sky-700',     dot: '#0ea5e9' },
  'Sequences':             { bg: 'bg-rose-50',    border: 'border-rose-200',   text: 'text-rose-700',   badge: 'bg-rose-100 text-rose-700',   dot: '#f43f5e' },
  'Patterns and Sequences':{ bg: 'bg-rose-50',    border: 'border-rose-200',   text: 'text-rose-700',   badge: 'bg-rose-100 text-rose-700',   dot: '#f43f5e' },
  'Proportional Reasoning':{ bg: 'bg-fuchsia-50', border: 'border-fuchsia-200',text: 'text-fuchsia-700',badge: 'bg-fuchsia-100 text-fuchsia-700', dot: '#d946ef' },
  'Optimisation':          { bg: 'bg-stone-50',   border: 'border-stone-200',  text: 'text-stone-700',  badge: 'bg-stone-100 text-stone-700', dot: '#78716c' },
  'Three-dimensional Geometry': { bg: 'bg-sky-50', border: 'border-sky-200', text: 'text-sky-700', badge: 'bg-sky-100 text-sky-700', dot: '#0ea5e9' },
  'Relations and Functions': { bg: 'bg-emerald-50', border: 'border-emerald-200', text: 'text-emerald-700', badge: 'bg-emerald-100 text-emerald-700', dot: '#10b981' },
  'Mathematical Reasoning': { bg: 'bg-amber-50', border: 'border-amber-200', text: 'text-amber-700', badge: 'bg-amber-100 text-amber-700', dot: '#f59e0b' },
};

export const DEFAULT_COLOR = { bg: 'bg-gray-50', border: 'border-gray-200', text: 'text-gray-700', badge: 'bg-gray-100 text-gray-700', dot: '#6b7280' };

export function areaColor(area) {
  return AREA_COLORS[area] || DEFAULT_COLOR;
}
