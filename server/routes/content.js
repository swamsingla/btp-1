/**
 * Content API Routes
 * GET /api/content/:grade/:subject/:chapter?lang=en
 */

const express = require('express');
const router = express.Router();
const { getCatalog } = require('../utils/catalogScanner');
const { loadContent } = require('../utils/contentLoader');

const SUPPORTED_LANGS = ['en', 'hi', 'te', 'or'];

router.get('/:grade/:subject/:chapter', (req, res) => {
  const gradeNum = parseInt(req.params.grade, 10);
  const subjectKey = req.params.subject.toLowerCase();
  const chapterNum = parseInt(req.params.chapter, 10);
  const lang = SUPPORTED_LANGS.includes(req.query.lang) ? req.query.lang : 'en';

  // Validate the route exists in catalog
  const catalog = getCatalog();
  const grade = catalog.grades.find(g => g.grade === gradeNum);
  if (!grade) {
    return res.status(404).json({ error: `Grade ${gradeNum} not found` });
  }

  const subject = grade.subjects.find(s => s.key === subjectKey);
  if (!subject) {
    return res.status(404).json({ error: `Subject '${subjectKey}' not found in Grade ${gradeNum}` });
  }

  const chapter = subject.chapters.find(c => c.number === chapterNum);
  if (!chapter) {
    return res.status(404).json({ error: `Chapter ${chapterNum} not found` });
  }

  const content = loadContent(gradeNum, subjectKey, chapterNum, lang);
  res.json({
    ...content,
    chapterMeta: chapter,
    availableLanguages: SUPPORTED_LANGS,
  });
});

module.exports = router;
