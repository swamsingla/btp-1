import Link from 'next/link';
import dbConnect from '@/lib/mongodb';
import Chapter from '@/lib/models/Chapter';
import Breadcrumb from '@/components/Breadcrumb';

const SUBJECT_META = {
  maths: { name: 'Mathematics', icon: '📐' },
  science: { name: 'Science', icon: '🔬' },
  physics: { name: 'Physics', icon: '⚛️' },
  chemistry: { name: 'Chemistry', icon: '🧪' },
  biology: { name: 'Biology', icon: '🧬' },
};

export const dynamic = 'force-dynamic';

export default async function SubjectPage({ params }) {
  const { gradeId, subject } = await params;
  const grade = parseInt(gradeId);
  await dbConnect();
  const chapters = await Chapter.find({ grade, subject }).sort({ chapter: 1 }).lean();
  const meta = SUBJECT_META[subject] || { name: subject, icon: '📖' };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <Breadcrumb items={[
        { label: `Grade ${grade}`, href: `/grade/${grade}` },
        { label: meta.name },
      ]} />

      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
          <span className="text-4xl">{meta.icon}</span> {meta.name}
        </h1>
        <p className="text-gray-500 mt-1">Grade {grade} · {chapters.length} chapter{chapters.length !== 1 ? 's' : ''}</p>
      </div>

      <div className="space-y-3">
        {chapters.map((ch, i) => (
          <Link key={ch.chapter} href={`/grade/${grade}/${subject}/chapter/${ch.chapter}`}
            className="flex items-center gap-4 bg-white rounded-xl p-5 shadow-sm border border-gray-100 hover:shadow-md hover:border-blue-200 transition-all group">
            <div className="flex-shrink-0 w-12 h-12 bg-blue-50 rounded-lg flex items-center justify-center text-lg font-bold text-blue-600 group-hover:bg-blue-100 transition-colors">
              {ch.chapter}
            </div>
            <div className="flex-1 min-w-0">
              <h3 className="font-semibold text-gray-900 truncate">{ch.title}</h3>
              {ch.summary && (
                <p className="text-sm text-gray-500 mt-1 line-clamp-2">{ch.summary}</p>
              )}
              <div className="flex items-center gap-3 mt-2 text-xs text-gray-400">
                <span>{ch.topicCount || 0} topics</span>
              </div>
            </div>
            <svg className="flex-shrink-0 w-5 h-5 text-gray-300 group-hover:text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
          </Link>
        ))}
      </div>

      {chapters.length === 0 && (
        <div className="text-center py-16 text-gray-400">
          <p className="text-lg">No chapters available yet.</p>
        </div>
      )}
    </div>
  );
}
