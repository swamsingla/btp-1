import { NextResponse } from 'next/server';
import { searchConcepts } from '@/lib/knowledge-graph';

export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get('q') || '';

  if (q.length < 2) {
    return NextResponse.json({ results: [] });
  }

  const concepts = searchConcepts(q, 15);

  const results = concepts.map(c => ({
    slug: c.slug,
    name: c.canonical_name,
    description: c.description || '',
    area: c.area || 'General',
    grades: c.grades || [],
    prereqCount: (c.prerequisites || []).length,
    leadsToCount: (c.leads_to || []).length,
  }));

  return NextResponse.json({ results });
}
