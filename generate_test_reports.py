from PIL import Image, ImageDraw, ImageFont
import os

def create_report(filename, patient_info, metrics):
    img = Image.new('RGB', (800, 600), color='white')
    d = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("Arial.ttf", 36)
        font_text = ImageFont.truetype("Arial.ttf", 20)
    except:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()

    text_lines = [
        "LIFELINE HEALTHCARE - CARDIAC DIAGNOSTIC REPORT",
        "--------------------------------------------------",
        f"Patient Name: {patient_info['name']}",
        f"Date: {patient_info['date']}",
        "",
        f"Age: {metrics['age']} years",
        f"Sex: {metrics['sex']}",
        f"Chest Pain Type (cp): {metrics['cp']}",
        f"Resting Blood Pressure (trestbps): {metrics['trestbps']} mmHg",
        f"Serum Cholesterol (chol): {metrics['chol']} mg/dl",
        f"Fasting Blood Sugar (fbs): {metrics['fbs']}",
        f"Resting Electrocardiographic Results (restecg): {metrics['restecg']}",
        f"Maximum Heart Rate Achieved (thalach): {metrics['thalach']} bpm",
        f"Exercise Induced Angina (exang): {metrics['exang']}",
        f"ST Depression Induced by Exercise (oldpeak): {metrics['oldpeak']}",
        f"Slope of the Peak Exercise ST Segment (slope): {metrics['slope']}",
        f"Number of Major Vessels (ca): {metrics['ca']}",
        f"Thalassemia (thal): {metrics['thal']}",
        "",
        "End of Report. Please consult your physician."
    ]

    y_text = 40
    for i, line in enumerate(text_lines):
        font = font_title if i == 0 else font_text
        d.text((40, y_text), line, fill=(0, 0, 0), font=font)
        y_text += 40 if i == 0 else 25

    img.save(filename)
    print(f"Successfully generated {filename}")

# Report 1: High Risk
create_report('report_high_risk.png', 
    {"name": "John Doe", "date": "October 24, 2026"},
    {"age": "65", "sex": "Male", "cp": "3", "trestbps": "160", "chol": "280", "fbs": "> 120 mg/dl (1)", "restecg": "2", "thalach": "120", "exang": "1 (True)", "oldpeak": "2.5", "slope": "1", "ca": "2", "thal": "3"}
)

# Report 2: Low Risk (Healthy)
create_report('report_low_risk.png', 
    {"name": "Alice Smith", "date": "October 25, 2026"},
    {"age": "34", "sex": "Female", "cp": "0", "trestbps": "110", "chol": "180", "fbs": "< 120 mg/dl (0)", "restecg": "0", "thalach": "170", "exang": "0 (False)", "oldpeak": "0.0", "slope": "2", "ca": "0", "thal": "2"}
)

# Report 3: Borderline
create_report('report_borderline.png', 
    {"name": "Robert Brown", "date": "October 26, 2026"},
    {"age": "54", "sex": "Male", "cp": "1", "trestbps": "130", "chol": "240", "fbs": "< 120 mg/dl (0)", "restecg": "1", "thalach": "145", "exang": "0 (False)", "oldpeak": "1.0", "slope": "1", "ca": "1", "thal": "2"}
)

# Report 4: Moderate Risk
create_report('report_moderate_risk.png', 
    {"name": "Emily Davis", "date": "October 27, 2026"},
    {"age": "58", "sex": "Female", "cp": "2", "trestbps": "140", "chol": "260", "fbs": "> 120 mg/dl (1)", "restecg": "0", "thalach": "150", "exang": "1 (True)", "oldpeak": "1.8", "slope": "1", "ca": "1", "thal": "3"}
)

# Report 5: Low Risk 2
create_report('report_low_risk_2.png', 
    {"name": "Michael Wilson", "date": "October 28, 2026"},
    {"age": "45", "sex": "Male", "cp": "1", "trestbps": "120", "chol": "200", "fbs": "< 120 mg/dl (0)", "restecg": "0", "thalach": "165", "exang": "0 (False)", "oldpeak": "0.5", "slope": "2", "ca": "0", "thal": "2"}
)

# Report 6: Severe Risk
create_report('report_severe_risk.png', 
    {"name": "David Miller", "date": "October 29, 2026"},
    {"age": "70", "sex": "Male", "cp": "3", "trestbps": "180", "chol": "320", "fbs": "> 120 mg/dl (1)", "restecg": "2", "thalach": "100", "exang": "1 (True)", "oldpeak": "3.5", "slope": "1", "ca": "3", "thal": "3"}
)
