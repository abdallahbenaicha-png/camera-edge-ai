import cv2
from ultralytics import YOLO
import time
import os

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

if not os.path.exists("detections"):
    os.makedirs("detections")

def detect(frame):
    results = model(frame, verbose=False)

    detected = False

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            if conf > 0.5:
                detected = True

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame,f"{label} {conf:.2f}",
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    return frame, detected


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, detected = detect(frame)

    if detected:
        filename = f"detections/event_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print("🚨 Object detected -> saved image!")

    cv2.imshow("Edge AI Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
