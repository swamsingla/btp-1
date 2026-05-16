import Link from 'next/link';

export default function Footer() {
  const grades = [6, 7, 8, 9, 10, 11, 12];

  return (
    <footer className="bg-gray-900 text-gray-400 mt-16 dark:bg-gray-950 dark:border-t dark:border-gray-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand */}
          <div className="md:col-span-1">
            <Link href="/" className="flex items-center gap-2 text-white text-lg font-bold">
              <span className="text-xl">📚</span> GraphLearn
            </Link>
            <p className="mt-3 text-sm leading-relaxed">
              A knowledge-graph powered educational platform covering school Mathematics
              and Science, Grades 6–12. Every concept linked to its prerequisites.
            </p>
            <p className="mt-3 text-xs text-gray-600">
              BTP Project · IIIT Hyderabad
            </p>
          </div>

          {/* Mathematics */}
          <div>
            <h4 className="text-white font-semibold mb-3 flex items-center gap-1.5">
              <span>📐</span> Mathematics
            </h4>
            <div className="grid grid-cols-2 gap-1.5 text-sm">
              {grades.map(g => (
                <Link key={g} href={`/maths/${g}`}
                  className="block hover:text-white transition-colors">
                  Grade {g}
                </Link>
              ))}
            </div>
          </div>

          {/* Science */}
          <div>
            <h4 className="text-white font-semibold mb-3 flex items-center gap-1.5">
              <span>⚗️</span> Science
            </h4>
            <div className="grid grid-cols-2 gap-1.5 text-sm">
              {grades.map(g => (
                <Link key={g} href={`/science/${g}`}
                  className="block hover:text-white transition-colors">
                  Grade {g}
                </Link>
              ))}
            </div>
          </div>

          {/* Platform */}
          <div>
            <h4 className="text-white font-semibold mb-3">Platform</h4>
            <div className="space-y-2 text-sm">
              <span className="block">324 Maths Concepts</span>
              <span className="block">382 Science Concepts</span>
              <span className="block">497 + 552 Prerequisite Links</span>
              <span className="block">Knowledge Graph Architecture</span>
              <span className="block">Wikipedia-Style Navigation</span>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-8 pt-6 text-center text-sm">
          <p>&copy; {new Date().getFullYear()} GraphLearn — BTP Project, IIIT Hyderabad</p>
        </div>
      </div>
    </footer>
  );
}

