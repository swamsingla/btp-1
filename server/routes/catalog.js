/**
 * Catalog API Routes
 * GET /api/catalog          — Full catalog
 * GET /api/catalog/summary  — Stats only
 * GET /api/catalog/:grade   — Single grade
 */

const express = require('express');
const router = express.Router();
const { getCatalog } = require('../utils/catalogScanner');

// Full catalog
router.get('/', (req, res) => {
  const catalog = getCatalog();
  res.json(catalog);
});

// Summary stats
router.get('/summary', (req, res) => {
  const catalog = getCatalog();
  res.json(catalog.summary);
});

// Single grade
router.get('/:grade', (req, res) => {
  const gradeNum = parseInt(req.params.grade, 10);
  const catalog = getCatalog();
  const grade = catalog.grades.find(g => g.grade === gradeNum);

  if (!grade) {
    return res.status(404).json({ error: `Grade ${gradeNum} not found` });
  }

  res.json(grade);
});

// Single subject within a grade
router.get('/:grade/:subject', (req, res) => {
  const gradeNum = parseInt(req.params.grade, 10);
  const subjectKey = req.params.subject.toLowerCase();
  const catalog = getCatalog();

  const grade = catalog.grades.find(g => g.grade === gradeNum);
  if (!grade) {
    return res.status(404).json({ error: `Grade ${gradeNum} not found` });
  }

  const subject = grade.subjects.find(s => s.key === subjectKey);
  if (!subject) {
    return res.status(404).json({ error: `Subject '${subjectKey}' not found in Grade ${gradeNum}` });
  }

  res.json({ grade: gradeNum, subject });
});

module.exports = router;
