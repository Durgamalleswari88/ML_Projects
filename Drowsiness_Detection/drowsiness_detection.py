import cv2
import winsound  # This is for Windows sound alerts. If you're on Linux or Mac, consider using pygame instead.

# Load Haar Cascade files for face and eyes
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start video capture (0 for webcam)
video_capture = cv2.VideoCapture(0)

# Initialize a flag to detect if sound has already been played for a given drowsiness alert
alert_played = False

while True:
    # Capture frame from the webcam
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to grayscale (Haar cascades require grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Detect eyes within the face region
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))

        # If no eyes are detected, assume drowsiness
        if len(eyes) == 0:
            cv2.putText(frame, "DROWSINESS ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Only play sound once per drowsiness detection
            if not alert_played:
                # Play a sound to alert the user (frequency, duration in milliseconds)
                winsound.Beep(1000, 500)  # 1000Hz for 500 milliseconds
                alert_played = True
        else:
            # Draw rectangles around detected eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Reset the alert sound flag when eyes are detected again
            alert_played = False

    # Show the frame with detections
    cv2.imshow("Drowsiness Detection", frame)

    # Break loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
