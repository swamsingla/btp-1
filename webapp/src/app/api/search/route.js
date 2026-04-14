import { NextResponse } from 'next/server';
import dbConnect from '@/lib/mongodb';
import Topic from '@/lib/models/Topic';
import Chapter from '@/lib/models/Chapter';

const SUBJECT_META = {
  maths: { name: 'Mathematics', icon: '📐' },
  science: { name: 'Science', icon: '🔬' },
  physics: { name: 'Physics', icon: '⚛️' },
  chemistry: { name: 'Chemistry', icon: '🧪' },
  biology: { name: 'Biology', icon: '🧬' },
};

export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const query = (searchParams.get('q') || '').trim();
  const gradeFilter = searchParams.get('grade');
  const subjectFilter = searchParams.get('subject');
  const chapterFilter = searchParams.get('chapter');

  if (!query || query.length < 2) {
    return NextResponse.json({ results: [], total: 0 });
  }

  await dbConnect();

  // Search topics — match substring in title or section headings only
  const escapedQuery = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const regex = new RegExp(escapedQuery, 'i');

  // Build filter conditions
  const topicFilter = {
    $or: [
      { title: regex },
      { headings: regex },
    ]
  };
  if (gradeFilter) topicFilter.grade = parseInt(gradeFilter);
  if (subjectFilter) topicFilter.subject = subjectFilter;
  if (chapterFilter) topicFilter.chapter = parseInt(chapterFilter);

  const chapterFilterQuery = { title: regex };
  if (gradeFilter) chapterFilterQuery.grade = parseInt(gradeFilter);
  if (subjectFilter) chapterFilterQuery.subject = subjectFilter;
  if (chapterFilter) chapterFilterQuery.chapter = parseInt(chapterFilter);

  let topics = [];
  try {
    topics = await Topic.find(topicFilter)
      .limit(20)
      .select('title topicNumber grade subject chapter _id headings')
      .lean();
  } catch (e) {
    topics = await Topic.find({ title: regex, ...(gradeFilter && { grade: parseInt(gradeFilter) }), ...(subjectFilter && { subject: subjectFilter }), ...(chapterFilter && { chapter: parseInt(chapterFilter) }) })
      .limit(20)
      .select('title topicNumber grade subject chapter _id headings')
      .lean();
  }

  // Also search chapter titles
  const chapters = await Chapter.find(chapterFilterQuery)
    .limit(5)
    .select('title grade subject chapter summary')
    .lean();

  const results = [];

  for (const ch of chapters) {
    const meta = SUBJECT_META[ch.subject] || { name: ch.subject, icon: '📖' };
    results.push({
      grade: ch.grade,
      subject: ch.subject,
      subjectName: meta.name,
      subjectIcon: meta.icon,
      chapter: ch.chapter,
      chapterTitle: ch.title,
      topicTitle: null,
      topicId: null,
      snippet: ch.summary ? ch.summary.substring(0, 200) : '',
    });
  }

  for (const t of topics) {
    const meta = SUBJECT_META[t.subject] || { name: t.subject, icon: '📖' };
    // Show matched headings as snippet
    let snippet = '';
    if (t.headings) {
      const matchedHeadings = t.headings.split('\n').filter(h => regex.test(h));
      snippet = matchedHeadings.length > 0
        ? matchedHeadings.slice(0, 3).join(' · ')
        : t.headings.split('\n').slice(0, 3).join(' · ');
    }

    results.push({
      grade: t.grade,
      subject: t.subject,
      subjectName: meta.name,
      subjectIcon: meta.icon,
      chapter: t.chapter,
      chapterTitle: `Chapter ${t.chapter}`,
      topicTitle: `${t.topicNumber} ${t.title}`,
      topicId: t._id.toString(),
      snippet,
    });
  }

  return NextResponse.json({ results, total: results.length });
}
