import Link from 'next/link';
import dbConnect from '@/lib/mongodb';
import Chapter from '@/lib/models/Chapter';
import Breadcrumb from '@/components/Breadcrumb';

const SUBJECT_META = {
  maths: { name: 'Mathematics', icon: '📐', color: 'blue' },
  science: { name: 'Science', icon: '🔬', color: 'green' },
  physics: { name: 'Physics', icon: '⚛️', color: 'purple' },
  chemistry: { name: 'Chemistry', icon: '🧪', color: 'yellow' },
  biology: { name: 'Biology', icon: '🧬', color: 'red' },
};

export const dynamic = 'force-dynamic';

export default async function GradePage({ params }) {
  const { gradeId } = await params;
  const grade = parseInt(gradeId);
  await dbConnect();
  const chapters = await Chapter.find({ grade }).lean();

  const subjectMap = {};
  for (const ch of chapters) {
    if (!subjectMap[ch.subject]) subjectMap[ch.subject] = [];
    subjectMap[ch.subject].push(ch);
  }

  const subjects = Object.entries(subjectMap).map(([key, chs]) => ({
    key,
    ...(SUBJECT_META[key] || { name: key, icon: '📖', color: 'gray' }),
    chapters: chs.sort((a, b) => a.chapter - b.chapter),
  }));

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <Breadcrumb items={[{ label: `Grade ${grade}` }]} />

      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Grade {grade}</h1>
        <p className="text-gray-500 mt-1">
          {subjects.length} subject{subjects.length !== 1 ? 's' : ''} available
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {subjects.map(subj => (
          <Link key={subj.key} href={`/grade/${grade}/${subj.key}`}
            className="bg-white rounded-xl p-6 shadow-sm border border-gray-100 hover:shadow-md hover:border-blue-200 transition-all group">
            <div className="flex items-center gap-3 mb-4">
              <span className="text-3xl">{subj.icon}</span>
              <div>
                <h2 className="text-xl font-bold text-gray-900">{subj.name}</h2>
                <p className="text-sm text-gray-500">{subj.chapters.length} chapter{subj.chapters.length !== 1 ? 's' : ''}</p>
              </div>
            </div>
            <div className="space-y-1">
              {subj.chapters.slice(0, 5).map(ch => (
                <div key={ch.chapter} className="text-sm text-gray-600 truncate">
                  Ch {ch.chapter}: {ch.title.replace(/^Chapter \d+:\s*/i, '')}
                </div>
              ))}
              {subj.chapters.length > 5 && (
                <div className="text-sm text-blue-500">+{subj.chapters.length - 5} more</div>
              )}
            </div>
          </Link>
        ))}
      </div>

      {subjects.length === 0 && (
        <div className="text-center py-16 text-gray-400">
          <p className="text-lg">No content available for Grade {grade} yet.</p>
        </div>
      )}
    </div>
  );
}
