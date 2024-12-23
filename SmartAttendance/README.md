# Face Recognition Attendance System

This project demonstrates a face recognition system built using OpenCV and Haar Cascade. The system captures faces through a webcam, recognizes the user, and logs attendance based on face identification.

## Files in this Repository:
1. **`dataset_collection.py`**: Collects face data from the webcam to create a dataset for each person. The images are saved to the `datasets2` folder, which will be used to train the model.
   
2. **`face_recognition_and_attendance.py`**: Trains a face recognition model using the collected dataset and uses the trained model for real-time face recognition. It logs the attendance in a CSV file (`attendance.csv`).

3. **`haarcascade_frontalface_default.xml`**: The Haar Cascade Classifier file used for face detection. This file is required for detecting faces in the webcam feed.

## How to Run:
1. **Step 1**: Collect face data.
   - Run `dataset_collection.py` to capture 50 images of your face using a webcam. These images will be saved to the `datasets2/durga` folder.

2. **Step 2**: Train the model.
   - After collecting the dataset, run `face_recognition_and_attendance.py` to train the face recognition model. The script will recognize faces in real-time, display the webcam feed, and log the attendance in a CSV file.

3. **Step 3**: View Attendance.
   - Check the `attendance.csv` file for the recorded attendance logs, which include the name and the time of face recognition.

## Technologies Used:
- Python
- OpenCV
- NumPy
- Haar Cascade Classifier

## Requirements:
- OpenCV
- NumPy

To install the required libraries:
```bash
pip install opencv-python opencv-contrib-python numpy
