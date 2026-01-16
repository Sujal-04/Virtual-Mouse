import numpy as np
import cv2
import config


class DrawingBoard:
    def __init__(self, width=640, height=480):
        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)
        self.prev_point = None

    def draw(self, img, point, drawing=True):
        if drawing:
            if self.prev_point is None:
                self.prev_point = point
            cv2.line(self.canvas, self.prev_point, point, config.DRAWING_COLOR, config.DRAWING_LINE_THICKNESS)
            self.prev_point = point
        else:
            self.prev_point = None

        combined = cv2.addWeighted(img, 1.0 - config.CANVAS_OPACITY, self.canvas, config.CANVAS_OPACITY, 0)
        return combined

    def clear(self):
        self.canvas[:] = 0
        self.prev_point = None
