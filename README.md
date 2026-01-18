# VirtuaMouse - Gesture-Based Virtual Mouse 🖐️🖱️

Control your computer using hand gestures! VirtuaMouse uses your webcam and AI-powered hand tracking to convert gestures into mouse actions and system controls.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

### 🖱️ Right Hand - Mouse Control
- **Cursor Movement**: Index finger up
- **Left Click**: Index + middle fingers together
- **Right Click**: Thumb up
- **Double Click**: Index + middle very close
- **Drag & Drop**: Thumb + index pinch
- **Scroll**: Three fingers up (index + middle + ring)
- **Drawing Mode**: Toggle with pinky, draw with index finger

### 🎛️ Left Hand - System Controls
- **Volume Control**: Thumb + index distance
- **Brightness Control**: Thumb + middle distance
- **Open Chrome**: Three fingers up
- **Copy (Ctrl+C)**: Index + pinky
- **Paste (Ctrl+V)**: Index + middle + pinky

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Webcam
- Windows/macOS/Linux

## 📖 Usage

1. Launch the application
2. Position yourself 30-60cm from the camera
3. Use hand gestures to control your computer
4. Press **'Q'** to quit

For detailed gesture instructions, see [GESTURE_REFERENCE.md](GESTURE_REFERENCE.md)

## 🎯 Use Cases

- **Emergency Backup**: When your mouse fails
- **Accessibility**: Hands-free computer control
- **Presentations**: Control slides without touching keyboard
- **Fun**: Futuristic way to interact with your PC


## 📁 Project Structure

```
VirtuaMouse/
├── main.py                  # Main application
├── hand_tracking.py         # Hand detection module
├── gesture_controller.py    # Gesture recognition
├── launcher.py              # Keyboard shortcut launcher
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── models/
│   └── hand_landmarker.task # MediaPipe model
└── utils/
    ├── volume.py           # Volume control
    ├── brightness.py       # Brightness control
    ├── apps.py             # Application launcher
    ├── keyboard_control.py # Keyboard shortcuts
    ├── drawing_board.py    # Drawing functionality
    └── powerpoint_control.py # Presentation controls
```

## 🔧 Troubleshooting

### Camera not working
- Check if camera is connected
- Close other apps using the camera
- Try changing `CAMERA_INDEX` in `config.py`

### Gestures not detected
- Ensure good lighting
- Keep hands within camera frame
- Maintain 30-60cm distance from camera

### Import errors
```bash
pip install -r requirements.txt --upgrade
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking
- [OpenCV](https://opencv.org/) for computer vision
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for system control


## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Made with ❤️ for accessibility and innovation**
