import mongoose from 'mongoose';

const TopicSchema = new mongoose.Schema({
  chapterId: { type: mongoose.Schema.Types.ObjectId, ref: 'Chapter', required: true },
  title: { type: String, required: true },
  topicNumber: { type: String, required: true },
  importance: { type: Number, default: 3 },
  content: { type: String, required: true },
  searchText: { type: String },
  headings: { type: String },
  translations: { type: mongoose.Schema.Types.Mixed, default: {} },
  grade: { type: Number, required: true, index: true },
  subject: { type: String, required: true, index: true },
  chapter: { type: Number, required: true },
  part: { type: Number, default: null },
  order: { type: Number, required: true },
}, { timestamps: true });

TopicSchema.index({ grade: 1, subject: 1, chapter: 1, order: 1 });

export default mongoose.models.Topic || mongoose.model('Topic', TopicSchema);
