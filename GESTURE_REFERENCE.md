# VirtuaMouse - Gesture Reference Guide

Quick reference for all available gestures in VirtuaMouse.

---

## 🖐️ Right Hand - Mouse Control

### Cursor Movement
**Gesture**: Index finger up ☝️, middle finger down
**Action**: Move mouse cursor
**Tips**: 
- Keep hand within the purple boundary box
- Smooth movements work best
- Adjust `MOUSE_SMOOTHENING` in config.py for sensitivity

### Left Click
**Gesture**: Index ☝️ + Middle 🖕 fingers touch (medium distance)
**Action**: Single left click
**Tips**: 
- Bring fingers close but not too close
- Distance: 20-40 pixels (configurable)
- Wait for cooldown between clicks

### Right Click
**Gesture**: Index ☝️ + Ring 💍 fingers touch
**Action**: Single right click
**Tips**: 
- Touch index and ring finger tips
- Keep middle finger down
- Distance: < 40 pixels (configurable)

### Double Click
**Gesture**: Index ☝️ + Middle 🖕 fingers very close together
**Action**: Double click
**Tips**: 
- Bring fingers very close (< 20 pixels)
- Closer than left click gesture
- Quick pinch motion works well

### Drag & Drop
**Gesture**: Thumb 👍 + Index ☝️ pinch and hold
**Action**: Hold mouse button down (drag)
**Release**: Separate thumb and index finger
**Tips**: 
- Pinch to start dragging
- Move hand while pinched
- Release to drop
- Distance: < 30 pixels to start, > 45 to release

### Scroll
**Gesture**: Three fingers up (Index ☝️ + Middle 🖕 + Ring 💍)
**Action**: Scroll up/down based on hand position
**Tips**: 
- Keep all three fingers extended
- Move hand up to scroll down
- Move hand down to scroll up
- Adjust `SCROLL_SENSITIVITY` in config.py

### Toggle Drawing Mode
**Gesture**: Pinky 🤙 finger up only
**Action**: Enable/disable drawing mode
**Tips**: 
- Only pinky should be up
- Watch for "DRAW MODE: ON/OFF" indicator
- Yellow text = drawing enabled

### Draw
**Gesture**: (In draw mode) Index ☝️ finger up only
**Action**: Draw on screen
**Tips**: 
- Must be in drawing mode first
- Move index finger to draw
- Lower index finger to stop drawing
- Drawings overlay on video

### Clear Drawing
**Gesture**: All five fingers up ✋
**Action**: Clear the drawing canvas
**Tips**: 
- Spread all fingers wide
- Works only in drawing mode
- Instant clear

---

## 🖐️ Left Hand - System Controls

### Volume Control
**Gesture**: Thumb 👍 + Index ☝️ distance
**Action**: Adjust system volume
**Tips**: 
- Close fingers = low volume
- Far apart = high volume
- Distance range: 20-200 pixels
- Real-time adjustment

### Brightness Control
**Gesture**: Thumb 👍 + Middle 🖕 distance
**Action**: Adjust screen brightness
**Tips**: 
- Close fingers = low brightness
- Far apart = high brightness
- Distance range: 20-200 pixels
- May not work on all systems

### Open Chrome
**Gesture**: Three fingers (Index ☝️ + Middle 🖕 + Ring 💍)
**Action**: Launch Google Chrome
**Tips**: 
- Keep thumb and pinky down
- Only works if Chrome is installed
- Cooldown applies

### Open Notepad
**Gesture**: Fist ✊ (all fingers down)
**Action**: Launch Notepad
**Tips**: 
- Close all fingers
- Windows only
- Cooldown applies

### Copy (Ctrl+C)
**Gesture**: Index ☝️ + Pinky 🤙
**Action**: Copy selected text/item
**Tips**: 
- Keep middle and ring down
- Standard copy shortcut
- Cooldown applies

### Paste (Ctrl+V)
**Gesture**: Index ☝️ + Middle 🖕 + Pinky 🤙
**Action**: Paste clipboard content
**Tips**: 
- Three specific fingers up
- Standard paste shortcut
- Cooldown applies

### Start PowerPoint Presentation
**Gesture**: Thumb 👍 only
**Action**: Press F5 (start slideshow)
**Tips**: 
- Only thumb extended
- Works in PowerPoint
- Starts from beginning

### Exit PowerPoint Presentation
**Gesture**: Pinky 🤙 only
**Action**: Press ESC (exit slideshow)
**Tips**: 
- Only pinky extended
- Exits presentation mode
- Returns to edit mode

### Next Slide
**Gesture**: Index ☝️ only
**Action**: Press Right Arrow (next slide)
**Tips**: 
- Only index finger up
- Works in presentation mode
- Also works for media

### Previous Slide
**Gesture**: Index ☝️ + Middle 🖕
**Action**: Press Left Arrow (previous slide)
**Tips**: 
- Two fingers up
- Works in presentation mode
- Also works for media

---

## ⚙️ System Controls

