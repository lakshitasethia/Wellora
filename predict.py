import sys
import json
import pickle
import pandas as pd
import warnings
import os

# Suppress warnings from scikit-learn
warnings.filterwarnings("ignore")

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No input provided"}))
        return

    try:
        # Load the input JSON
        input_data = json.loads(sys.argv[1])
        
        # Define expected columns based on training data
        expected_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        
        # Extract features (defaulting to 0 for missing ones, though Gemini should extract all or we use defaults)
        features = {}
        for col in expected_cols:
            # Handle possible type issues, convert to float
            val = input_data.get(col, 0)
            if val is None or val == "":
                val = 0
            features[col] = [float(val)]
            
        df = pd.DataFrame(features)

        # Load the model relative to the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(script_dir, 'heart_model.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        # Predict
        prediction = model.predict(df)[0]
        
        # Output result as JSON
        print(json.dumps({"prediction": int(prediction), "success": True}))

    except Exception as e:
        print(json.dumps({"error": str(e), "success": False}))

if __name__ == "__main__":
    main()
