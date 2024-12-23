# Face Detection and Image Capture System

## Project Overview:
This project implements a simple face detection system using OpenCV that captures images of a specific person through a webcam. The captured images are then saved to a folder for later use, such as training a facial recognition model.

The system uses Haar Cascade Classifiers to detect faces and stores the images in a structured dataset folder. Each image is resized to a consistent size of 130x100 pixels, and the images are stored in a sub-folder named after the person.

## Features:
- Real-time face detection using webcam feed.
- Saves images of detected faces into a designated directory.
- Supports multiple people (can create sub-directories for each person).
- The system automatically processes and stores 50 images of a person for training a recognition model.

## Requirements:
- Python 3.x
- OpenCV
- Operating system: Windows (for the `winsound` library)
  
To install the necessary libraries, use the following command:
```bash
pip install opencv-python opencv-contrib-python


##Folder Structure:
datasets/
    └── sintu/
        ├── 1.png
        ├── 2.png
        ├── 3.png
        └── ...
