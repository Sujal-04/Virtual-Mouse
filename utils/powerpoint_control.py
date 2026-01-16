import pyautogui


# Disable any hotkeys that might open notepad
BLOCKED_KEYS = []


def next_slide():
    pyautogui.press("right")


def prev_slide():
    pyautogui.press("left")


def start_ppt():
    # F5 might open something - let's disable it
    print("PowerPoint start disabled (F5 blocked)")
    pass


def exit_ppt():
    pyautogui.press("esc")
