Description:
This project implements a real-time vehicle detection and counting system using OpenCV in Python. The program detects vehicles in a video, tracks their movement, and counts the number of vehicles crossing a predefined line.

Requirements:
Python 3.x
OpenCV (cv2)
NumPy (numpy)

To install the required libraries, run:
pip install opencv-python opencv-contrib-python numpy

Setup
Ensure you have a video file named video.mp4 in the project directory or update the video_path variable with the correct file path.
Adjust the parameters as needed:
largura_min: Minimum width of a detected vehicle.
altura_min: Minimum height of a detected vehicle.
pos_linha: Position of the counting line.
delay: Frames per second for video playback.

How to Run
Save the code in a Python file, e.g., vehicle_counter.py.

Run the script:
python vehicle_counter.py
The program will:

Load the video.
Detect and count vehicles crossing the counting line.
Display the results in real-time.
Press the Esc key to exit the program
