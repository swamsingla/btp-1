import Link from 'next/link';
import dbConnect from '@/lib/mongodb';
import Chapter from '@/lib/models/Chapter';

const GRADE_GROUPS = [
  { label: 'Secondary', range: [9, 10], emoji: '🎓' },
  { label: 'Senior Secondary', range: [11, 12], emoji: '🎯' },
];

const SUBJECT_META = {
  maths: { name: 'Mathematics', icon: '📐' },
  science: { name: 'Science', icon: '🔬' },
  physics: { name: 'Physics', icon: '⚛️' },
  chemistry: { name: 'Chemistry', icon: '🧪' },
  biology: { name: 'Biology', icon: '🧬' },
};

export const dynamic = 'force-dynamic';

export default async function Home() {
  await dbConnect();
  const chapters = await Chapter.find({}).lean();

  const gradeMap = {};
  for (const ch of chapters) {
    if (!gradeMap[ch.grade]) gradeMap[ch.grade] = {};
    if (!gradeMap[ch.grade][ch.subject]) gradeMap[ch.grade][ch.subject] = 0;
    gradeMap[ch.grade][ch.subject]++;
  }

  const grades = Object.entries(gradeMap)
    .map(([g, subjects]) => ({
      grade: parseInt(g),
      subjects: Object.entries(subjects).map(([key, count]) => ({
        key, ...(SUBJECT_META[key] || { name: key, icon: '📖' }), chapters: count,
      })),
      totalChapters: Object.values(subjects).reduce((a, b) => a + b, 0),
    }))
    .sort((a, b) => a.grade - b.grade);

  const totalChapters = chapters.length;
  const totalTopics = chapters.reduce((s, c) => s + (c.topicCount || 0), 0);

  return (
    <div>
      {/* Hero */}
      <section className="relative bg-gradient-to-br from-blue-600 via-blue-700 to-indigo-800 text-white overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-10 left-10 w-72 h-72 bg-white rounded-full blur-3xl"></div>
          <div className="absolute bottom-10 right-10 w-96 h-96 bg-blue-300 rounded-full blur-3xl"></div>
        </div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-white/15 backdrop-blur rounded-full text-sm font-medium mb-6">
            📚 NCERT Curriculum Aligned
          </div>
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight">
            Your Personal<br /><span className="text-blue-200">Study Companion</span>
          </h1>
          <p className="text-lg md:text-xl text-blue-100 max-w-2xl mx-auto mb-10 leading-relaxed">
            Topic-wise explanations, solved examples, practice problems and key formulas —
            everything you need to master your NCERT syllabus, all in one place.
          </p>
          <a href="#grades" className="inline-flex items-center gap-2 px-6 py-3 bg-white text-blue-700 font-semibold rounded-xl hover:bg-blue-50 transition-colors shadow-lg">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
            Start Learning
          </a>
          <div className="grid grid-cols-3 gap-6 max-w-md mx-auto mt-12">
            <div className="text-center"><div className="text-3xl font-bold">{grades.length}</div><div className="text-sm text-blue-200">Grades</div></div>
            <div className="text-center"><div className="text-3xl font-bold">{totalChapters}</div><div className="text-sm text-blue-200">Chapters</div></div>
            <div className="text-center"><div className="text-3xl font-bold">{totalTopics}</div><div className="text-sm text-blue-200">Topics</div></div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { icon: '📖', title: 'Topic-wise Learning', desc: 'Every chapter broken into focused topics with clear explanations, step-by-step solutions, and real examples' },
            { icon: '📐', title: 'Math Rendered Beautifully', desc: 'All formulas and equations displayed with professional LaTeX rendering — just like your textbook' },
            { icon: '✅', title: 'Practice with Solutions', desc: 'Graded practice problems (Easy, Medium, Hard) with detailed step-by-step solutions to build confidence' },
            { icon: '🎯', title: 'Exam-Ready Content', desc: 'Key formulas, common mistakes, memory aids and important theorems — everything needed for board preparation' },
          ].map((f, i) => (
            <div key={i} className="bg-white rounded-xl p-6 shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
              <div className="text-3xl mb-3">{f.icon}</div>
              <h3 className="font-semibold text-gray-900 mb-2">{f.title}</h3>
              <p className="text-sm text-gray-600 leading-relaxed">{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Grade Selection */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16" id="grades">
        <div className="text-center mb-10">
          <h2 className="text-2xl md:text-3xl font-bold text-gray-900">Select Your Grade</h2>
          <p className="text-gray-500 mt-2">Choose a grade to explore chapters and topics</p>
        </div>
        {GRADE_GROUPS.map(group => {
          const groupGrades = grades.filter(g => group.range.includes(g.grade));
          if (!groupGrades.length) return null;
          return (
            <div key={group.label} className="mb-10">
              <h3 className="text-lg font-semibold text-gray-700 mb-4 flex items-center gap-2">
                <span>{group.emoji}</span> {group.label}
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {groupGrades.map(g => (
                  <Link key={g.grade} href={`/grade/${g.grade}`}
                    className="flex items-center gap-4 bg-white rounded-xl p-5 shadow-sm border border-gray-100 hover:shadow-md hover:border-blue-200 transition-all group">
                    <div className="flex-shrink-0 w-14 h-14 bg-blue-50 rounded-xl flex items-center justify-center text-2xl font-bold text-blue-600 group-hover:bg-blue-100 transition-colors">{g.grade}</div>
                    <div className="flex-1">
                      <div className="font-semibold text-gray-900">Grade {g.grade}</div>
                      <div className="text-sm text-gray-500 mt-0.5">{g.subjects.length} subject{g.subjects.length > 1 ? 's' : ''} · {g.totalChapters} chapter{g.totalChapters > 1 ? 's' : ''}</div>
                      <div className="flex flex-wrap gap-1.5 mt-2">
                        {g.subjects.map(s => (
                          <span key={s.key} className="inline-flex items-center gap-1 px-2 py-0.5 bg-gray-100 rounded-full text-xs text-gray-600">{s.icon} {s.name}</span>
                        ))}
                      </div>
                    </div>
                    <svg className="flex-shrink-0 w-5 h-5 text-gray-300 group-hover:text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
                  </Link>
                ))}
              </div>
            </div>
          );
        })}
        {grades.length === 0 && (
          <div className="text-center py-12 text-gray-400">
            <p className="text-lg">No content available yet.</p>
            <p className="text-sm mt-2">Run the content generation pipeline to add chapters.</p>
          </div>
        )}
      </section>
    </div>
  );
}
