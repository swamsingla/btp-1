/**
 * Loads pre-generated content for chapters.
 * Falls back to placeholder content if pipeline hasn't been run yet.
 */

const fs = require('fs');
const path = require('path');

const GENERATED_DIR = path.join(__dirname, '../../data/generated');

const SUBJECT_NAMES = {
  maths: 'Mathematics',
  science: 'Science',
  physics: 'Physics',
  chemistry: 'Chemistry',
  biology: 'Biology',
};

/**
 * Load generated content for a chapter in a given language.
 */
function loadContent(grade, subject, chapter, lang = 'en') {
  const contentPath = path.join(GENERATED_DIR, `grade${grade}`, subject, `chapter${chapter}`, `${lang}.json`);

  if (fs.existsSync(contentPath)) {
    try {
      const raw = fs.readFileSync(contentPath, 'utf-8');
      return JSON.parse(raw);
    } catch (err) {
      console.error(`Error loading content: ${contentPath}`, err.message);
    }
  }

  return getPlaceholder(grade, subject, chapter, lang);
}

function getPlaceholder(grade, subject, chapter, lang) {
  const subjectName = SUBJECT_NAMES[subject] || subject;

  const placeholders = {
    en: {
      title: `Chapter ${chapter}`,
      subject: subjectName,
      grade,
      chapter,
      language: 'en',
      status: 'pending',
      summary: `This is Chapter ${chapter} of ${subjectName} for Grade ${grade}. Content will be available after the generation pipeline is run.`,
      topics: [
        {
          id: 1,
          title: 'Introduction',
          content: `<p>Welcome to Chapter ${chapter} of <strong>${subjectName}</strong> (Grade ${grade}). This content is a placeholder and will be replaced with rich, enriched content once the content generation pipeline is executed.</p><p>To generate content, run:</p><pre><code>python scripts/structure_gen.py\npython scripts/content_gen.py</code></pre>`,
          subtopics: [],
        },
        {
          id: 2,
          title: 'Key Concepts',
          content: `<p>The key concepts for this chapter will include detailed explanations, simplified analogies, and real-world applications — all grounded in the NCERT curriculum.</p><p>Mathematical formulas will be rendered using KaTeX. For example: $E = mc^2$ or the quadratic formula:</p><p>$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$</p>`,
          subtopics: [],
        },
        {
          id: 3,
          title: 'Summary',
          content: `<p>A comprehensive summary of Chapter ${chapter} will appear here after content generation. The content is designed to be pedagogically appropriate for Grade ${grade} students.</p>`,
          subtopics: [],
        },
      ],
    },
    hi: {
      title: `अध्याय ${chapter}`,
      subject: subjectName,
      grade,
      chapter,
      language: 'hi',
      status: 'pending',
      summary: `यह कक्षा ${grade} के ${subjectName} का अध्याय ${chapter} है। सामग्री निर्माण पाइपलाइन चलाने के बाद सामग्री उपलब्ध होगी।`,
      topics: [
        { id: 1, title: 'परिचय', content: `<p>कक्षा ${grade} के <strong>${subjectName}</strong> के अध्याय ${chapter} में आपका स्वागत है। यह सामग्री एक प्लेसहोल्डर है।</p>`, subtopics: [] },
        { id: 2, title: 'मुख्य अवधारणाएँ', content: `<p>इस अध्याय की मुख्य अवधारणाओं में विस्तृत व्याख्या, सरल उपमाएँ और वास्तविक दुनिया के अनुप्रयोग शामिल होंगे। गणितीय सूत्र: $E = mc^2$</p>`, subtopics: [] },
        { id: 3, title: 'सारांश', content: `<p>अध्याय ${chapter} का व्यापक सारांश सामग्री निर्माण के बाद यहाँ दिखाई देगा।</p>`, subtopics: [] },
      ],
    },
    te: {
      title: `అధ్యాయం ${chapter}`,
      subject: subjectName,
      grade,
      chapter,
      language: 'te',
      status: 'pending',
      summary: `ఇది తరగతి ${grade} ${subjectName} అధ్యాయం ${chapter}. కంటెంట్ జనరేషన్ పైప్‌లైన్ అమలు చేసిన తర్వాత కంటెంట్ అందుబాటులో ఉంటుంది.`,
      topics: [
        { id: 1, title: 'పరిచయం', content: `<p>తరగతి ${grade} <strong>${subjectName}</strong> అధ్యాయం ${chapter}కు స్వాగతం. ఇది ప్లేస్‌హోల్డర్ కంటెంట్.</p>`, subtopics: [] },
        { id: 2, title: 'ముఖ్య భావనలు', content: `<p>ఈ అధ్యాయం యొక్క ముఖ్య భావనలు వివరణాత్మక వివరణలు మరియు నిజ-ప్రపంచ అనువర్తనాలను కలిగి ఉంటాయి. $E = mc^2$</p>`, subtopics: [] },
        { id: 3, title: 'సారాంశం', content: `<p>అధ్యాయం ${chapter} యొక్క సమగ్ర సారాంశం కంటెంట్ ఉత్పత్తి తర్వాత ఇక్కడ కనిపిస్తుంది.</p>`, subtopics: [] },
      ],
    },
    or: {
      title: `ଅଧ୍ୟାୟ ${chapter}`,
      subject: subjectName,
      grade,
      chapter,
      language: 'or',
      status: 'pending',
      summary: `ଏହା ଶ୍ରେଣୀ ${grade} ${subjectName} ର ଅଧ୍ୟାୟ ${chapter}। ବିଷୟବସ୍ତୁ ସୃଷ୍ଟି ପାଇପଲାଇନ ଚଲାଇବା ପରେ ବିଷୟବସ୍ତୁ ଉପಲବ୍ଧ ହେବ।`,
      topics: [
        { id: 1, title: 'ପରିଚୟ', content: `<p>ଶ୍ରେଣୀ ${grade} <strong>${subjectName}</strong> ଅଧ୍ୟାୟ ${chapter} କୁ ସ୍ୱାଗତ। ଏହା ଏକ ପ୍ଲେସହୋଲ୍ଡର।</p>`, subtopics: [] },
        { id: 2, title: 'ମୁଖ୍ୟ ଧାରଣା', content: `<p>ଏହି ଅଧ୍ୟାୟର ମୁଖ୍ୟ ଧାରଣାଗୁଡ଼ିକ ବିସ୍ତୃତ ବ୍ୟାଖ୍ୟା ଏବଂ ପ୍ରକୃତ ବିଶ୍ୱ ପ୍ରୟୋଗ ଅନ୍ତର୍ଭୁକ୍ତ ହେବ। $E = mc^2$</p>`, subtopics: [] },
        { id: 3, title: 'ସାରାଂଶ', content: `<p>ଅଧ୍ୟାୟ ${chapter} ର ବ୍ୟାପକ ସାରାଂଶ ବିଷୟବସ୍ତୁ ଉତ୍ପାଦନ ପରେ ଏଠାରେ ଦେଖାଯିବ।</p>`, subtopics: [] },
      ],
    },
  };

  return placeholders[lang] || placeholders.en;
}

module.exports = { loadContent };
