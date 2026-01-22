# NeuroAI-Research-Lab 

This repository is dedicated to the exploration, experimentation, and research at the intersection of **Neuroscience** and **Artificial Intelligence** (NeuroAI). The primary focus of this lab is to decode neural signals (EEG/fMRI) into machine-understandable information.

---

## Project Portfolio

### 1. EEG Emotion Decoding 
This project aims to classify human emotional states (Positive, Negative, Neutral) from brainwave activity using EEG signal data.

#### Dataset
The dataset consists of EEG brainwave recordings that capture the electrical activity of the brain while subjects experience specific emotional triggers.
- **Source:** Muse EEG Dataset (via Kaggle)
- **Features:** 2,549 features including statistical measures and **FFT (Fast Fourier Transform)** bins.
- **Labels:** 3 Emotional Classes (Neutral, Positive, Negative).

#### Methodology & Technical Stack
- **Preprocessing:** Label Encoding, Column Normalization, and Signal Cleaning.
- **Feature Exploration:** Frequency distribution analysis using FFT to identify neural patterns.
- **Model:** Random Forest Classifier (serving as a robust baseline for high-dimensional data).
- **Architecture:** Implemented using **Object-Oriented Programming (OOP)** principles in Python for scalability.

#### Results & Performance
The model currently achieves an accuracy of **~98%** in distinguishing emotional states on the test set, demonstrating the high separability of neural frequency patterns.

_new projects will be added over time_

---

## Future Research Goals
- Implementation of **Deep Learning** architectures (LSTM/CNN) for raw time-series EEG data.
- Exploring **Brain-Computer Interface (BCI)** for real-time robotic control.

---
