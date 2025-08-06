"""
01_read_display.py
-------------------
This script demonstrates how to read and display:
1. Images
2. Video files
3. Live webcam feed
using OpenCV in Python.

Author: Your Name
"""

import cv2

# ------------------------------
# 1. READ AND DISPLAY AN IMAGE
# ------------------------------
def display_image(image_path):
    """
    Reads and displays an image using OpenCV.

    Args:
        image_path (str): Path to the image file.
    """
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    cv2.imshow('Image Window', img)

    # Wait for any key press (0 means wait indefinitely)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ------------------------------
# 2. READ AND DISPLAY A VIDEO
# ------------------------------
def display_video(video_path):
    """
    Reads and displays a video file frame by frame.

    Args:
        video_path (str): Path to the video file.
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Video file cannot be opened!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video Window', frame)

        # Press 'q' to quit early
        if cv2.waitKey(20)
