import librosa
import numpy as np

# Load audio file
file_path = r"C:\Users\HP\PycharmProjects\PythonProject2\audio_file.wav"
y, sr = librosa.load(file_path, sr=None)
print(f"Audio loaded with sampling rate {sr}")

# Extract MFCCs (Mel-frequency cepstral coefficients)
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
print(mfcc.shape)
