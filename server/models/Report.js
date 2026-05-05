const mongoose = require('mongoose');

const reportSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  symptoms: String,
  ocrText: String,
  extractedMetrics: Object,
  modelPrediction: Number,
  finalDiagnosis: String,
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Report', reportSchema);
