import cv2
import mediapipe as mp
import config
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandDetector:
    def __init__(self, model_path=None, max_hands=2):
        if model_path is None:
            model_path = config.MODEL_PATH
        self.max_hands = max_hands

        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=max_hands
        )
        self.detector = vision.HandLandmarker.create_from_options(options)

    def find_hands(self, img, draw=True):
        """
        Returns the same structure as before:
        hands_data = [
          {"lmList": [[id,cx,cy]...], "bbox": (xmin,ymin,xmax,ymax), "type": "Left"/"Right"}
        ]
        """
        h, w, _ = img.shape
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        result = self.detector.detect(mp_image)

        hands_data = []

        if result.hand_landmarks:
            for i, hand_lms in enumerate(result.hand_landmarks):
                lmList = []
                xList, yList = [], []

                for idx, lm in enumerate(hand_lms):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([idx, cx, cy])
                    xList.append(cx)
                    yList.append(cy)

                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                bbox = (xmin, ymin, xmax, ymax)

                hand_type = "Unknown"
                if result.handedness:
                    hand_type = result.handedness[i][0].category_name  # "Left" or "Right"

                hands_data.append({"lmList": lmList, "bbox": bbox, "type": hand_type})

                # Draw landmarks (optional)
                if draw and config.SHOW_HAND_LANDMARKS:
                    for _, cx, cy in lmList:
                        cv2.circle(img, (cx, cy), 4, config.COLOR_LANDMARKS, cv2.FILLED)

                if draw and config.SHOW_BOUNDING_BOX:
                    cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                                  config.COLOR_BBOX, 2)

        return img, hands_data

    def fingers_up(self, lmList, hand_type="Right"):
        """
        Same logic (landmark indices are same 0-20)
        """
        tip_ids = [4, 8, 12, 16, 20]
        fingers = []

        # Thumb
        if hand_type == "Right":
            fingers.append(1 if lmList[tip_ids[0]][1] > lmList[tip_ids[0] - 1][1] else 0)
        else:
            fingers.append(1 if lmList[tip_ids[0]][1] < lmList[tip_ids[0] - 1][1] else 0)

        # Index, Middle, Ring, Pinky
        for i in range(1, 5):
            fingers.append(1 if lmList[tip_ids[i]][2] < lmList[tip_ids[i] - 2][2] else 0)

        return fingers

    def distance(self, lmList, p1, p2):
        x1, y1 = lmList[p1][1], lmList[p1][2]
        x2, y2 = lmList[p2][1], lmList[p2][2]
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        return length, (x1, y1, x2, y2, cx, cy)
