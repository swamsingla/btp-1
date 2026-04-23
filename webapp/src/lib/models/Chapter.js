import mongoose from 'mongoose';

const ChapterSchema = new mongoose.Schema({
  title: { type: String, required: true },
  subject: { type: String, required: true, index: true },
  grade: { type: Number, required: true, index: true },
  chapter: { type: Number, required: true },
  part: { type: Number, default: null },
  language: { type: String, default: 'en' },
  model: String,
  summary: String,
  translations: { type: mongoose.Schema.Types.Mixed, default: {} },
  topicCount: Number,
}, { timestamps: true });

ChapterSchema.index({ grade: 1, subject: 1, chapter: 1, part: 1 }, { unique: true });

export default mongoose.models.Chapter || mongoose.model('Chapter', ChapterSchema);
