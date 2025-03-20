import cv2
import torch
import pygame
import numpy as np
from ultralytics import YOLO

# Initialize Pygame mixer for drum sounds
pygame.mixer.init()

drum_sounds = {
    "snare": pygame.mixer.Sound("sounds/snare.wav"),
    "bass": pygame.mixer.Sound("sounds/bass.wav"),
    "hihat": pygame.mixer.Sound("sounds/hihat.wav"),
    "tom": pygame.mixer.Sound("sounds/tom.wav"),
}

# Load YOLOv8 Pose model
model = YOLO("yolov8n-pose.pt")

# Define drum zones (x, y, width, height)
drum_zones = {
    "snare": (100, 200, 150, 150),
    "bass": (300, 400, 200, 200),
    "hihat": (500, 200, 150, 150),
    "tom": (700, 300, 180, 180),
}

# Open Webcam
cap = cv2.VideoCapture(0)

def check_drum_hit(hand_x, hand_y):
    """Check if hand is in a drum zone and play sound"""
    for drum, (x, y, w, h) in drum_zones.items():
        if x < hand_x < x + w and y < hand_y < y + h:
            drum_sounds[drum].play()
            return drum
    return None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror effect
    results = model(frame)
    keypoints = results[0].keypoints.xy.cpu().numpy() if results[0].keypoints is not None else []

    if len(keypoints) > 0:
        for kp in keypoints:  # Loop through detected hands
            wrist_x, wrist_y = int(kp[0][0]), int(kp[0][1])  # Wrist point
            check_drum_hit(wrist_x, wrist_y)
            cv2.circle(frame, (wrist_x, wrist_y), 10, (0, 255, 0), -1)  # Draw hand point
    
    # Draw drum zones
    for drum, (x, y, w, h) in drum_zones.items():
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, drum, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    cv2.imshow("Virtual Drum Kit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
