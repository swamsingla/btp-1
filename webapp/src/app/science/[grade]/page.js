import Link from 'next/link';
import { notFound } from 'next/navigation';
import {
  getScienceGrades,
  getScienceAreaGroups,
  getScienceConcept,
  getScienceEntryPoints,
  scienceAreaColor,
} from '@/lib/science-graph';

export async function generateStaticParams() {
  return getScienceGrades().map(g => ({ grade: String(g) }));
}

export async function generateMetadata({ params }) {
  const { grade } = await params;
  return { title: `Grade ${grade} Science — GraphLearn` };
}

export default async function ScienceGradePage({ params }) {
  const { grade: gradeStr } = await params;
  const grade = parseInt(gradeStr);
  if (isNaN(grade)) notFound();

  const areaGroups = getScienceAreaGroups(grade);
  if (Object.keys(areaGroups).length === 0) notFound();

  const totalConcepts = Object.values(areaGroups).reduce((s, arr) => s + arr.length, 0);
  const sortedAreas   = Object.keys(areaGroups).sort();
  const entryPoints   = getScienceEntryPoints(grade);
  const entrySlugSet  = new Set(entryPoints.map(e => e.slug));

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6">
        <Link href="/" className="hover:text-teal-600 transition-colors">Home</Link>
        <span>/</span>
        <Link href="/science" className="hover:text-teal-600 transition-colors">Science</Link>
        <span>/</span>
        <span className="text-gray-900 dark:text-gray-100 font-medium">Grade {grade}</span>
      </nav>

      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100">
          Grade {grade} — Science
        </h1>
        <p className="text-gray-500 dark:text-gray-400 mt-1">
          {totalConcepts} concept{totalConcepts !== 1 ? 's' : ''} across {sortedAreas.length} areas
        </p>
      </div>

      {/* Area jump links */}
      <div className="flex flex-wrap gap-2 mb-8">
        {sortedAreas.map(area => {
          const c = scienceAreaColor(area);
          return (
            <a
              key={area}
              href={`#${area.replace(/\s+/g, '-').toLowerCase()}`}
              className={`px-3 py-1 rounded-full text-xs font-medium ${c.badge} hover:opacity-80 transition-opacity`}
            >
              {area} <span className="opacity-60">({areaGroups[area].length})</span>
            </a>
          );
        })}
      </div>

      {/* Concepts by area */}
      <div className="space-y-10">
        {sortedAreas.map(area => {
          const concepts = areaGroups[area];
          const c = scienceAreaColor(area);
          return (
            <section key={area} id={area.replace(/\s+/g, '-').toLowerCase()}>
              <div className="flex items-center gap-3 mb-4">
                <h2 className={`text-lg font-bold ${c.text}`}>{area}</h2>
                <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${c.badge}`}>
                  {concepts.length}
                </span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {concepts.map(concept => {
                  const prereqNames = (concept.prerequisites || [])
                    .map(slug => getScienceConcept(slug)?.canonical_name)
                    .filter(Boolean)
                    .slice(0, 2);
                  const isEntry = entrySlugSet.has(concept.slug);

                  return (
                    <Link
                      key={concept.slug}
                      href={`/science/${grade}/${concept.slug}`}
                      className={`group relative bg-white dark:bg-gray-800 rounded-xl border ${c.border} hover:shadow-md hover:-translate-y-0.5 transition-all p-4`}
                    >
                      {isEntry && (
                        <span className="absolute top-3 right-3 text-yellow-400 text-xs" title="No prerequisites">⭐</span>
                      )}
                      <h3 className="font-semibold text-gray-900 dark:text-gray-100 group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors text-sm leading-snug mb-1">
                        {concept.canonical_name}
                      </h3>
                      <p className="text-xs text-gray-400 dark:text-gray-500 line-clamp-2 mb-3">
                        {concept.description}
                      </p>
                      {prereqNames.length > 0 && (
                        <div className="flex flex-wrap gap-1">
                          {prereqNames.map(name => (
                            <span key={name} className="inline-flex items-center gap-1 px-2 py-0.5 bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 rounded text-xs">
                              <span className="text-gray-300">←</span> {name}
                            </span>
                          ))}
                        </div>
                      )}
                      {concept.grades.length > 1 && (
                        <span className="absolute bottom-3 right-3 text-xs text-gray-300 dark:text-gray-600">
                          Gr {concept.grades.join(',')}
                        </span>
                      )}
                    </Link>
                  );
                })}
              </div>
            </section>
          );
        })}
      </div>
    </div>
  );
}
