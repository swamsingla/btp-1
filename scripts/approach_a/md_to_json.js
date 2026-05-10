#!/usr/bin/env node
/**
 * Convert Qwen3 markdown topic files into the JSON format
 * expected by the NCERT Smart Wiki UI.
 *
 * Input:  output/qwen3/*.md  +  output/qwen3/_index.json
 * Output: data/generated/grade{N}/{subject}/chapter{N}/en.json
 *
 * The UI expects:
 * {
 *   title: "Chapter 1: SETS",
 *   subject: "Mathematics",
 *   grade: 11,
 *   chapter: 1,
 *   language: "en",
 *   status: "ready",
 *   summary: "...",
 *   topics: [
 *     { id: 1, title: "...", content: "<html>...", subtopics: [] },
 *     ...
 *   ]
 * }
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const QWEN_DIR = path.join(ROOT, 'output', 'qwen3');
const INDEX_FILE = path.join(QWEN_DIR, '_index.json');

// ── Markdown → HTML (lightweight, no external deps) ─────────

function mdToHtml(md) {
  let html = md;

  // Escape HTML entities first (but preserve our own tags later)
  // Actually we do NOT escape since we want the markdown converted.

  // Display math: $$ ... $$  →  keep as-is for KaTeX auto-render
  // We just need to make sure they're on their own paragraph.
  html = html.replace(/\$\$([\s\S]*?)\$\$/g, (_, eq) => {
    return `<div class="math-display">$$${eq.trim()}$$</div>`;
  });

  // Inline math: $ ... $  →  keep as-is for KaTeX

  // Headers: ### → <h3>, #### → <h4>  (within topic content, not top-level)
  html = html.replace(/^####\s+(.+)$/gm, '<h4>$1</h4>');
  html = html.replace(/^###\s+\*\*(.+?)\*\*$/gm, '<h3>$1</h3>');
  html = html.replace(/^###\s+(.+)$/gm, '<h3>$1</h3>');

  // Bold: **text** → <strong>text</strong>
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

  // Italic: *text* → <em>text</em>
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

  // Blockquote: > text → <blockquote>
  html = html.replace(/^>\s*(.+)$/gm, '<blockquote>$1</blockquote>');
  // Merge adjacent blockquotes
  html = html.replace(/<\/blockquote>\n<blockquote>/g, '<br/>');

  // Unordered list items: - text
  html = html.replace(/^(\s*)- (.+)$/gm, '$1<li>$2</li>');

  // Ordered list items: 1. text
  html = html.replace(/^\d+\.\s+(.+)$/gm, '<li>$1</li>');

  // Wrap consecutive <li> in <ul>
  html = html.replace(/((?:<li>.*<\/li>\n?)+)/g, (match) => {
    return '<ul>' + match.trim() + '</ul>';
  });

  // Code blocks: ```...```
  html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => {
    return `<pre><code class="language-${lang}">${code.trim()}</code></pre>`;
  });

  // Inline code: `text`
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

  // Horizontal rule: ---
  html = html.replace(/^---$/gm, '<hr/>');

  // Paragraphs: wrap non-tag lines
  const lines = html.split('\n');
  const result = [];
  let inBlock = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();

    if (!line) {
      result.push('');
      continue;
    }

    // Skip lines that are already HTML tags
    if (line.startsWith('<')) {
      result.push(line);
      continue;
    }

    // Wrap plain text in <p>
    result.push(`<p>${line}</p>`);
  }

  html = result.join('\n');

  // Clean up empty paragraphs
  html = html.replace(/<p><\/p>/g, '');

  // Clean up double newlines
  html = html.replace(/\n{3,}/g, '\n\n');

  return html.trim();
}

// ── Parse a single markdown file into topic sections ────────

function parseMarkdownFile(mdContent) {
  const lines = mdContent.split('\n');
  const sections = {};
  let currentSection = null;
  let currentLines = [];
  let title = '';
  let meta = '';

  for (const line of lines) {
    // Top-level title: # 1.1 Introduction
    if (line.match(/^# \d/)) {
      title = line.replace(/^# /, '').trim();
      continue;
    }

    // Grade/chapter meta: > **Grade 11** | **Chapter 1: SETS**
    if (line.match(/^>\s*\*\*Grade/)) {
      meta = line;
      continue;
    }

    // Section headers: ## Introduction, ## Explanation, etc.
    if (line.match(/^## /)) {
      if (currentSection) {
        sections[currentSection] = currentLines.join('\n').trim();
      }
      currentSection = line.replace(/^## /, '').trim();
      currentLines = [];
      continue;
    }

    if (currentSection) {
      currentLines.push(line);
    }
  }

  if (currentSection) {
    sections[currentSection] = currentLines.join('\n').trim();
  }

  return { title, meta, sections };
}

// ── Build subtopics from explanation section ────────────────

function buildSubtopics(explanationHtml) {
  // Split by <h3> tags to create subtopics
  const parts = explanationHtml.split(/<h3>(.*?)<\/h3>/);
  const subtopics = [];

  // First part is intro text before any h3
  let mainContent = parts[0] || '';

  for (let i = 1; i < parts.length; i += 2) {
    const subTitle = parts[i];
    const subContent = parts[i + 1] || '';
    subtopics.push({
      title: subTitle.replace(/<[^>]*>/g, '').trim(),
      content: subContent.trim(),
    });
  }

  return { mainContent: mainContent.trim(), subtopics };
}

// ── Main conversion ─────────────────────────────────────────

function convert() {
  // Read index
  const index = JSON.parse(fs.readFileSync(INDEX_FILE, 'utf-8'));
  const { model, grade, chapter_number, chapter_title, topics: topicsMeta } = index;

  // Build topics array for the UI
  const topics = [];

  for (let i = 0; i < topicsMeta.length; i++) {
    const tm = topicsMeta[i];
    const mdPath = path.join(QWEN_DIR, tm.file);

    if (!fs.existsSync(mdPath)) {
      console.warn(`⚠️  Missing file: ${tm.file}`);
      continue;
    }

    const mdContent = fs.readFileSync(mdPath, 'utf-8');
    const parsed = parseMarkdownFile(mdContent);

    // Build HTML content from all sections
    const contentParts = [];

    // Introduction
    if (parsed.sections['Introduction']) {
      contentParts.push(mdToHtml(parsed.sections['Introduction']));
    }

    // Explanation (main content)
    if (parsed.sections['Explanation']) {
      const expHtml = mdToHtml(parsed.sections['Explanation']);
      contentParts.push(expHtml);
    }

    // Solved Examples
    if (parsed.sections['Solved Examples']) {
      contentParts.push('<h3>📝 Solved Examples</h3>');
      contentParts.push(mdToHtml(parsed.sections['Solved Examples']));
    }

    // Practice Problems
    if (parsed.sections['Practice Problems']) {
      contentParts.push('<h3>✏️ Practice Problems</h3>');
      contentParts.push(mdToHtml(parsed.sections['Practice Problems']));
    }

    // Summary
    if (parsed.sections['Summary']) {
      contentParts.push('<h3>📋 Summary</h3>');
      contentParts.push(mdToHtml(parsed.sections['Summary']));
    }

    // Student Corner
    if (parsed.sections['Student Corner']) {
      contentParts.push('<h3>🎓 Student Corner</h3>');
      contentParts.push(mdToHtml(parsed.sections['Student Corner']));
    }

    const fullContent = contentParts.join('\n');

    // Extract subtopics from the explanation for sidebar rendering
    const subtopics = [];

    topics.push({
      id: i + 1,
      title: tm.topic_title,
      topicNumber: tm.topic_number,
      content: fullContent,
      subtopics,
    });
  }

  // Compose the summary from the Introduction topic
  const introTopic = topicsMeta.find(t => t.topic_title === 'Introduction');
  let summary = '';
  if (introTopic) {
    const introPath = path.join(QWEN_DIR, introTopic.file);
    if (fs.existsSync(introPath)) {
      const introMd = fs.readFileSync(introPath, 'utf-8');
      const introParsed = parseMarkdownFile(introMd);
      summary = (introParsed.sections['Introduction'] || '')
        .replace(/\*\*/g, '')
        .replace(/\*([^*]+)\*/g, '$1')
        .substring(0, 300);
    }
  }

  // Build the final JSON
  const output = {
    title: `Chapter ${chapter_number}: ${chapter_title}`,
    subject: 'Mathematics',
    grade,
    chapter: chapter_number,
    language: 'en',
    status: 'ready',
    model,
    summary: summary || `Grade ${grade} Mathematics — Chapter ${chapter_number}: ${chapter_title}`,
    topics,
  };

  // Write to data/generated/
  const outDir = path.join(ROOT, 'data', 'generated', `grade${grade}`, 'maths', `chapter${chapter_number}`);
  fs.mkdirSync(outDir, { recursive: true });

  const outPath = path.join(outDir, 'en.json');
  fs.writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf-8');

  console.log(`✅ Generated: ${outPath}`);
  console.log(`   ${topics.length} topics, ${Math.round(JSON.stringify(output).length / 1024)}KB`);
}

convert();
