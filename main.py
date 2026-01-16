import cv2
import time
import autopy
import pyautogui

from hand_tracking import HandDetector
from gesture_controller import GestureController
import config

# Set PyAutoGUI failsafe
pyautogui.FAILSAFE = config.PYAUTOGUI_FAILSAFE
pyautogui.PAUSE = config.PYAUTOGUI_PAUSE


def main():
    cam_w, cam_h = config.CAMERA_WIDTH, config.CAMERA_HEIGHT
    
    # Initialize camera with error handling
    cap = cv2.VideoCapture(config.CAMERA_INDEX)
    if not cap.isOpened():
        print("Error: Could not open camera. Please check your webcam connection.")
        return
    
    cap.set(3, cam_w)
    cap.set(4, cam_h)

    try:
        detector = HandDetector(max_hands=config.MAX_HANDS, model_path=config.MODEL_PATH)
        screen_w, screen_h = autopy.screen.size()
        controller = GestureController(screen_w, screen_h, cam_w, cam_h)
    except Exception as e:
        print(f"Error initializing components: {e}")
        cap.release()
        return

    pTime = 0

    print("VirtuaMouse started successfully!")
    print("Press 'q' to quit")
    print("Move mouse cursor to top-left corner for emergency exit (PyAutoGUI failsafe)")

    try:
        while True:
            success, img = cap.read()
            if not success:
                print("Error: Failed to read from camera")
                break

            img = cv2.flip(img, 1)
            
            try:
                img, hands = detector.find_hands(img, draw=config.SHOW_HAND_LANDMARKS)
                img = controller.process(img, detector, hands)
            except Exception as e:
                print(f"Error processing frame: {e}")
                continue

            # FPS
            cTime = time.time()
            fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
            pTime = cTime

            # Display info
            if config.SHOW_FPS:
                cv2.putText(img, f"FPS: {int(fps)}", (20, 50),
                            cv2.FONT_HERSHEY_PLAIN, 2, config.COLOR_FPS, 2)

            if config.SHOW_INSTRUCTIONS:
                cv2.putText(img, "Right Hand: Mouse | Left Hand: Controls", (20, 80),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, config.COLOR_INSTRUCTIONS, 2)

                cv2.putText(img, "Pinky(R): Toggle Draw | All fingers(R): Clear", (20, 110),
                            cv2.FONT_HERSHEY_PLAIN, 1.2, config.COLOR_INSTRUCTIONS, 2)
            
            # Display draw mode status
            if config.SHOW_DRAW_MODE_STATUS:
                draw_status = "DRAW MODE: ON" if controller.draw_mode else "DRAW MODE: OFF"
                color = config.COLOR_DRAW_MODE_ON if controller.draw_mode else config.COLOR_DRAW_MODE_OFF
                cv2.putText(img, draw_status, (20, 140),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, color, 2)

            cv2.imshow(config.WINDOW_NAME, img)

            if cv2.waitKey(1) & 0xFF == ord(config.QUIT_KEY):
                break

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("VirtuaMouse closed")


if __name__ == "__main__":
    main()
