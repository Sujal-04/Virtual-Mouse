import screen_brightness_control as sbc


class BrightnessController:
    def set_brightness(self, value: int):
        value = max(0, min(100, value))
        try:
            sbc.set_brightness(value)
        except Exception:
            pass
