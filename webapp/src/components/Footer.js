import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-400 mt-16 dark:bg-gray-950">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="md:col-span-1">
            <Link href="/" className="flex items-center gap-2 text-white text-lg font-bold">
              <span className="text-xl">📚</span> NCERT Learn
            </Link>
            <p className="mt-3 text-sm leading-relaxed">
              A knowledge-graph powered educational platform for NCERT Mathematics,
              Grades 6–12. Every concept linked to its prerequisites.
            </p>
          </div>
          <div>
            <h4 className="text-white font-semibold mb-3">Explore by Grade</h4>
            <div className="grid grid-cols-2 gap-2 text-sm">
              {[6, 7, 8, 9, 10, 11, 12].map(g => (
                <Link key={g} href={`/maths/${g}`} className="block hover:text-white transition-colors">Grade {g}</Link>
              ))}
            </div>
          </div>
          <div>
            <h4 className="text-white font-semibold mb-3">About</h4>
            <div className="space-y-2 text-sm">
              <span className="block">324 Mathematical Concepts</span>
              <span className="block">497 Prerequisite Connections</span>
              <span className="block">Wikipedia-Style Navigation</span>
              <span className="block">Knowledge Graph Architecture</span>
            </div>
          </div>
        </div>
        <div className="border-t border-gray-800 mt-8 pt-6 text-center text-sm">
          <p>&copy; {new Date().getFullYear()} NCERT Learn — BTP Project, IIIT Hyderabad</p>
        </div>
      </div>
    </footer>
  );
}
