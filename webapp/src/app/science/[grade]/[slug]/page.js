import Link from 'next/link';
import { notFound } from 'next/navigation';
import {
  getScienceGrades,
  getScienceConcept,
  getScienceConceptsForGrade,
  scienceAreaColor,
} from '@/lib/science-graph';

export async function generateStaticParams() {
  const params = [];
  for (const grade of getScienceGrades()) {
    for (const concept of getScienceConceptsForGrade(grade)) {
      params.push({ grade: String(grade), slug: concept.slug });
    }
  }
  return params;
}

export async function generateMetadata({ params }) {
  const { grade, slug } = await params;
  const concept = getScienceConcept(slug);
  if (!concept) return { title: 'Not Found' };
  return {
    title: `${concept.canonical_name} · Grade ${grade} Science — GraphLearn`,
    description: concept.description,
  };
}

export default async function ScienceConceptPage({ params }) {
  const { grade: gradeStr, slug } = await params;
  const grade   = parseInt(gradeStr);
  const concept = getScienceConcept(slug);

  if (!concept || isNaN(grade) || !concept.grades.includes(grade)) notFound();

  const c = scienceAreaColor(concept.area);

  const prereqs = (concept.prerequisites || [])
    .map(s => getScienceConcept(s))
    .filter(Boolean);

  const leadsTo = (concept.leads_to || [])
    .map(s => getScienceConcept(s))
    .filter(Boolean);

  const otherGrades = concept.grades.filter(g => g !== grade);

  const sameAreaConcepts = getScienceConceptsForGrade(grade)
    .filter(cc => (cc.area || 'General') === (concept.area || 'General') && cc.slug !== slug)
    .slice(0, 8);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="lg:grid lg:grid-cols-4 lg:gap-8">
        {/* ═══ Main Content (3 cols) ═══ */}
        <div className="lg:col-span-3">
          {/* Breadcrumb */}
          <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6 flex-wrap">
            <Link href="/" className="hover:text-teal-600 transition-colors">Home</Link>
            <span className="text-gray-300">/</span>
            <Link href="/science" className="hover:text-teal-600 transition-colors">Science</Link>
            <span className="text-gray-300">/</span>
            <Link href={`/science/${grade}`} className="hover:text-teal-600 transition-colors">Grade {grade}</Link>
            <span className="text-gray-300">/</span>
            <span className="text-gray-900 dark:text-gray-100 font-medium">{concept.canonical_name}</span>
          </nav>

          {/* Area badge + grade indicator */}
          <div className="flex items-center gap-3 mb-4 flex-wrap">
            <span className={`px-3 py-1 rounded-full text-xs font-semibold ${c.badge}`}>
              {concept.area || 'General'}
            </span>
            <span className="text-xs text-gray-400 dark:text-gray-500">Grade {grade}</span>
            {otherGrades.length > 0 && (
              <span className="text-xs text-gray-400 dark:text-gray-500">
                · Also in{' '}
                {otherGrades.map((g, i) => (
                  <span key={g}>
                    {i > 0 && ', '}
                    <Link href={`/science/${g}/${slug}`} className="text-teal-500 hover:underline">
                      Grade {g}
                    </Link>
                  </span>
                ))}
              </span>
            )}
          </div>

          {/* Title */}
          <h1 className="text-3xl md:text-4xl font-extrabold text-gray-900 dark:text-gray-100 mb-3 leading-tight">
            {concept.canonical_name}
          </h1>

          {/* Description */}
          <p className="text-gray-600 dark:text-gray-400 text-base md:text-lg leading-relaxed mb-8 max-w-3xl">
            {concept.description}
          </p>

          {/* Prerequisites */}
          {prereqs.length > 0 && (
            <section className="mb-8">
              <h2 className="flex items-center gap-2 text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-4">
                <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="15 18 9 12 15 6" />
                </svg>
                Prerequisites — you should know these first
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {prereqs.map(pre => {
                  const pc = scienceAreaColor(pre.area);
                  const targetGrade = pre.grades.includes(grade) ? grade : pre.grades[0];
                  return (
                    <Link
                      key={pre.slug}
                      href={`/science/${targetGrade}/${pre.slug}`}
                      className={`flex items-center gap-3 px-4 py-3 rounded-xl border ${pc.border} ${pc.bg} dark:bg-gray-800 hover:shadow-md hover:-translate-y-0.5 transition-all group`}
                    >
                      <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-white dark:bg-gray-700 flex items-center justify-center shadow-sm">
                        <svg className="w-4 h-4 text-gray-400 group-hover:text-teal-500 transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <polyline points="15 18 9 12 15 6" />
                        </svg>
                      </div>
                      <div className="min-w-0">
                        <div className={`text-sm font-semibold ${pc.text} group-hover:text-teal-600 transition-colors truncate`}>
                          {pre.canonical_name}
                        </div>
                        <div className="text-xs text-gray-400 dark:text-gray-500 truncate">
                          {pre.area || 'General'} · Grade {targetGrade}
                        </div>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </section>
          )}

          {/* Content placeholder */}
          <section className="mb-8">
            <div className={`rounded-2xl border-2 border-dashed ${c.border} bg-gradient-to-br ${c.bg} dark:bg-gray-800/50 p-10 text-center`}>
              <div className="text-5xl mb-4">📝</div>
              <h3 className={`text-xl font-bold ${c.text} mb-2`}>Content Coming Soon</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400 max-w-md mx-auto mb-4">
                Detailed explanations, worked examples, and practice problems for{' '}
                <strong>{concept.canonical_name}</strong> will appear here.
              </p>
              <div className="inline-flex items-center gap-2 px-4 py-2 bg-white dark:bg-gray-700 rounded-lg text-xs text-gray-500 dark:text-gray-400 shadow-sm">
                <span className="w-2 h-2 bg-yellow-400 rounded-full animate-pulse" />
                Content generation in progress
              </div>
            </div>
          </section>

          {/* What this unlocks */}
          {leadsTo.length > 0 && (
            <section className="mb-8">
              <h2 className="flex items-center gap-2 text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-4">
                <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="9 18 15 12 9 6" />
                </svg>
                What this unlocks — study these next
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {leadsTo.map(next => {
                  const nc = scienceAreaColor(next.area);
                  const targetGrade = next.grades.includes(grade) ? grade : next.grades[0];
                  return (
                    <Link
                      key={next.slug}
                      href={`/science/${targetGrade}/${next.slug}`}
                      className={`flex items-center gap-3 px-4 py-3 rounded-xl border ${nc.border} bg-white dark:bg-gray-800 hover:shadow-md hover:-translate-y-0.5 transition-all group`}
                    >
                      <div className="min-w-0 flex-1">
                        <div className={`text-sm font-semibold ${nc.text} group-hover:text-teal-600 transition-colors truncate`}>
                          {next.canonical_name}
                        </div>
                        <div className="text-xs text-gray-400 dark:text-gray-500 truncate">
                          {next.area || 'General'} · Grade {targetGrade}
                        </div>
                      </div>
                      <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-gray-50 dark:bg-gray-700 flex items-center justify-center">
                        <svg className="w-4 h-4 text-gray-400 group-hover:text-teal-500 transition-colors" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <polyline points="9 18 15 12 9 6" />
                        </svg>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </section>
          )}

          {/* Multi-grade navigation */}
          {otherGrades.length > 0 && (
            <section className="mb-8">
              <h2 className="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-4">
                📚 This concept at different levels
              </h2>
              <div className="flex flex-wrap gap-3">
                {concept.grades.map(g => (
                  <Link
                    key={g}
                    href={`/science/${g}/${slug}`}
                    className={`px-4 py-2 rounded-xl border text-sm font-medium transition-all ${
                      g === grade
                        ? 'bg-teal-600 text-white border-teal-600 shadow-md'
                        : 'bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-300 hover:border-teal-300 hover:text-teal-600'
                    }`}
                  >
                    Grade {g}
                  </Link>
                ))}
              </div>
            </section>
          )}

          {/* Bottom navigation */}
          <div className="flex items-center justify-between pt-6 border-t border-gray-100 dark:border-gray-700">
            <Link
              href={`/science/${grade}`}
              className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-teal-600 transition-colors"
            >
              <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <polyline points="15 18 9 12 15 6" />
              </svg>
              Back to Grade {grade}
            </Link>
            <Link
              href="/science"
              className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-teal-600 transition-colors"
            >
              All Grades
              <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <polyline points="9 18 15 12 9 6" />
              </svg>
            </Link>
          </div>
        </div>

        {/* ═══ Sidebar (1 col) ═══ */}
        <aside className="hidden lg:block">
          <div className="sticky top-24 space-y-6">
            {/* Concept info card */}
            <div className="bg-white dark:bg-gray-800 rounded-2xl border border-gray-100 dark:border-gray-700 p-5 shadow-sm">
              <h3 className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider mb-3">Concept Info</h3>
              <dl className="space-y-3 text-sm">
                <div className="flex justify-between">
                  <dt className="text-gray-500 dark:text-gray-400">Area</dt>
                  <dd className={`font-medium ${c.text}`}>{concept.area || 'General'}</dd>
                </div>
                <div className="flex justify-between">
                  <dt className="text-gray-500 dark:text-gray-400">Grades</dt>
                  <dd className="font-medium text-gray-900 dark:text-gray-100">{concept.grades.join(', ')}</dd>
                </div>
                <div className="flex justify-between">
                  <dt className="text-gray-500 dark:text-gray-400">Prerequisites</dt>
                  <dd className="font-medium text-gray-900 dark:text-gray-100">{prereqs.length}</dd>
                </div>
                <div className="flex justify-between">
                  <dt className="text-gray-500 dark:text-gray-400">Unlocks</dt>
                  <dd className="font-medium text-gray-900 dark:text-gray-100">{leadsTo.length}</dd>
                </div>
              </dl>
            </div>

            {/* Same area concepts */}
            {sameAreaConcepts.length > 0 && (
              <div className="bg-white dark:bg-gray-800 rounded-2xl border border-gray-100 dark:border-gray-700 p-5 shadow-sm">
                <h3 className="text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider mb-3">
                  More in {concept.area || 'General'}
                </h3>
                <ul className="space-y-2">
                  {sameAreaConcepts.map(cc => (
                    <li key={cc.slug}>
                      <Link
                        href={`/science/${grade}/${cc.slug}`}
                        className="text-sm text-gray-600 dark:text-gray-400 hover:text-teal-600 dark:hover:text-teal-400 transition-colors line-clamp-1"
                      >
                        {cc.canonical_name}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </aside>
      </div>
    </div>
  );
}
