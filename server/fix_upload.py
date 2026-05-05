import re

with open('/Users/akarshaksingh/Desktop/Wellora/server/index.js', 'r') as f:
    text = f.read()

# Replace the signature and MongoDB save
text = text.replace("app.post('/api/upload-report', upload.single('report'), async (req, res) => {", "app.post('/api/upload-report', verifyToken, upload.single('report'), async (req, res) => {")

text = text.replace("""const reportRecord = new Report({
      symptoms,
      ocrText: text,
      extractedMetrics: metricsResult,
      modelPrediction: prediction,
      finalDiagnosis
    });""", """const reportRecord = new Report({
      userId: req.user.id,
      symptoms,
      ocrText: text,
      extractedMetrics: metricsResult,
      modelPrediction: prediction,
      finalDiagnosis
    });""")

reports_route = """
// --- FETCH REPORTS ROUTE --- //
app.get('/api/reports', verifyToken, async (req, res) => {
  try {
    const reports = await Report.find({ userId: req.user.id }).sort({ createdAt: 1 });
    res.json({ success: true, reports });
  } catch (error) {
    console.error('Error fetching reports:', error);
    res.status(500).json({ error: 'Failed to fetch reports' });
  }
});

// --- SERVER INITIALIZATION --- //
"""
text = text.replace("// --- SERVER INITIALIZATION --- //", reports_route)

with open('/Users/akarshaksingh/Desktop/Wellora/server/index.js', 'w') as f:
    f.write(text)
