import os
import joblib
import pandas as pd
from feature_extractor import extract_features

# 📌 Paths
MODEL_PATH = "E:/2nd year/research/model.pkl"
AUDIO_FOLDER = "E:/2nd year/research/audios"

# 🎯 Emotion mapping
emotion_map = {
    "01": "Neutral",
    "02": "Calm",
    "03": "Happy",
    "05": "Angry"
}

# =========================
# 🔹 OPTION 1: Train Model
# =========================
def train_model():
    print("\n👉 Training model...")

    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

    df = pd.read_csv("ravdess_features.csv")

    X = df.drop("emotion", axis=1)
    y = df["emotion"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\n✅ Model trained! Accuracy: {accuracy:.2f}")

    joblib.dump(model, MODEL_PATH)
    print("📁 Model saved!")

# =========================
# 🔹 OPTION 2: Predict Emotion
# =========================
def predict_audio():
    print("\n👉 Available audio files:\n")

    files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith(".mp3")]

    if not files:
        print("No audio files found!")
        return

    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

    try:
        choice = int(input("\nSelect file number: "))
        selected_file = files[choice - 1]
    except:
        print("Invalid choice!")
        return

    file_path = os.path.join(AUDIO_FOLDER, selected_file)

    print(f"\nSelected: {selected_file}")

    # Load model
    if not os.path.exists(MODEL_PATH):
        print("❌ Model not found. Train model first.")
        return

    model = joblib.load(MODEL_PATH)

    # Extract features
    features = extract_features(file_path)

    if features:
        feature_names = ["pitch", "intensity"] + [f"mfcc_{i}" for i in range(13)]
        features_df = pd.DataFrame([features], columns=feature_names)

        prediction = model.predict(features_df)[0]

        emotion = emotion_map.get(str(prediction).zfill(2), "Unknown")

        print("\n🎯 Predicted Emotion:", emotion)

# =========================
# 🔹 MAIN MENU
# =========================
def main():
    while True:
        print("\n===== Emotion Recognition System =====")
        print("1. Train Model")
        print("2. Predict Emotion from Audio")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            train_model()

        elif choice == "2":
            predict_audio()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

# Run program
if __name__ == "__main__":
    main()
