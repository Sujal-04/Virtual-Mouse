"""
VirtuaMouse Keyboard Shortcut Launcher
This script allows launching VirtuaMouse using a keyboard shortcut (Ctrl+Alt+M)
even when the mouse is not working.
"""
import keyboard
import subprocess
import sys
import os
import config


def launch_virtuamouse():
    """Launch the main VirtuaMouse application"""
    print("Launching VirtuaMouse...")
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        main_script = os.path.join(script_dir, "main.py")
        
        # Launch main.py
        subprocess.Popen([sys.executable, main_script])
        print("VirtuaMouse launched successfully!")
    except Exception as e:
        print(f"Error launching VirtuaMouse: {e}")


def main():
    print("=" * 60)
    print("VirtuaMouse Keyboard Launcher")
    print("=" * 60)
    print(f"Press {config.LAUNCHER_HOTKEY.upper()} to launch VirtuaMouse")
    print(f"Press {config.LAUNCHER_QUIT_HOTKEY.upper()} to quit this launcher")
    print("=" * 60)
    
    # Register the hotkey
    keyboard.add_hotkey(config.LAUNCHER_HOTKEY, launch_virtuamouse)
    keyboard.add_hotkey(config.LAUNCHER_QUIT_HOTKEY, lambda: sys.exit(0))
    
    print("\nLauncher is running... Waiting for hotkey...")
    
    try:
        # Keep the script running
        keyboard.wait()
    except KeyboardInterrupt:
        print("\nLauncher stopped by user")


if __name__ == "__main__":
    main()
