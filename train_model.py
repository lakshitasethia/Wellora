import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv('heart.csv.xls')

# Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# Train-test split (optional, here we just train on whole data for the project)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Save the model
with open('heart_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("Model trained and saved as heart_model.pkl")
