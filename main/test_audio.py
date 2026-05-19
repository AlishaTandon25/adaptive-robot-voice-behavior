from feature_extractor import extract_features
import pandas as pd
import joblib

# Load trained model
model = joblib.load("../model.pkl")

# Test file
file_path = "movie_clip.wav"

features = extract_features(file_path)

if features:
    prediction = model.predict([features])
    print("Predicted Emotion:", prediction)
