import os
import librosa
import soundfile as sf
import tempfile
import pandas as pd
import joblib
from feature_extractor import extract_features

# 📌 Load model
model = joblib.load("E:/2nd year/research/model.pkl")

# 🎯 Emotion mapping
emotion_map = {
    "01": "Neutral",
    "02": "Calm",
    "03": "Happy",
    "05": "Angry"
}

# 📂 Folder with audio files
AUDIO_FOLDER = "E:/2nd year/research/audios"

files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith((".mp3", ".wav"))]

if not files:
    print("No audio files found!")
    exit()

# 🎯 Show options
print("\nAvailable audio files:\n")

for i, file in enumerate(files):
    print(f"{i+1}. {file}")

# 🧠 User input
choice = int(input("\nSelect an audio file (enter number): "))

if choice < 1 or choice > len(files):
    print("Invalid choice!")
    exit()

selected_file = files[choice - 1]
file_path = os.path.join(AUDIO_FOLDER, selected_file)

print(f"\nSelected file: {selected_file}")

# 🔍 Directly use WAV file
features = extract_features(file_path)

if features:
    import pandas as pd

    feature_names = ["pitch", "intensity"] + [f"mfcc_{i}" for i in range(13)]
    features_df = pd.DataFrame([features], columns=feature_names)

    prediction = model.predict(features_df)[0]

    emotion_map = {
        "01": "Neutral",
        "02": "Calm",
        "03": "Happy",
        "05": "Angry"
    }

    emotion = emotion_map.get(str(prediction).zfill(2), "Unknown")

    print("\n🎯 Predicted Emotion:", emotion)
    
probs = model.predict_proba(features_df)[0]
print("Confidence:", max(probs))
