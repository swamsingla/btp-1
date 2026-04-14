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
              A free educational platform with structured, topic-wise learning material
              aligned to the NCERT curriculum for Grades 6–12.
            </p>
          </div>
          <div>
            <h4 className="text-white font-semibold mb-3">Grades</h4>
            <div className="grid grid-cols-2 gap-2 text-sm">
              {[6, 7, 8, 9, 10, 11, 12].map(g => (
                <Link key={g} href={`/grade/${g}`} className="block hover:text-white transition-colors">Grade {g}</Link>
              ))}
            </div>
          </div>
          <div>
            <h4 className="text-white font-semibold mb-3">Resources</h4>
            <div className="space-y-2 text-sm">
              <span className="block">Topic-wise Explanations</span>
              <span className="block">Practice Problems</span>
              <span className="block">Key Formulas & Summaries</span>
              <span className="block">Board Exam Preparation</span>
            </div>
          </div>
        </div>
        <div className="border-t border-gray-800 mt-8 pt-6 text-center text-sm">
          <p>&copy; {new Date().getFullYear()} NCERT Learn. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}
