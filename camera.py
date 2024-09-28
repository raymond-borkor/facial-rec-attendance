import cv2

# Initialize the video capture object
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not access the camera.")
else:
    print("Camera successfully opened!")

# Capture a frame to check if it’s working
# ret, frame = video_capture.read()
# if not ret or frame is None:
#     print("Error: Couldn't read a frame from the camera.")
# else:
#     print("Frame captured successfully!")

ret, frame = video_capture.read()
if not ret or frame is None:
    print("Error: Frame is empty.")
else:
    # Frame is successfully read, proceed with resizing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

# Release the camera and close any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
