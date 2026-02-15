
# Adaptive Robot Behaviors

## Overview
This project investigates how adaptive robot voice behaviors influence user comfort and trust in Human–Robot Interaction (HRI).

Modern robots are increasingly used in educational, service, and social environments. For smooth and effective interaction, robots must adapt their communication style according to user comfort and contextual needs. Among various adaptive behaviors, vocal tone plays a critical role in shaping user perception.

This study focuses specifically on adaptive voice modulation and its measurable impact on perceived comfort and trust.

---

## Problem Statement
There is limited empirical evidence on how variations in robot voice tone influence user comfort and trust within a controlled sample-based study.

---

## Research Objectives
- Analyze emotional speech characteristics using a validated dataset.
- Extract acoustic features such as pitch (F0), intensity, and spectral properties.
- Map emotional tone variations to robot Text-to-Speech (TTS) systems.
- Conduct a controlled user study measuring comfort and trust.
- Perform statistical analysis to determine significant relationships.

---

## Dataset Used

### RAVDESS – Ryerson Audio-Visual Database of Emotional Speech and Song
Official Source: https://zenodo.org/records/1188976

This dataset provides validated emotional speech recordings used to extract acoustic parameters for modeling adaptive voice behavior.

**Note:** The dataset is not included in this repository due to size and licensing constraints.

---

## Methodology

### 1. Feature Extraction  
- Extract pitch (F0)  
- Analyze pitch variability  
- Measure intensity (amplitude)  
- Extract MFCC features  

### 2. Voice Mapping  
- Map extracted emotional features to robot TTS system  
- Generate controlled tone variations (neutral, calm, firm, etc.)  

### 3. Experimental Study  
- Participants interact with a robot delivering identical scripted instructions.  
- Only variable manipulated: vocal tone.  
- Post-interaction questionnaire measures:
  - Comfort (Likert Scale)
  - Trust (Likert Scale)
  - Naturalness
  - Perceived Warmth

### 4. Statistical Analysis  
- Descriptive statistics  
- ANOVA  
- Correlation analysis  

---

## Current Progress
- Literature review completed.
- RAVDESS dataset explored and analyzed.
- Feature extraction framework designed.
- Experimental design finalized.
- Survey instrument drafted.

---

## Future Work
- Full-scale experimental deployment.
- Real-time adaptive voice implementation.
- Research paper submission.
- Exploration of intellectual property protection for adaptive modeling framework.

---

## Contribution
This project contributes to advancing adaptive communication strategies in Human–Robot Interaction by empirically investigating the role of vocal tone in shaping user comfort and trust.

---

## License
This project is licensed under the MIT License.