### Quit Application
**Keyboard**: Press 'Q' key
**Action**: Close VirtuaMouse
**Tips**: 
- Quick exit method
- Releases camera
- Closes all windows

### Emergency Exit (Failsafe)
**Mouse**: Move cursor to top-left corner of screen
**Action**: PyAutoGUI emergency stop
**Tips**: 
- Use if gestures malfunction
- Automatic safety feature
- Stops all mouse control

### Launch via Keyboard
**Keyboard**: Ctrl+Alt+M (when launcher is running)
**Action**: Start VirtuaMouse
**Tips**: 
- Run launcher.py first
- Works without mouse
- Emergency access method

---

## 📊 Visual Indicators

### FPS Counter
**Location**: Top-left corner
**Color**: Blue
**Shows**: Frames per second (performance)

### Instructions
**Location**: Below FPS
**Color**: Green
**Shows**: Hand assignments and controls

### Draw Mode Status
**Location**: Below instructions
**Color**: Yellow (ON) / Gray (OFF)
**Shows**: Current drawing mode state

### Purple Boundary Box
**Location**: Center of screen
**Purpose**: Mouse control area
**Tips**: Keep hand inside for cursor control

### Hand Landmarks
**Color**: Magenta dots
**Purpose**: Show detected hand points
**Toggle**: Set `SHOW_HAND_LANDMARKS = False` in config.py

### Bounding Box
**Color**: Green rectangle
**Purpose**: Show hand detection area
**Toggle**: Set `SHOW_BOUNDING_BOX = False` in config.py

---

## 🎯 Tips for Best Performance

### Lighting
- ✅ Use good, even lighting
- ✅ Avoid backlighting
- ✅ Natural light works best
- ❌ Avoid shadows on hands

### Camera Position
- ✅ 30-60 cm from camera
- ✅ Hands clearly visible
- ✅ Neutral background
- ❌ Don't move too fast

### Hand Position
- ✅ Keep hands in frame
- ✅ Face palms toward camera
- ✅ Clear finger separation
- ❌ Don't overlap hands

### Performance
- ✅ Close other applications
- ✅ Use good webcam
- ✅ Adjust smoothing in config
- ❌ Don't use in low light

---

## 🔧 Customization

All gesture thresholds can be adjusted in `config.py`:

```python
# Click distances
DOUBLE_CLICK_DISTANCE = 20
LEFT_CLICK_DISTANCE_MIN = 20
LEFT_CLICK_DISTANCE_MAX = 40
RIGHT_CLICK_DISTANCE = 40

# Drag thresholds
PINCH_THRESHOLD_CLOSE = 30
PINCH_THRESHOLD_RELEASE = 45

# Scroll settings
SCROLL_SENSITIVITY = 10
SCROLL_THRESHOLD = 1

# Mouse smoothing
MOUSE_SMOOTHENING = 8

# Click cooldown
CLICK_DELAY = 0.3
```

---

## 🐛 Troubleshooting

### Gestures Not Detected
1. Check lighting conditions
2. Ensure hands are in frame
3. Verify camera is working
4. Check hand landmarks are visible

### Wrong Gesture Triggered
1. Adjust distance thresholds in config.py
2. Increase CLICK_DELAY for more time between gestures
3. Make gestures more distinct
4. Check finger positions carefully

### Cursor Too Sensitive/Slow
1. Adjust MOUSE_SMOOTHENING (higher = smoother)
2. Change FRAME_REDUCTION for larger control area
3. Adjust camera distance

### Drawing Not Working
1. Toggle draw mode with pinky gesture
2. Check for "DRAW MODE: ON" indicator
3. Use only index finger to draw
4. Clear canvas if needed

---

## 📝 Quick Reference Table

| Gesture | Hand | Fingers | Action |
|---------|------|---------|--------|
| Index up | Right | ☝️ | Move cursor |
| Index + Middle touch | Right | ☝️🖕 | Left click |
| Index + Ring touch | Right | ☝️💍 | Right click |
| Index + Middle close | Right | ☝️🖕 | Double click |
| Thumb + Index pinch | Right | 👍☝️ | Drag & drop |
| 3 fingers up | Right | ☝️🖕💍 | Scroll |
| Pinky only | Right | 🤙 | Toggle draw |
| All fingers | Right | ✋ | Clear canvas |
| Thumb + Index | Left | 👍☝️ | Volume |
| Thumb + Middle | Left | 👍🖕 | Brightness |
| 3 fingers | Left | ☝️🖕💍 | Open Chrome |
| Fist | Left | ✊ | Open Notepad |
| Index + Pinky | Left | ☝️🤙 | Copy |
| Index + Middle + Pinky | Left | ☝️🖕🤙 | Paste |
| Thumb only | Left | 👍 | Start PPT |
| Pinky only | Left | 🤙 | Exit PPT |
| Index only | Left | ☝️ | Next slide |
| Index + Middle | Left | ☝️🖕 | Prev slide |

---

**Remember**: Practice makes perfect! Start with basic gestures and gradually try more complex ones.

For detailed configuration options, see `config.py`
For troubleshooting, see `README.md`
