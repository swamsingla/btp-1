import Link from 'next/link';
import { getGraph, getGrades, getConceptsForGrade, getEntryPoints, getAllAreas, areaColor } from '@/lib/knowledge-graph';

const GRADE_META = {
  6:  { tier: 'Middle School',    emoji: '📚', color: 'from-sky-500 to-blue-600' },
  7:  { tier: 'Middle School',    emoji: '📚', color: 'from-blue-500 to-indigo-600' },
  8:  { tier: 'Middle School',    emoji: '📚', color: 'from-indigo-500 to-violet-600' },
  9:  { tier: 'Secondary',       emoji: '🎓', color: 'from-violet-500 to-purple-600' },
  10: { tier: 'Secondary',       emoji: '🎓', color: 'from-purple-500 to-fuchsia-600' },
  11: { tier: 'Senior Secondary', emoji: '🎯', color: 'from-fuchsia-500 to-pink-600' },
  12: { tier: 'Senior Secondary', emoji: '🎯', color: 'from-pink-500 to-rose-600' },
};

export default function Home() {
  const graph = getGraph();
  const grades = getGrades();
  const allAreas = getAllAreas();

  // Get entry-point concepts for Grade 6 as "Start Here" suggestions
  const starterConcepts = getEntryPoints(6).slice(0, 8);

  return (
    <div className="min-h-screen">
      {/* ═══ Hero ═══ */}
      <section className="relative bg-gradient-to-br from-blue-600 via-indigo-700 to-violet-800 text-white overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-10 left-10 w-80 h-80 bg-white rounded-full blur-3xl animate-float" />
          <div className="absolute bottom-10 right-10 w-96 h-96 bg-blue-300 rounded-full blur-3xl animate-float-delayed" />
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-violet-400 rounded-full blur-3xl opacity-50" />
        </div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-28 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-white/15 backdrop-blur-sm rounded-full text-sm font-medium mb-6 border border-white/20">
            <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
            Knowledge Graph — {graph.total_concepts} Concepts
          </div>
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight tracking-tight">
            NCERT Mathematics<br />
            <span className="bg-gradient-to-r from-blue-200 to-violet-200 bg-clip-text text-transparent">
              Knowledge Graph
            </span>
          </h1>
          <p className="text-lg md:text-xl text-blue-100 max-w-2xl mx-auto mb-10 leading-relaxed">
            Every concept linked to its prerequisites and successors.
            Navigate the full NCERT maths curriculum from Whole Numbers to Calculus
            — one concept at a time, like Wikipedia.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
            <Link href="/maths"
              className="inline-flex items-center justify-center gap-2 px-6 py-3 bg-white text-blue-700 font-semibold rounded-xl hover:bg-blue-50 transition-all shadow-lg hover:shadow-xl hover:-translate-y-0.5">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
              Explore All Grades
            </Link>
            <a href="#start-here"
              className="inline-flex items-center justify-center gap-2 px-6 py-3 bg-white/15 backdrop-blur text-white font-semibold rounded-xl hover:bg-white/25 transition-all border border-white/20">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              Start Learning
            </a>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-6 max-w-md mx-auto">
            <div className="text-center">
              <div className="text-3xl font-bold">{graph.total_concepts}</div>
              <div className="text-sm text-blue-200">Concepts</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold">{graph.total_edges}</div>
              <div className="text-sm text-blue-200">Connections</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold">{grades.length}</div>
              <div className="text-sm text-blue-200">Grades</div>
            </div>
          </div>
        </div>
      </section>

      {/* ═══ Features ═══ */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { icon: '🔗', title: 'Prerequisite Tracking', desc: 'Every concept shows what you need to know first — no gaps in your understanding' },
            { icon: '🗺️', title: 'Cross-Grade Navigation', desc: 'See how concepts evolve from Grade 6 to 12 — follow your learning journey across years' },
            { icon: '📐', title: 'Area-Based Organisation', desc: 'Concepts grouped by mathematical areas — Number Theory, Geometry, Algebra, and more' },
            { icon: '🔍', title: 'Wikipedia-Style Pages', desc: 'Each concept has its own page with linked prerequisites, related topics, and what it unlocks' },
          ].map((f, i) => (
            <div key={i} className="group bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-sm border border-gray-100 dark:border-gray-700 hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
              <div className="text-3xl mb-3 group-hover:scale-110 transition-transform duration-300">{f.icon}</div>
              <h3 className="font-semibold text-gray-900 dark:text-gray-100 mb-2">{f.title}</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ═══ Areas Overview ═══ */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12">
        <h2 className="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-4">
          {allAreas.length} Mathematical Areas
        </h2>
        <div className="flex flex-wrap gap-2">
          {allAreas.map(area => {
            const c = areaColor(area);
            return (
              <span key={area} className={`px-3 py-1.5 rounded-full text-xs font-medium ${c.badge} transition-all hover:scale-105 cursor-default`}>
                {area}
              </span>
            );
          })}
        </div>
      </section>

      {/* ═══ Grade Selection ═══ */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16" id="grades">
        <div className="text-center mb-10">
          <h2 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-gray-100">Choose Your Grade</h2>
          <p className="text-gray-500 dark:text-gray-400 mt-2">Select a grade to explore its concept map</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {grades.map(grade => {
            const concepts = getConceptsForGrade(grade);
            const areas = [...new Set(concepts.map(c => c.area || 'General'))];
            const meta = GRADE_META[grade] || { tier: '', emoji: '📖', color: 'from-gray-500 to-gray-700' };
            const entryPts = getEntryPoints(grade);

            return (
              <Link key={grade} href={`/maths/${grade}`}
                className="group relative bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden">
                <div className={`h-1.5 bg-gradient-to-r ${meta.color}`} />
                <div className="p-5">
                  <div className="flex items-start justify-between mb-3">
                    <div>
                      <h3 className="text-lg font-bold text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                        Grade {grade}
                      </h3>
                      <p className="text-xs text-gray-400">{meta.tier}</p>
                    </div>
                    <div className="text-2xl">{meta.emoji}</div>
                  </div>
                  <div className="flex items-center gap-4 text-sm text-gray-500 mb-3">
                    <span><span className="font-semibold text-gray-700 dark:text-gray-300">{concepts.length}</span> concepts</span>
                    <span><span className="font-semibold text-gray-700 dark:text-gray-300">{areas.length}</span> areas</span>
                  </div>
                  <div className="flex flex-wrap gap-1">
                    {areas.slice(0, 4).map(area => {
                      const c = areaColor(area);
                      return (
                        <span key={area} className={`px-2 py-0.5 rounded-full text-xs font-medium ${c.badge}`}>
                          {area.length > 15 ? area.split(' ').slice(0, 2).join(' ') : area}
                        </span>
                      );
                    })}
                    {areas.length > 4 && (
                      <span className="px-2 py-0.5 rounded-full text-xs font-medium bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400">
                        +{areas.length - 4}
                      </span>
                    )}
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </section>

      {/* ═══ Start Here ═══ */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20" id="start-here">
        <div className="text-center mb-8">
          <h2 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-gray-100">
            <span className="text-yellow-500">⭐</span> Start Here — Grade 6 Foundations
          </h2>
          <p className="text-gray-500 dark:text-gray-400 mt-2">
            These concepts have no prerequisites — the perfect starting point
          </p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {starterConcepts.map(concept => {
            const c = areaColor(concept.area);
            return (
              <Link key={concept.slug} href={`/maths/6/${concept.slug}`}
                className={`group bg-white dark:bg-gray-800 rounded-xl border ${c.border} p-4 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200`}>
                <div className="flex items-start justify-between mb-2">
                  <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${c.badge}`}>{concept.area}</span>
                  <span className="text-yellow-400 text-xs">⭐ Start</span>
                </div>
                <h3 className="font-semibold text-sm text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors leading-snug mb-1">
                  {concept.canonical_name}
                </h3>
                <p className="text-xs text-gray-500 dark:text-gray-400 line-clamp-2">{concept.description}</p>
                {(concept.leads_to || []).length > 0 && (
                  <div className="mt-2 text-xs text-gray-400">
                    Unlocks {concept.leads_to.length} concept{concept.leads_to.length !== 1 ? 's' : ''}  →
                  </div>
                )}
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}
