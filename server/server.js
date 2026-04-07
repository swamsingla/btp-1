/**
 * NCERT Smart Wiki — Express Server
 * Main entry point for the API server.
 */

const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const path = require('path');
require('dotenv').config();

const catalogRoutes = require('./routes/catalog');
const contentRoutes = require('./routes/content');
const searchRoutes = require('./routes/search');

const app = express();
const PORT = process.env.PORT || 5000;

// ── Middleware ──────────────────────────────────────────────
app.use(cors());
app.use(morgan('dev'));
app.use(express.json());

// ── API Routes ─────────────────────────────────────────────
app.use('/api/catalog', catalogRoutes);
app.use('/api/content', contentRoutes);
app.use('/api/search', searchRoutes);

// ── Serve React build in production ────────────────────────
if (process.env.NODE_ENV === 'production') {
  app.use(express.static(path.join(__dirname, '../client/dist')));
  app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../client/dist/index.html'));
  });
}

// ── Health check ───────────────────────────────────────────
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// ── Start ──────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`\n📚 NCERT Smart Wiki API running on http://localhost:${PORT}`);
  console.log(`   Environment: ${process.env.NODE_ENV || 'development'}\n`);
});

module.exports = app;
