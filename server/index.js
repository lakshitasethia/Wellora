require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const multer = require('multer');
const Tesseract = require('tesseract.js');
const path = require('path');
const fs = require('fs');
const axios = require('axios');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const Report = require('./models/Report');
const User = require('./models/User');

const app = express();
app.use(cors());
app.use(express.json());

const JWT_SECRET = process.env.JWT_SECRET || 'wellora_secret_key_123';

// Connect to MongoDB Local Community Server
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/wellora';
mongoose.connect(MONGODB_URI).then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Set up Multer for file uploads
const upload = multer({ dest: 'uploads/' });

const FASTAPI_URL = process.env.FASTAPI_URL || 'http://127.0.0.1:8000';

// --- AUTHENTICATION ROUTES --- //

// Register User
app.post('/api/auth/register', async (req, res) => {
  try {
    const { name, email, password } = req.body;
    
    let user = await User.findOne({ email });
    if (user) {
      return res.status(400).json({ error: 'User already exists' });
    }

    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);

    user = new User({
      name,
      email,
      password: hashedPassword
    });

    await user.save();

    const token = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '1h' });
    res.json({ success: true, token, user: { id: user._id, name: user.name, email: user.email } });
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Server details error' });
  }
});

// Login User
app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await User.findOne({ email });
    if (!user) {
      return res.status(400).json({ error: 'Invalid Credentials' });
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(400).json({ error: 'Invalid Credentials' });
    }

    const token = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '1h' });
    res.json({ success: true, token, user: { id: user._id, name: user.name, email: user.email } });
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Server error' });
  }
});

// --- ML RUNNER ROUTE --- //

app.post('/api/upload-report', upload.single('report'), async (req, res) => {
  try {
    const { symptoms } = req.body;
    const file = req.file;

    if (!file) {
      return res.status(400).json({ error: 'No report file uploaded' });
    }

    console.log('1. Processing OCR...');
    // 1. Run OCR on the image
    const { data: { text } } = await Tesseract.recognize(file.path, 'eng');
    
    console.log('2. Extracting metrics & Running prediction module via FastAPI...');
    // 2. & 3. & 4. Use FastAPI to extract metrics, predict, and frame the diagnosis
    let apiResponse;
    try {
      const response = await axios.post(`${FASTAPI_URL}/process_report`, {
        text: text,
        symptoms: symptoms || ""
      });
      apiResponse = response.data;
    } catch (e) {
      console.error('FastAPI error:', e.message);
      return res.status(500).json({ error: 'Failed to process report via ML API.' });
    }

    const metricsResult = apiResponse.extractedMetrics;
    const prediction = apiResponse.prediction;
    const finalDiagnosis = apiResponse.diagnosis;

    // 5. Save to MongoDB
    const reportRecord = new Report({
      symptoms,
      ocrText: text,
      extractedMetrics: metricsResult,
      modelPrediction: prediction,
      finalDiagnosis
    });
    await reportRecord.save();

    // Clean up uploaded file
    fs.unlinkSync(file.path);

    res.json({
      success: true,
      extractedMetrics: metricsResult,
      prediction,
      diagnosis: finalDiagnosis
    });

  } catch (error) {
    console.error('Error processing report:', error);
    res.status(500).json({ error: 'Internal server error processing the report' });
  }
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
