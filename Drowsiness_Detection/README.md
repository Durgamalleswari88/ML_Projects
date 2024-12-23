# Drowsiness Detection System

This project implements a **Drowsiness Detection System** using OpenCV, which monitors a user's face and eyes in real-time. If the system detects that the user is drowsy (by identifying no visible eyes), it will alert the user with a sound. This system is designed to run using a webcam for face and eye detection.

---

## Files:

- **drowsiness_detection.py**: Python script that detects drowsiness using OpenCV and plays an alert sound when drowsiness is detected.

---

## Features:

- Real-time face and eye detection using Haar Cascades.
- Drowsiness is detected when no eyes are visible in the webcam feed.
- Alerts the user with a sound if drowsiness is detected.
- Stops the sound once eyes are detected again, and it resets for the next alert.

---

## Installation:

1. Clone or download the project files to your local machine.

2. Install the required libraries:

   ```bash
   pip install opencv-python
   pip install opencv-python-headless
