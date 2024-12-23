Overview
The Color Range Detection Tool is a Python-based application that provides an interactive interface for detecting and filtering specific color ranges in images or live camera feeds. It allows users to adjust HSV (Hue, Saturation, Value) values using sliders to isolate and display certain colors. This project leverages OpenCV and Tkinter for image processing and GUI creation, along with the ability to capture and process screenshots.

Technologies Used
Python
Tkinter for the graphical user interface
OpenCV for image processing
Pillow (PIL) for image manipulation
PyAutoGUI for screenshot functionality
Numpy for numerical computations

Prerequisites:
Make sure you have Python installed and the following libraries:
pip install opencv-python  
pip install opencv-python-headless  
pip install pillow  
pip install pyautogui

How to Use
-Run the Script:
python script_name.py  
-Open an Image:
Click the "Open" button to load an image (e.g., input.jpg).
-Adjust HSV Sliders:
Use the sliders to modify low and high values for Hue, Saturation, and Value.
The filtered mask will appear in the HSV display.
-Take a Screenshot:
Click the "Screenshot" button, and follow the instructions to select the area of the screen.
The screenshot will automatically process and display in the GUI.
-Use Color Presets:
Quickly set the HSV sliders to predefined values for detecting reds, greens, or blues by clicking the corresponding buttons.
-Print HSV Ranges:
Click the "Print" button to log the current HSV range to the console.
