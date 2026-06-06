from camera import detect
from alert import trigger_alert
import cv2
import time
import os

cap = cv2.VideoCapture(0)

if not os.path.exists("detections"):
    os.makedirs("detections")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, detected = detect(frame)

    if detected:
        trigger_alert("Object")
        cv2.imwrite(f"detections/{int(time.time())}.jpg", frame)

    cv2.imshow("Smart Edge AI Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
