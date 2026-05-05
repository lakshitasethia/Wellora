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

months = ["January", "February", "March", "April", "May", "June", "July"]
base_metrics = {"age": "55", "sex": "Male", "cp": "3", "trestbps": "160", "chol": "280", "fbs": "> 120 mg/dl (1)", "restecg": "2", "thalach": "120", "exang": "1 (True)", "oldpeak": "2.5", "slope": "1", "ca": "2", "thal": "3"}

# Let's create a scenario where the patient's health improves over these 7 months
trends = [
    {"trestbps": "165", "chol": "290", "thalach": "115", "oldpeak": "2.8"}, # Jan (Worst)
    {"trestbps": "160", "chol": "280", "thalach": "120", "oldpeak": "2.5"}, # Feb
    {"trestbps": "150", "chol": "260", "thalach": "125", "oldpeak": "2.0"}, # Mar
    {"trestbps": "145", "chol": "240", "thalach": "135", "oldpeak": "1.5", "cp": "2", "fbs": "< 120 mg/dl (0)"}, # Apr (Improvement begins)
    {"trestbps": "135", "chol": "220", "thalach": "145", "oldpeak": "1.0", "cp": "1"}, # May
    {"trestbps": "125", "chol": "200", "thalach": "155", "oldpeak": "0.5", "cp": "0", "exang": "0 (False)", "restecg": "0", "ca": "0"}, # Jun
    {"trestbps": "120", "chol": "180", "thalach": "165", "oldpeak": "0.0", "cp": "0", "exang": "0 (False)", "restecg": "0", "ca": "0", "thal": "2"}  # Jul (Best)
]

for i, month in enumerate(months):
    metrics = base_metrics.copy()
    metrics.update(trends[i])
    create_report(
        f"report_{month.lower()}_2026.png",
        {"name": "John Doe", "date": f"{month} 15, 2026"},
        metrics
    )
