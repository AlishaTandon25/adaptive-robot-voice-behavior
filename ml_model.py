import pandas as pd

# Load dataset
df = pd.read_csv("ravdess_features.csv")

print("Dataset loaded successfully!\n")
print(df.head())

emotion_map = {
    1: "Neutral",
    2: "Calm",
    3: "Happy",
    5: "Angry"
}

df["emotion"] = df["emotion"].map(emotion_map)

from sklearn.model_selection import train_test_split

# 🔥 USE ALL FEATURES NOW (IMPORTANT CHANGE)
X = df.drop("emotion", axis=1)
y = df["emotion"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nData prepared successfully!")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train
model.fit(X_train, y_train)

print("\nModel training completed!")

from sklearn.metrics import accuracy_score

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

from sklearn.metrics import classification_report

print("\nDetailed Report:\n")
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

labels = ["Neutral", "Calm", "Happy", "Angry"]

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=labels,
            yticklabels=labels)

plt.title(f"Confusion Matrix (Accuracy = {accuracy:.2f})")
plt.xlabel("Predicted Emotion")
plt.ylabel("Actual Emotion")

plt.show()

print("\nFeature Importance:")
print(model.feature_importances_)

import joblib

joblib.dump(model, "model.pkl")

print("Model saved successfully!")
