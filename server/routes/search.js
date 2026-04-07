/**
 * Search API Routes
 * GET /api/search?q=query&lang=en
 */

const express = require('express');
const router = express.Router();
const { getCatalog } = require('../utils/catalogScanner');
const { loadContent } = require('../utils/contentLoader');

router.get('/', (req, res) => {
  const query = (req.query.q || '').trim().toLowerCase();
  const lang = req.query.lang || 'en';

  if (!query || query.length < 2) {
    return res.json({ results: [], total: 0 });
  }

  const catalog = getCatalog();
  const results = [];

  for (const grade of catalog.grades) {
    for (const subject of grade.subjects) {
      // Search in subject name
      const subjectMatch = subject.name.toLowerCase().includes(query);

      for (const ch of subject.chapters) {
        const content = loadContent(grade.grade, subject.key, ch.number, lang);

        const titleMatch = (content.title || '').toLowerCase().includes(query);
        const summaryMatch = (content.summary || '').toLowerCase().includes(query);

        let topicMatch = null;
        for (const topic of (content.topics || [])) {
          const tTitle = (topic.title || '').toLowerCase();
          const tContent = (topic.content || '').toLowerCase().replace(/<[^>]*>/g, '');
          if (tTitle.includes(query) || tContent.includes(query)) {
            topicMatch = topic;
            break;
          }
        }

        if (titleMatch || summaryMatch || subjectMatch || topicMatch) {
          results.push({
            grade: grade.grade,
            subject: subject.key,
            subjectName: subject.name,
            subjectIcon: subject.icon,
            chapter: ch.number,
            title: content.title || `Chapter ${ch.number}`,
            topic: topicMatch ? topicMatch.title : null,
            snippet: topicMatch
              ? topicMatch.content.replace(/<[^>]*>/g, '').substring(0, 200)
              : (content.summary || '').substring(0, 200),
          });
        }

        if (results.length >= 20) break;
      }
      if (results.length >= 20) break;
    }
    if (results.length >= 20) break;
  }

  res.json({ results, total: results.length });
});

module.exports = router;
