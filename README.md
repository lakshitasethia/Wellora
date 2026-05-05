# Wellora - Cardiac Diagnostic AI Portal

Wellora is a full-stack, AI-powered health portal designed to analyze medical reports and patient symptoms. It utilizes Optical Character Recognition (OCR) and a localized Machine Learning model to instantly predict a patient's risk of heart disease, saving API token costs while maintaining high accuracy and data privacy.

## 🚀 User Journey / Steps

1. **Sign Up / Log In:** Securely register a new patient account or log into an existing one using your email and password.
2. **Patient Dashboard:** Once authenticated, you will be redirected to your personalized and secure dashboard.
3. **Upload & Describe:** Enter your current medical symptoms into the text box and upload your latest medical report (Image or PDF).
4. **AI Analysis:** Behind the scenes, the system performs OCR to extract 13 critical health metrics (Cholesterol, BP, Fasting Blood Sugar, etc.) from the report and runs them through our ML model.
5. **Instant Diagnosis:** Instantly receive a comprehensive breakdown indicating your risk level (**High Risk** or **Low Risk**) along with a customized medical recommendation.

## 💻 Tech Stack

### Frontend
* **HTML5, CSS3, Vanilla JavaScript:** Clean, responsive, and lightweight user interface.
* **Phosphor Icons:** Modern UI iconography.

### Backend (Node.js)
* **Node.js & Express:** Core REST API Server handling uploads and business logic.
* **MongoDB & Mongoose:** Database for securely storing user credentials and generated report history.
* **JWT & bcryptjs:** Industry-standard secure authentication and password hashing.
* **Tesseract.js:** Server-side Optical Character Recognition (OCR) for reading uploaded health reports.
* **Multer:** Middleware for handling image/PDF file uploads securely.

### Machine Learning API (Python)
* **FastAPI & Uvicorn:** Blazing-fast, lightweight microservice API to process ML transactions locally.
* **Scikit-Learn & Pandas:** Powers the core `heart_model.pkl` to analyze extracted metrics and finalize the prediction.
* **RegEx (NLP):** Extracts precise mathematical health data locally, seamlessly bypassing expensive AI API processing tokens.
