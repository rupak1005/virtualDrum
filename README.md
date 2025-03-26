# 🥁 Virtual Drum Kit using OpenCV & Pygame

This project is an **AI-powered Virtual Drum Kit** that uses **OpenCV for hand tracking** and **Pygame for real-time sound playback**. Users can play a virtual drum set using hand gestures, creating a fun and interactive drumming experience.

## 🛠️ **Technologies Used**
- **Python**
- **OpenCV** (for hand tracking and gesture recognition)
- **Mediapipe** (for efficient hand detection)
- **Pygame** (for real-time drum sound playback)
- **NumPy** (for fast mathematical operations)

## 🚀 **Features**
✅ **Hand Tracking-Based Drum Kit** – Uses AI to recognize hand positions  
✅ **Real-time Sound Effects** – Plays drum sounds instantly with gestures  
✅ **Smooth UI & Drum Visualization** – Displays drum pads and active hits  
✅ **Gesture-Based Control** – Tap on virtual drums to play beats  
✅ **Customizable Sounds** – Replace default drum samples with custom ones  

## 🔧 **Installation & Setup**
To run the Virtual Drum Kit on your local machine:

1. **Clone this repository:**
   ```sh
   git clone https://github.com/rupak1005/virtualDrum.git
   ```
2. **Navigate to the project folder:**
   ```sh
   cd virtualDrum
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Virtual Drum Kit:**
   ```sh
   python virtualDrumKit.py
   ```

## 🥁 **How It Works**
1. **Camera detects hand movements** using OpenCV & Mediapipe.
2. **Finger positions** are tracked to determine which drum is hit.
3. The corresponding **drum sound** is played using Pygame.
4. **Drum visuals** update dynamically based on hand movements.

## 📂 **Folder Structure**
```
virtualDrum/
│── models/
│   ├── hand_tracking_model.xml
│── sounds/
│   ├── snare.wav
│   ├── kick.wav
│   ├── hi_hat.wav
│── assets/
│   ├── drum_ui.png
│── virtualDrumKit.py
│── requirements.txt
│── README.md
```

## 🤝 **Contributing**
We welcome contributions! 🛠️
1. Fork the repository 🍴
2. Create a new branch: `git checkout -b feature-new-drum-effect`
3. Commit your changes: `git commit -m "Added new drum sound"`
4. Push to your fork and create a Pull Request

## ⚡ **Resources**
- [Mediapipe Hand Tracking](https://developers.google.com/mediapipe/solutions/vision/hand_tracking)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [OpenCV Python Docs](https://docs.opencv.org/master/)

## 📜 **License**
This project is licensed under the **MIT License**. Feel free to use and modify it! 🚀

---

🥁 **Star this repo** if you like it! ⭐  
🎶 Have fun drumming with AI! 🔥

