import Link from 'next/link';
import { getGrades, getConceptsForGrade, getGraph, getEntryPoints, getAllAreas, areaColor } from '@/lib/knowledge-graph';

export const metadata = { title: 'Mathematics Knowledge Graph — NCERT Learn' };

const GRADE_LABELS = {
  6: { label: 'Grade 6', tier: 'Middle School', color: 'from-sky-500 to-blue-600' },
  7: { label: 'Grade 7', tier: 'Middle School', color: 'from-blue-500 to-indigo-600' },
  8: { label: 'Grade 8', tier: 'Middle School', color: 'from-indigo-500 to-violet-600' },
  9: { label: 'Grade 9', tier: 'Secondary', color: 'from-violet-500 to-purple-600' },
  10: { label: 'Grade 10', tier: 'Secondary', color: 'from-purple-500 to-fuchsia-600' },
  11: { label: 'Grade 11', tier: 'Senior Secondary', color: 'from-fuchsia-500 to-pink-600' },
  12: { label: 'Grade 12', tier: 'Senior Secondary', color: 'from-pink-500 to-rose-600' },
};

export default function MathsHome() {
  const graph = getGraph();
  const grades = getGrades();
  const allAreas = getAllAreas();

  return (
    <div className="min-h-screen">
      {/* Hero */}
      <section className="relative bg-gradient-to-br from-blue-600 via-indigo-700 to-violet-800 text-white overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-10 left-10 w-80 h-80 bg-white rounded-full blur-3xl" />
          <div className="absolute bottom-10 right-10 w-96 h-96 bg-blue-300 rounded-full blur-3xl" />
        </div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-white/15 backdrop-blur-sm rounded-full text-sm font-medium mb-6 border border-white/20">
            📐 Mathematics · Grades 6 – 12
          </div>
          <h1 className="text-4xl md:text-6xl font-extrabold mb-5 leading-tight">
            Maths Knowledge<br />
            <span className="bg-gradient-to-r from-blue-200 to-violet-200 bg-clip-text text-transparent">Graph</span>
          </h1>
          <p className="text-lg md:text-xl text-blue-100 max-w-2xl mx-auto mb-10 leading-relaxed">
            Every concept linked to its prerequisites. Navigate the full NCERT maths
            curriculum from Whole Numbers to Calculus — one step at a time.
          </p>
          {/* Stats */}
          <div className="grid grid-cols-3 gap-6 max-w-sm mx-auto">
            <div>
              <div className="text-3xl font-bold">{graph.total_concepts}</div>
              <div className="text-sm text-blue-200">Concepts</div>
            </div>
            <div>
              <div className="text-3xl font-bold">{graph.total_edges}</div>
              <div className="text-sm text-blue-200">Links</div>
            </div>
            <div>
              <div className="text-3xl font-bold">{allAreas.length}</div>
              <div className="text-sm text-blue-200">Areas</div>
            </div>
          </div>
        </div>
      </section>

      {/* Area legend */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h2 className="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-4">Topics by Area</h2>
        <div className="flex flex-wrap gap-2">
          {allAreas.map(area => {
            const c = areaColor(area);
            return (
              <span key={area} className={`px-3 py-1 rounded-full text-xs font-medium ${c.badge}`}>
                {area}
              </span>
            );
          })}
        </div>
      </section>

      {/* Grade Cards */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-6">Choose a Grade</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {grades.map(grade => {
            const concepts = getConceptsForGrade(grade);
            const areas = [...new Set(concepts.map(c => c.area || 'General'))];
            const entryPts = getEntryPoints(grade);
            const meta = GRADE_LABELS[grade] || { label: `Grade ${grade}`, tier: '', color: 'from-gray-500 to-gray-700' };

            return (
              <Link
                key={grade}
                href={`/maths/${grade}`}
                className="group relative bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 hover:shadow-lg hover:-translate-y-0.5 transition-all overflow-hidden"
              >
                {/* coloured top bar */}
                <div className={`h-1.5 bg-gradient-to-r ${meta.color}`} />
                <div className="p-5">
                  <div className="flex items-start justify-between mb-3">
                    <div>
                      <h3 className="text-lg font-bold text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                        {meta.label}
                      </h3>
                      <p className="text-xs text-gray-400">{meta.tier}</p>
                    </div>
                    <svg className="w-5 h-5 text-gray-300 group-hover:text-blue-400 transition-colors mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <polyline points="9 18 15 12 9 6" />
                    </svg>
                  </div>

                  <div className="flex items-center gap-4 text-sm text-gray-500 dark:text-gray-400 mb-3">
                    <span><span className="font-semibold text-gray-700 dark:text-gray-300">{concepts.length}</span> concepts</span>
                    <span><span className="font-semibold text-gray-700 dark:text-gray-300">{areas.length}</span> areas</span>
                  </div>

                  {/* Entry point hint */}
                  {entryPts.length > 0 && (
                    <div className="text-xs text-gray-400 mb-3">
                      ⭐ {entryPts.length} starting point{entryPts.length !== 1 ? 's' : ''}
                    </div>
                  )}

                  {/* area chips */}
                  <div className="flex flex-wrap gap-1">
                    {areas.slice(0, 5).map(area => {
                      const c = areaColor(area);
                      return (
                        <span key={area} className={`px-2 py-0.5 rounded-full text-xs font-medium ${c.badge}`}>
                          {area.length > 15 ? area.split(' ').slice(0, 2).join(' ') : area}
                        </span>
                      );
                    })}
                    {areas.length > 5 && (
                      <span className="px-2 py-0.5 rounded-full text-xs font-medium bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400">
                        +{areas.length - 5}
                      </span>
                    )}
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}
