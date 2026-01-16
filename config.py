"""
VirtuaMouse Configuration File
Customize settings here to adjust behavior
"""

# Camera Settings
CAMERA_INDEX = 0  # Change to 1 or 2 if default camera doesn't work
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# Mouse Control Settings
MOUSE_SMOOTHENING = 8  # Higher = smoother but slower (5-15 recommended)
FRAME_REDUCTION = 80  # Border area for mouse control (pixels)

# Gesture Sensitivity
CLICK_DELAY = 0.3  # Cooldown between clicks (seconds)
PINCH_THRESHOLD_CLOSE = 30  # Distance for drag detection (pixels)
PINCH_THRESHOLD_RELEASE = 45  # Distance to release drag (pixels)

# Click Distance Thresholds
DOUBLE_CLICK_DISTANCE = 20  # Very close fingers
LEFT_CLICK_DISTANCE_MIN = 20  # Minimum distance for left click
LEFT_CLICK_DISTANCE_MAX = 40  # Maximum distance for left click
RIGHT_CLICK_DISTANCE = 40  # Index + ring finger distance

# Scroll Settings
SCROLL_SENSITIVITY = 10  # Scroll speed (1-20 recommended)
SCROLL_THRESHOLD = 1  # Minimum scroll amount to register

# Volume & Brightness Control
VOLUME_MIN_DISTANCE = 20  # Minimum finger distance (pixels)
VOLUME_MAX_DISTANCE = 200  # Maximum finger distance (pixels)
BRIGHTNESS_MIN_DISTANCE = 20
BRIGHTNESS_MAX_DISTANCE = 200

# Drawing Settings
DRAWING_LINE_THICKNESS = 5  # Thickness of drawn lines
DRAWING_COLOR = (255, 255, 255)  # White (BGR format)
CANVAS_OPACITY = 0.3  # Transparency of drawing overlay (0.0-1.0)

# Display Settings
SHOW_FPS = True
SHOW_INSTRUCTIONS = True
SHOW_DRAW_MODE_STATUS = True
SHOW_HAND_LANDMARKS = True
SHOW_BOUNDING_BOX = True

# Colors (BGR format)
COLOR_FPS = (255, 0, 0)  # Blue
COLOR_INSTRUCTIONS = (0, 255, 0)  # Green
COLOR_DRAW_MODE_ON = (0, 255, 255)  # Yellow
COLOR_DRAW_MODE_OFF = (128, 128, 128)  # Gray
COLOR_LANDMARKS = (255, 0, 255)  # Magenta
COLOR_BBOX = (0, 255, 0)  # Green
COLOR_FRAME_BORDER = (255, 0, 255)  # Magenta

# Hand Detection Settings
MAX_HANDS = 2  # Maximum number of hands to detect (1 or 2)

# PyAutoGUI Settings
PYAUTOGUI_FAILSAFE = True  # Move to top-left corner to stop
PYAUTOGUI_PAUSE = 0.01  # Pause between PyAutoGUI commands (seconds)

# Keyboard Launcher Settings
LAUNCHER_HOTKEY = 'ctrl+alt+m'  # Hotkey to launch VirtuaMouse
LAUNCHER_QUIT_HOTKEY = 'ctrl+alt+q'  # Hotkey to quit launcher

# Model Path
MODEL_PATH = "models/hand_landmarker.task"

# Application Settings
WINDOW_NAME = "VirtuaMouse - Gesture Control System"
QUIT_KEY = 'q'  # Key to quit application

# Performance Settings
ENABLE_MULTIPROCESSING = False  # Experimental: Use multiprocessing (may cause issues)

# Debug Settings
DEBUG_MODE = True  # Print debug information - ENABLED TO FIND NOTEPAD ISSUE
SHOW_GESTURE_INFO = False  # Show detected gestures on screen
