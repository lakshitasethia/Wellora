with open('/Users/akarshaksingh/Desktop/Wellora/server/index.js', 'r') as f:
    text = f.read()

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

const PORT = process.env.PORT || 5001;
"""

text = text.replace("const PORT = process.env.PORT || 5001;", reports_route)

with open('/Users/akarshaksingh/Desktop/Wellora/server/index.js', 'w') as f:
    f.write(text)
