Adaptive Robot Voice Behavior for Enhancing User Comfort and Trust

Project Status: This project is currently under active development at Manipal University Jaipur. Research, experimentation, and user studies are ongoing.

Overview

This project explores how variations in a robot's voice tone affect human perception, particularly in terms of comfort and trust during Human-Robot Interaction (HRI).

Using the RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song) dataset, the system extracts acoustic features such as:

Pitch (Fundamental Frequency)
Intensity (Energy)
MFCCs (Mel-Frequency Cepstral Coefficients)

These features are used to train a Random Forest Classifier that predicts emotions from speech.

The long-term goal is to build a robotic system capable of adapting its voice tone to improve interaction quality.

Objectives
Analyze emotional speech characteristics
Extract meaningful acoustic features
Train a machine learning model for emotion classification
Evaluate model performance using accuracy and confusion matrix
Study how different voice tones influence user comfort and trust
Emotions Used

The current implementation focuses on the following emotions:

Neutral
Calm
Happy
Angry

Tech Stack
Python
Librosa
Scikit-learn
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook
Dataset
RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)

Features Implemented
Audio preprocessing
Feature extraction (Pitch, Intensity, MFCCs)
CSV dataset generation
Random Forest model training
Emotion prediction
Confidence score output
Confusion matrix visualization
Acoustic feature analysis
Preliminary Results
Model Accuracy: ~75%
Strong performance on Happy and Angry
Common confusion between Calm and Neutral
Visualizations

The project currently includes:

Mean Pitch per Emotion
Mean Intensity per Emotion
Confusion Matrix

How to Run
1. Clone the Repository
git clone https://github.com/AlishaTandon25/adaptive-robot-voice-behavior.git
cd adaptive-robot-voice-behavior
2. Install Dependencies
pip install -r requirements.txt
3. Run the Project
python main.py

Current Progress
Literature review completed
Feature extraction pipeline implemented
Machine learning model trained
Preliminary analysis and results obtained
Progress report prepared
User study design in progress
Final research paper under development
Real-time robot integration planned

Future Work
Improve model accuracy using deep learning (CNN/LSTM)
Conduct user perception studies
Integrate with robotic platforms
Implement real-time adaptive voice modulation
Expand to additional emotions

References
Livingstone, S. R., & Russo, F. A. (2018). RAVDESS Dataset.
Emotional Speech Recognition using Machine Learning.
Quatieri, T. F. (2002). Discrete-Time Speech Signal Processing.
Human-Robot Interaction studies on trust and comfort.

Author

Alisha Tandon
B.Tech Computer Science and Engineering
Manipal University Jaipur

License

This project is developed for academic and research purposes.
