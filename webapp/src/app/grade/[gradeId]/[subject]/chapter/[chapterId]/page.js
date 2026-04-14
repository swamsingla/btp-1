import Link from 'next/link';
import dbConnect from '@/lib/mongodb';
import Chapter from '@/lib/models/Chapter';
import Topic from '@/lib/models/Topic';
import Breadcrumb from '@/components/Breadcrumb';

const SUBJECT_META = {
  maths: { name: 'Mathematics', icon: '📐' },
  science: { name: 'Science', icon: '🔬' },
  physics: { name: 'Physics', icon: '⚛️' },
  chemistry: { name: 'Chemistry', icon: '🧪' },
  biology: { name: 'Biology', icon: '🧬' },
};

export const dynamic = 'force-dynamic';

export default async function ChapterPage({ params }) {
  const { gradeId, subject, chapterId } = await params;
  const grade = parseInt(gradeId);
  const chapter = parseInt(chapterId);
  await dbConnect();

  const chapterDoc = await Chapter.findOne({ grade, subject, chapter }).lean();
  const topics = await Topic.find({ grade, subject, chapter }).sort({ order: 1 }).select('title topicNumber importance order _id').lean();
  const meta = SUBJECT_META[subject] || { name: subject, icon: '📖' };

  if (!chapterDoc) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Chapter not found</h1>
        <p className="text-gray-500 mt-2">This chapter hasn't been generated yet.</p>
        <Link href={`/grade/${grade}/${subject}`} className="inline-block mt-4 text-blue-600 hover:underline">← Back to {meta.name}</Link>
      </div>
    );
  }

  // Find adjacent chapters for navigation
  const allChapters = await Chapter.find({ grade, subject }).sort({ chapter: 1 }).select('chapter title').lean();
  const idx = allChapters.findIndex(c => c.chapter === chapter);
  const prev = idx > 0 ? allChapters[idx - 1] : null;
  const next = idx < allChapters.length - 1 ? allChapters[idx + 1] : null;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <Breadcrumb items={[
        { label: `Grade ${grade}`, href: `/grade/${grade}` },
        { label: meta.name, href: `/grade/${grade}/${subject}` },
        { label: chapterDoc.title },
      ]} />

      {/* Chapter header */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-100 mb-8">
        <div className="flex items-center gap-2 mb-3">
          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
            {meta.icon} {meta.name}
          </span>
          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-600">
            Grade {grade}
          </span>
        </div>
        <h1 className="text-2xl md:text-3xl font-bold text-gray-900">{chapterDoc.title}</h1>
        {chapterDoc.summary && (
          <p className="text-gray-600 mt-3 leading-relaxed">{chapterDoc.summary}</p>
        )}
        <div className="flex items-center gap-4 mt-4 text-sm text-gray-400">
          <span>{topics.length} topics</span>
        </div>
      </div>

      {/* Topic list */}
      <div className="mb-4">
        <h2 className="text-lg font-semibold text-gray-900">Topics in this Chapter</h2>
      </div>
      <div className="space-y-2">
        {topics.map((topic, i) => (
          <Link
            key={topic._id.toString()}
            href={`/grade/${grade}/${subject}/chapter/${chapter}/topic/${topic._id.toString()}`}
            className="flex items-center gap-4 bg-white rounded-lg p-4 shadow-sm border border-gray-100 hover:shadow-md hover:border-blue-200 transition-all group"
          >
            <div className="flex-shrink-0 w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center text-sm font-bold text-blue-600 group-hover:bg-blue-100 transition-colors">
              {topic.topicNumber}
            </div>
            <div className="flex-1 min-w-0">
              <h3 className="font-medium text-gray-900">{topic.title}</h3>
            </div>
            <svg className="flex-shrink-0 w-5 h-5 text-gray-300 group-hover:text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
          </Link>
        ))}
      </div>

      {/* Chapter navigation */}
      <div className="flex justify-between mt-10">
        {prev ? (
          <Link href={`/grade/${grade}/${subject}/chapter/${prev.chapter}`}
            className="flex items-center gap-2 text-sm text-gray-600 hover:text-blue-600 transition-colors">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="15 18 9 12 15 6"/></svg>
            <span>Ch {prev.chapter}: {prev.title.replace(/^Chapter \d+:\s*/i, '')}</span>
          </Link>
        ) : <div />}
        {next ? (
          <Link href={`/grade/${grade}/${subject}/chapter/${next.chapter}`}
            className="flex items-center gap-2 text-sm text-gray-600 hover:text-blue-600 transition-colors">
            <span>Ch {next.chapter}: {next.title.replace(/^Chapter \d+:\s*/i, '')}</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="9 18 15 12 9 6"/></svg>
          </Link>
        ) : <div />}
      </div>
    </div>
  );
}
