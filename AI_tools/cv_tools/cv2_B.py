
import cv2
video_path = "./case1.mp4"
cap = cv2.VideoCapture(video_path)
print(cap.isOpened())