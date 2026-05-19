import librosa
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt   

# 📌 Dataset path
DATASET_PATH = "E:/2nd year/research/data"

# 🎯 Select emotions
# 01 = Neutral, 02 = Calm, 03 = Happy, 05 = Angry
selected_emotions = ["01", "02", "03", "05"]

data = []

print("Starting feature extraction...\n")

# 🔁 Loop through dataset
for actor in os.listdir(DATASET_PATH):
    actor_path = os.path.join(DATASET_PATH, actor)

    if not os.path.isdir(actor_path):
        continue

    print(f"\nProcessing folder: {actor}")

    for file in os.listdir(actor_path):

        if not file.endswith(".wav"):
            continue

        print(f"Processing file: {file}")

        file_path = os.path.join(actor_path, file)

        emotion = file.split("-")[2]

        if emotion not in selected_emotions:
            continue

        try:
            # 🎵 Load audio
            y, sr = librosa.load(file_path)

            # 🎯 Pitch
            pitches, _ = librosa.piptrack(y=y, sr=sr)
            pitch = pitches[pitches > 0]
            mean_pitch = np.mean(pitch) if len(pitch) > 0 else 0

            # 🔊 Intensity
            intensity = np.mean(librosa.feature.rms(y=y))

            # 🎯 MFCC (13 features)
            mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)

            data.append([emotion, mean_pitch, intensity] + list(mfcc))

        except Exception as e:
            print("Error:", file, e)

# 📊 Create DataFrame
columns = ["emotion", "pitch", "intensity"] + [f"mfcc_{i}" for i in range(13)]
df = pd.DataFrame(data, columns=columns)

print("\n✅ Feature extraction completed!\n")
print(df.head())

# 💾 Save CSV
df.to_csv("ravdess_features.csv", index=False)
print("\n📁 CSV saved as ravdess_features.csv")

# 📊 Mean values per emotion
mean_values = df.groupby("emotion").mean()

# 🎯 Map emotion codes to names
emotion_labels = {
    "01": "Neutral",
    "02": "Calm",
    "03": "Happy",
    "05": "Angry"
}

mean_values.index = mean_values.index.map(emotion_labels)

print("\n📊 Mean values per emotion:\n")
print(mean_values)

# 📈 Plot Pitch
plt.figure(figsize=(8,5))
mean_values["pitch"].plot(kind="bar")
plt.title("Mean Pitch per Emotion")
plt.xlabel("Emotion")
plt.ylabel("Pitch")
plt.show()

# 📈 Plot Intensity (FIXED)
plt.figure(figsize=(8,5))
plt.clf()   # <-- clears previous plot

mean_values["intensity"].plot(kind="bar")

plt.title("Mean Intensity per Emotion")
plt.xlabel("Emotion")
plt.ylabel("Intensity")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show(block=True)

for i, v in enumerate(mean_values["intensity"]):
    plt.text(i, v, f"{v:.3f}", ha='center', va='bottom')

    plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
mean_values["pitch"].plot(kind="bar")
plt.title("Pitch")

plt.subplot(1,2,2)
mean_values["intensity"].plot(kind="bar")
plt.title("Intensity")

plt.tight_layout()
plt.show()
