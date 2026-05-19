import librosa
import numpy as np

def extract_features(file_path):
    try:
        # Load audio
        y, sr = librosa.load(file_path)

        # Pitch
        pitches, _ = librosa.piptrack(y=y, sr=sr)
        pitch = pitches[pitches > 0]
        mean_pitch = np.mean(pitch) if len(pitch) > 0 else 0

        # Intensity
        intensity = np.mean(librosa.feature.rms(y=y))

        # MFCC (13 features)
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)

        # Return as single list
        return [mean_pitch, intensity] + list(mfcc)

    except Exception as e:
        print("Error processing file:", file_path, e)
        return None
