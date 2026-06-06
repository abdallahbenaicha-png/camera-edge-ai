# camera-edge-ai
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/bb8b59df-38e8-4be0-b558-900cc20bf723" />


                ──────────────────────┐
                │   Camera Module      │
                │ (Raspberry Pi Cam)   │
                └─────────┬────────────┘
                          │ frames
                          v
                ┌──────────────────────┐
                │  Edge Device AI      │
                │ Raspberry Pi / Jetson│
                │                      │
                │  OpenCV Capture      │
                │  YOLOv8 Detection    │
                └───────┬───────┬─────┘
                        │       │
        detection yes   │       │ no detection
                        v       v
        ┌──────────────────┐   (continue)
        │ Alert System     │
        │ - Save Image     │
        │ - LED / Buzzer   │
        │ - Log Event      │
        └────────┬─────────┘
                 │
                 v
        ┌──────────────────────┐
        │ IoT / Cloud Layer     │
        │ - Firebase / MQTT     │
        │ - Telegram Alert      │
        └──────────────────────┘

                 │
                 v
        ┌──────────────────────┐
        │ Web Dashboard        │
        │ Flask / Node.js      │
        │ Live monitoring      │
        └──────────────────────┘
