# Facial Recognition System with Real-Time Identification

## Project Overview:
This project implements a real-time facial recognition system using OpenCV and Python. The system can identify known faces from a dataset and classify them accordingly, with an alert for unknown individuals. It uses the **LBPH (Local Binary Patterns Histograms)** algorithm for training and recognizing faces.

The system captures images using a webcam, performs face detection, and uses a pre-trained model to predict the identity of the face in the frame. If the face matches a known person, the system labels it accordingly. Otherwise, it marks the person as "Unknown."

## Features:
- Real-time face detection and recognition using a webcam.
- Training the system with labeled face images.
- Recognition of known faces with confidence scores.
- Alerts for unknown individuals with the option to save the image.
- Integration of **LBPH Face Recognizer** for efficient facial recognition.

## Requirements:
- Python 3.x
- OpenCV
- NumPy
- A webcam for real-time face recognition

To install the necessary libraries, use the following command:
```bash
pip install opencv-python opencv-contrib-python numpy
