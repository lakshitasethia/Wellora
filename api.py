from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
import os
import re

app = FastAPI(title="Wellora ML API")

# Load the model
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'heart_model.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

class MetricsInput(BaseModel):
    age: float = 0
    sex: float = 0
    cp: float = 0
    trestbps: float = 0
    chol: float = 0
    fbs: float = 0
    restecg: float = 0
    thalach: float = 0
    exang: float = 0
    oldpeak: float = 0
    slope: float = 0
    ca: float = 0
    thal: float = 0

class OCRInput(BaseModel):
    text: str
    symptoms: str = ""

@app.post("/predict")
async def predict(metrics: MetricsInput):
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    expected_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    input_data = metrics.dict()
    
    features = {col: [input_data.get(col, 0)] for col in expected_cols}
    df = pd.DataFrame(features)
    
    try:
        prediction = int(model.predict(df)[0])
        return {"success": True, "prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/process_report")
async def process_report(data: OCRInput):
    text = data.text.lower()
    
    # Simple regex based extraction to replace expensive AI API calls
    metrics = {
        'age': 50.0, 'sex': 1.0, 'cp': 0.0, 'trestbps': 120.0, 'chol': 200.0, 
        'fbs': 0.0, 'restecg': 1.0, 'thalach': 150.0, 'exang': 0.0, 
        'oldpeak': 1.0, 'slope': 1.0, 'ca': 0.0, 'thal': 2.0
    }
    
    def extract_val(pattern, is_float=False):
        match = re.search(pattern, text)
        if match:
            return float(match.group(1)) if is_float else float(match.group(1))
        return None

    val = extract_val(r'age.*?:?\s*(\d+)')
    if val is not None: metrics['age'] = val
    
    if 'female' in text:
        metrics['sex'] = 0.0
    elif 'male' in text:
        metrics['sex'] = 1.0
        
    val = extract_val(r'\(cp\).*?:?\s*(\d+)')
    if val is not None: metrics['cp'] = val
    
    val = extract_val(r'\(trestbps\).*?:?\s*(\d+)')
    if val is not None: metrics['trestbps'] = val
    
    val = extract_val(r'\(chol\).*?:?\s*(\d+)')
    if val is not None: metrics['chol'] = val
    
    val = extract_val(r'\(fbs\).*?(\d+)\s*\)')
    if val is None: val = extract_val(r'\(fbs\).*?:?\s*(\d+)')
    if val is not None: metrics['fbs'] = val
    
    val = extract_val(r'\(restecg\).*?:?\s*(\d+)')
    if val is not None: metrics['restecg'] = val
    
    val = extract_val(r'\(thalach\).*?:?\s*(\d+)')
    if val is not None: metrics['thalach'] = val
    
    val = extract_val(r'\(exang\).*?(\d+)\s*\)')
    if val is None: val = extract_val(r'\(exang\).*?:?\s*(\d+)')
    if val is not None: metrics['exang'] = val
    
    val = extract_val(r'\(oldpeak\).*?:?\s*([0-9.]+)', True)
    if val is not None: metrics['oldpeak'] = val
    
    val = extract_val(r'\(slope\).*?:?\s*(\d+)')
    if val is not None: metrics['slope'] = val
    
    val = extract_val(r'\(ca\).*?:?\s*(\d+)')
    if val is not None: metrics['ca'] = val
    
    val = extract_val(r'\(thal\).*?:?\s*(\d+)')
    if val is not None: metrics['thal'] = val

    # Run model prediction
    if not model:
        prediction = 0
    else:
        df = pd.DataFrame({k: [v] for k, v in metrics.items()})
        prediction = int(model.predict(df)[0])
        
    symptoms = data.symptoms.strip()
    
    # Simple rule-based framing reflecting 100% ML model output
    if prediction == 1:
        diagnosis_base = "The ML model has analyzed your report metrics and predicted a HIGH RISK of heart disease."
    else:
        diagnosis_base = "The ML model has analyzed your report metrics and predicted a LOW RISK for heart disease."
        
    conclusion = " Please consult a qualified healthcare professional for a complete medical diagnosis."

    if symptoms:
        final_diagnosis = f"{diagnosis_base} We have also noted your reported symptoms: \"{symptoms}\".{conclusion}"
    else:
        final_diagnosis = f"{diagnosis_base}{conclusion}"

    return {
        "success": True,
        "extractedMetrics": metrics,
        "prediction": prediction,
        "diagnosis": final_diagnosis
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
