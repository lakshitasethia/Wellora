const mongoose = require('mongoose');

const reportSchema = new mongoose.Schema({
  symptoms: String,
  ocrText: String,
  extractedMetrics: Object,
  modelPrediction: Number,
  finalDiagnosis: String,
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Report', reportSchema);
