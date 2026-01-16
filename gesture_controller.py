import time
import numpy as np
import pyautogui
import config

from utils.volume import VolumeController
from utils.brightness import BrightnessController
from utils.apps import open_app
from utils.keyboard_control import shortcut, type_text
from utils.drawing_board import DrawingBoard
from utils.powerpoint_control import next_slide, prev_slide, start_ppt, exit_ppt


class GestureController:
    def __init__(self, screen_w, screen_h, cam_w=640, cam_h=480):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.cam_w = cam_w
        self.cam_h = cam_h

        # mouse smoothing
        self.smoothening = config.MOUSE_SMOOTHENING
        self.prev_x, self.prev_y = 0, 0

        # boundaries
        self.frameR = config.FRAME_REDUCTION

        # click cooldown
        self.last_click_time = 0
        self.click_delay = config.CLICK_DELAY

        # drag state
        self.dragging = False

        # mode
        self.draw_mode = False

        # controllers
        try:
            self.vol = VolumeController()
        except Exception as e:
            print(f"Warning: Volume controller initialization failed: {e}")
            self.vol = None
        
        try:
            self.bright = BrightnessController()
        except Exception as e:
            print(f"Warning: Brightness controller initialization failed: {e}")
            self.bright = None
            
        self.board = DrawingBoard(width=cam_w, height=cam_h)

    def _cooldown_ok(self):
        return (time.time() - self.last_click_time) > self.click_delay

    def process(self, img, detector, hands):
        """
        Right hand => mouse actions
        Left hand => system controls (volume/brightness/apps/ppt)
        """

        # If no hands
        if len(hands) == 0:
            return img

        # Split hands (swapped for natural use)
        right_hand = None
        left_hand = None
        for h in hands:
            if h["type"] == "Right":
                left_hand = h  # Swap: Right detection = Left hand control
            elif h["type"] == "Left":
                right_hand = h  # Swap: Left detection = Right hand control

        # ---------- RIGHT HAND : Mouse + Drawing ----------
        if right_hand:
            lmList = right_hand["lmList"]
            fingers = detector.fingers_up(lmList, "Right")

            x_index, y_index = lmList[8][1], lmList[8][2]
            x_middle, y_middle = lmList[12][1], lmList[12][2]
            x_ring, y_ring = lmList[16][1], lmList[16][2]
            x_thumb, y_thumb = lmList[4][1], lmList[4][2]

            # draw boundary
            import cv2
            cv2.rectangle(img, (self.frameR, self.frameR),
                          (self.cam_w - self.frameR, self.cam_h - self.frameR),
                          config.COLOR_FRAME_BORDER, 2)

            # ✅ Right Click with THUMB ONLY
            if fingers == [1, 0, 0, 0, 0] and self._cooldown_ok():
                pyautogui.rightClick()
                self.last_click_time = time.time()

            # ✅ Toggle DRAW MODE: Pinky up only
            elif fingers == [0, 0, 0, 0, 1] and self._cooldown_ok():
                self.draw_mode = not self.draw_mode
                self.last_click_time = time.time()

            # ✅ Clear canvas: All fingers up
            if fingers == [1, 1, 1, 1, 1] and self._cooldown_ok():
                self.board.clear()
                self.last_click_time = time.time()

            # ✅ Drawing mode
            if self.draw_mode:
                drawing = (fingers[1] == 1 and fingers[2] == 0)  # index only
                img = self.board.draw(img, (x_index, y_index), drawing=drawing)
            else:
                # ✅ Mouse Move: Index up, middle down
                if fingers[1] == 1 and fingers[2] == 0:
                    x3 = np.interp(x_index, (self.frameR, self.cam_w - self.frameR), (0, self.screen_w))
                    y3 = np.interp(y_index, (self.frameR, self.cam_h - self.frameR), (0, self.screen_h))

                    curr_x = self.prev_x + (x3 - self.prev_x) / self.smoothening
                    curr_y = self.prev_y + (y3 - self.prev_y) / self.smoothening

                    pyautogui.moveTo(curr_x, curr_y)
                    self.prev_x, self.prev_y = curr_x, curr_y

                # ✅ Click gestures with proper distance checks
                length_index_middle, _ = detector.distance(lmList, 8, 12)
                
                # Double Click: Index + middle very close (check first to avoid conflict)
                if fingers[1] == 1 and fingers[2] == 1 and length_index_middle < config.DOUBLE_CLICK_DISTANCE and self._cooldown_ok():
                    pyautogui.doubleClick()
                    self.last_click_time = time.time()
                
                # Left Click: Index + middle up (ANY distance - removed distance check)
                elif fingers[1] == 1 and fingers[2] == 1 and self._cooldown_ok():
                    pyautogui.click()
                    self.last_click_time = time.time()

                # RIGHT CLICK NOW USES THUMB (removed index+ring gesture)

                # ✅ Drag & Drop: Thumb + index pinch hold
                length_drag, _ = detector.distance(lmList, 4, 8)
                if length_drag < config.PINCH_THRESHOLD_CLOSE and not self.dragging:
                    pyautogui.mouseDown()
                    self.dragging = True
                elif length_drag > config.PINCH_THRESHOLD_RELEASE and self.dragging:
                    pyautogui.mouseUp()
                    self.dragging = False

                # ✅ Scroll: Three fingers up (index, middle, ring)
                if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[0] == 0 and fingers[4] == 0:
                    # based on vertical movement of middle finger
                    scroll_amount = int(np.interp(y_middle, (0, self.cam_h), (config.SCROLL_SENSITIVITY, -config.SCROLL_SENSITIVITY)))
                    if abs(scroll_amount) > config.SCROLL_THRESHOLD:  # Avoid tiny scrolls
                        pyautogui.scroll(scroll_amount)

        # ---------- LEFT HAND : Volume + Brightness + Apps + PPT ----------
        if left_hand:
            lmList = left_hand["lmList"]
            fingers = detector.fingers_up(lmList, "Left")
            
            # DEBUG: Print detected gesture
            if config.DEBUG_MODE:
                print(f"LEFT HAND: {fingers}")

            # BLOCK: Thumb only gesture (do nothing - prevent any action)
            if fingers == [1, 0, 0, 0, 0]:
                if config.DEBUG_MODE:
                    print("LEFT THUMB ONLY - BLOCKED")
                pass  # Explicitly do nothing
                
            # BLOCK: Fist gesture (all fingers down)
            elif fingers == [0, 0, 0, 0, 0]:
                if config.DEBUG_MODE:
                    print("LEFT FIST - BLOCKED")
                pass  # Explicitly do nothing

            # Volume control (Thumb + index distance)
            dist_vol, _ = detector.distance(lmList, 4, 8)
            vol_percent = int(np.interp(dist_vol, (config.VOLUME_MIN_DISTANCE, config.VOLUME_MAX_DISTANCE), (0, 100)))

            # Brightness control (Thumb + middle distance)
            dist_bri, _ = detector.distance(lmList, 4, 12)
            bri_percent = int(np.interp(dist_bri, (config.BRIGHTNESS_MIN_DISTANCE, config.BRIGHTNESS_MAX_DISTANCE), (0, 100)))

            # ✅ Volume Gesture: only thumb + index up
            if fingers == [1, 1, 0, 0, 0]:
                if self.vol and self.vol.enabled:
                    self.vol.set_volume_percent(vol_percent)

            # ✅ Brightness Gesture: thumb + middle up
            elif fingers == [1, 0, 1, 0, 0]:
                if self.bright:
                    self.bright.set_brightness(bri_percent)

            # ✅ Open Apps gestures
            elif fingers == [0, 1, 1, 1, 0] and self._cooldown_ok():  # 3 fingers (index+middle+ring)
                try:
                    open_app("chrome")
                except Exception as e:
                    print(f"Error opening Chrome: {e}")
                self.last_click_time = time.time()

            # ✅ Keyboard shortcuts
            elif fingers == [0, 1, 0, 0, 1] and self._cooldown_ok():  # index+pinky
                shortcut("ctrl+c")
                self.last_click_time = time.time()

            elif fingers == [0, 1, 1, 0, 1] and self._cooldown_ok():  # index+middle+pinky
                shortcut("ctrl+v")
                self.last_click_time = time.time()

        return img
