"""
01_read_display.py
-------------------
This script demonstrates how to read and display images, videos, and webcam streams using OpenCV.
"""

import cv2

# -------------------------------
# 1. READ AND DISPLAY AN IMAGE
# -------------------------------
img = cv2.imread('flower.jpg')  # Replace with your image path

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image. Check the file path.")
else:
    cv2.imshow('Image - Flower', img)  # Display image in a window

    cv2.waitKey(0)  # Wait until any key is pressed
    cv2.destroyAllWindows()  # Close all OpenCV windows

# -------------------------------
# 2. READ AND DISPLAY A VIDEO
# -------------------------------
video_path = 'video.mp4'  # Replace with your video path
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    while True:
        ret, frame = cap.read()  # Read one frame at a time
        if not ret:
            break  # Break loop if no frame is returned (end of video)

        cv2.imshow('Video Playback', frame)

        # Press 'q' to exit early
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

cap.release()  # Release video resource
cv2.destroyAllWindows()

# -------------------------------
# 3. READ FROM WEBCAM (LIVE STREAM)
# -------------------------------
cap = cv2.VideoCapture(0)  # 0 means default webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Webcam Live', frame)

        # Press 'q' to quit webcam
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

cap.release()  # Release webcam
cv2.destroyAllWindows()
