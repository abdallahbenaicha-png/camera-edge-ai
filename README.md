# camera-edge-ai
![Uploading image.png…]()

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
