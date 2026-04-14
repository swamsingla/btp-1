import Link from 'next/link';
import dbConnect from '@/lib/mongodb';
import Chapter from '@/lib/models/Chapter';
import Topic from '@/lib/models/Topic';
import Breadcrumb from '@/components/Breadcrumb';
import TopicPageClient from '@/components/TopicPageClient';
import ReadingProgress from '@/components/ReadingProgress';
import BackToTop from '@/components/BackToTop';

const SUBJECT_META = {
  maths: { name: 'Mathematics', icon: '📐' },
  science: { name: 'Science', icon: '🔬' },
  physics: { name: 'Physics', icon: '⚛️' },
  chemistry: { name: 'Chemistry', icon: '🧪' },
  biology: { name: 'Biology', icon: '🧬' },
};

export const dynamic = 'force-dynamic';

export default async function TopicPage({ params }) {
  const { gradeId, subject, chapterId, topicId } = await params;
  const grade = parseInt(gradeId);
  const chapter = parseInt(chapterId);
  await dbConnect();

  const topic = await Topic.findById(topicId).lean();
  if (!topic) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-16 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Topic not found</h1>
        <Link href={`/grade/${grade}/${subject}/chapter/${chapter}`} className="text-blue-600 hover:underline mt-4 inline-block">← Back to chapter</Link>
      </div>
    );
  }

  const chapterDoc = await Chapter.findOne({ grade, subject, chapter }).lean();
  const allTopics = await Topic.find({ grade, subject, chapter }).sort({ order: 1 }).select('title topicNumber _id order').lean();
  const meta = SUBJECT_META[subject] || { name: subject, icon: '📖' };

  const currentIdx = allTopics.findIndex(t => t._id.toString() === topicId);
  const prevTopic = currentIdx > 0 ? allTopics[currentIdx - 1] : null;
  const nextTopic = currentIdx < allTopics.length - 1 ? allTopics[currentIdx + 1] : null;


  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <ReadingProgress />
      <BackToTop />
      <Breadcrumb items={[
        { label: `Grade ${grade}`, href: `/grade/${grade}` },
        { label: meta.name, href: `/grade/${grade}/${subject}` },
        { label: chapterDoc?.title || `Chapter ${chapter}`, href: `/grade/${grade}/${subject}/chapter/${chapter}` },
        { label: topic.title },
      ]} />

      <div className="flex gap-8">
        {/* Sidebar (desktop) */}
        <aside className="hidden lg:block w-64 flex-shrink-0">
          <div className="sticky top-20 bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden">
            <div className="p-3 bg-gray-50 border-b border-gray-100">
              <h3 className="text-sm font-semibold text-gray-700">Topics</h3>
            </div>
            <nav className="max-h-[calc(100vh-12rem)] overflow-y-auto p-2">
              {allTopics.map(t => {
                const isActive = t._id.toString() === topicId;
                return (
                  <Link key={t._id.toString()}
                    href={`/grade/${grade}/${subject}/chapter/${chapter}/topic/${t._id.toString()}`}
                    className={`flex items-center gap-2 px-3 py-2 rounded-lg text-sm transition-colors ${
                      isActive
                        ? 'bg-blue-50 text-blue-700 font-medium'
                        : 'text-gray-600 hover:bg-gray-50'
                    }`}
                  >
                    <span className={`flex-shrink-0 w-7 text-xs font-mono ${isActive ? 'text-blue-600' : 'text-gray-400'}`}>
                      {t.topicNumber}
                    </span>
                    <span className="truncate">{t.title}</span>
                  </Link>
                );
              })}
            </nav>
          </div>
        </aside>

        {/* Main content */}
        <div className="flex-1 min-w-0">
          <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 md:p-8">
            {/* Topic header */}
            <div className="mb-6 pb-4 border-b border-gray-100">
              <div className="flex items-center gap-2 mb-2">
                <span className="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
                  {topic.topicNumber}
                </span>
                {topic.importance >= 4 && (
                  <span className="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-700">
                    Important
                  </span>
                )}
              </div>
              <h1 className="text-2xl md:text-3xl font-bold text-gray-900">{topic.title}</h1>
            </div>

            <TopicPageClient
              topic={{ content: topic.content }}
              translations={topic.translations || {}}
            />
          </div>

          {/* Topic navigation */}
          <div className="flex justify-between mt-6">
            {prevTopic ? (
              <Link href={`/grade/${grade}/${subject}/chapter/${chapter}/topic/${prevTopic._id.toString()}`}
                className="flex items-center gap-2 px-4 py-3 bg-white rounded-xl border border-gray-100 hover:border-blue-200 shadow-sm transition-all text-sm group max-w-[45%]">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="flex-shrink-0 text-gray-400 group-hover:text-blue-500"><polyline points="15 18 9 12 15 6"/></svg>
                <div className="min-w-0">
                  <div className="text-xs text-gray-400">Previous</div>
                  <div className="text-gray-700 font-medium truncate">{prevTopic.topicNumber} {prevTopic.title}</div>
                </div>
              </Link>
            ) : <div />}
            {nextTopic ? (
              <Link href={`/grade/${grade}/${subject}/chapter/${chapter}/topic/${nextTopic._id.toString()}`}
                className="flex items-center gap-2 px-4 py-3 bg-white rounded-xl border border-gray-100 hover:border-blue-200 shadow-sm transition-all text-sm group max-w-[45%] text-right ml-auto">
                <div className="min-w-0">
                  <div className="text-xs text-gray-400">Next</div>
                  <div className="text-gray-700 font-medium truncate">{nextTopic.topicNumber} {nextTopic.title}</div>
                </div>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="flex-shrink-0 text-gray-400 group-hover:text-blue-500"><polyline points="9 18 15 12 9 6"/></svg>
              </Link>
            ) : <div />}
          </div>
        </div>
      </div>
    </div>
  );
}
