/**
 * Scans data/input directory and builds the full content catalog.
 * Returns a structured object: { grades: [ { grade, subjects: [...] } ] }
 */

const fs = require('fs');
const path = require('path');

const INPUT_DIR = path.join(__dirname, '../../data/input');

const SUBJECT_META = {
  maths:     { name: 'Mathematics', icon: '📐', color: '#3b82f6' },
  science:   { name: 'Science',     icon: '🔬', color: '#10b981' },
  physics:   { name: 'Physics',     icon: '⚛️',  color: '#8b5cf6' },
  chemistry: { name: 'Chemistry',   icon: '🧪', color: '#f59e0b' },
  biology:   { name: 'Biology',     icon: '🧬', color: '#ef4444' },
};

function naturalSort(a, b) {
  return a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' });
}

function scanCatalog() {
  if (!fs.existsSync(INPUT_DIR)) {
    console.warn('⚠️  data/input directory not found');
    return { grades: [] };
  }

  const gradeDirs = fs.readdirSync(INPUT_DIR)
    .filter(d => d.startsWith('grade') && fs.statSync(path.join(INPUT_DIR, d)).isDirectory())
    .sort(naturalSort);

  const grades = gradeDirs.map(gradeDir => {
    const gradeNum = parseInt(gradeDir.replace('grade', ''), 10);
    const gradePath = path.join(INPUT_DIR, gradeDir);

    const subjectDirs = fs.readdirSync(gradePath)
      .filter(d => fs.statSync(path.join(gradePath, d)).isDirectory())
      .sort(naturalSort);

    const subjects = subjectDirs.map(subjectDir => {
      const subjectKey = subjectDir.toLowerCase();
      const subjectPath = path.join(gradePath, subjectDir);
      const meta = SUBJECT_META[subjectKey] || { name: subjectKey.charAt(0).toUpperCase() + subjectKey.slice(1), icon: '📖', color: '#6b7280' };

      const chapters = [];

      // Check for part subdirectories
      const entries = fs.readdirSync(subjectPath);
      const hasParts = entries.some(e => e.startsWith('part') && fs.statSync(path.join(subjectPath, e)).isDirectory());

      if (hasParts) {
        const partDirs = entries
          .filter(e => e.startsWith('part') && fs.statSync(path.join(subjectPath, e)).isDirectory())
          .sort(naturalSort);

        partDirs.forEach(partDir => {
          const partPath = path.join(subjectPath, partDir);
          const partNum = partDir.replace('part', '');
          const partLabel = `Part ${partNum}`;

          fs.readdirSync(partPath)
            .filter(f => f.endsWith('.pdf'))
            .sort(naturalSort)
            .forEach(file => {
              const match = file.match(/chapter(\d+)/i);
              if (match) {
                chapters.push({
                  number: parseInt(match[1], 10),
                  file,
                  part: partLabel,
                  partNum: parseInt(partNum, 10),
                });
              }
            });
        });
      } else {
        entries
          .filter(f => f.endsWith('.pdf'))
          .sort(naturalSort)
          .forEach(file => {
            const match = file.match(/chapter(\d+)/i);
            if (match) {
              chapters.push({
                number: parseInt(match[1], 10),
                file,
                part: null,
                partNum: null,
              });
            }
          });
      }

      chapters.sort((a, b) => a.number - b.number);

      return {
        key: subjectKey,
        ...meta,
        chapters,
        totalChapters: chapters.length,
        hasParts,
      };
    });

    return {
      grade: gradeNum,
      subjects,
      totalSubjects: subjects.length,
      totalChapters: subjects.reduce((sum, s) => sum + s.totalChapters, 0),
    };
  });

  const summary = {
    totalGrades: grades.length,
    totalSubjects: grades.reduce((sum, g) => sum + g.totalSubjects, 0),
    totalChapters: grades.reduce((sum, g) => sum + g.totalChapters, 0),
  };

  return { grades, summary };
}

// Cache the catalog at module load
let _catalog = null;

function getCatalog() {
  if (!_catalog) {
    _catalog = scanCatalog();
    console.log(`📂 Catalog loaded: ${_catalog.summary.totalGrades} grades, ${_catalog.summary.totalSubjects} subjects, ${_catalog.summary.totalChapters} chapters`);
  }
  return _catalog;
}

function refreshCatalog() {
  _catalog = null;
  return getCatalog();
}

module.exports = { getCatalog, refreshCatalog, SUBJECT_META };
