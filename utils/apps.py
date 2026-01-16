import subprocess
import platform
import os


def open_app(app_name: str):
    """
    Open applications safely - NOTEPAD IS COMPLETELY BLOCKED
    """
    system = platform.system()
    
    # ABSOLUTE BLOCK: Never open notepad
    if "notepad" in app_name.lower():
        print("❌ BLOCKED: Notepad is disabled")
        return
    
    print(f"Attempting to open: {app_name}")
    
    if system == "Windows":
        if app_name == "chrome":
            try:
                # Use full path to avoid any ambiguity
                subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"], 
                               shell=False)
            except:
                try:
                    # Fallback to start command
                    subprocess.Popen(["cmd", "/c", "start", "chrome"], shell=False)
                except Exception as e:
                    print(f"Could not open Chrome: {e}")
                    
        elif app_name == "calculator":
            try:
                subprocess.Popen(["calc.exe"], shell=False)
            except Exception as e:
                print(f"Could not open Calculator: {e}")
                
        elif app_name == "vscode":
            try:
                subprocess.Popen(["code"], shell=False)
            except Exception as e:
                print(f"Could not open VSCode: {e}")
        else:
            print(f"❌ App '{app_name}' not in allowed list")
            
    elif system == "Darwin":  # macOS
        if app_name in ["chrome", "calculator", "vscode"]:
            try:
                subprocess.call(["open", "-a", app_name])
            except Exception as e:
                print(f"Could not open {app_name}: {e}")
                
    else:  # Linux
        if app_name in ["chrome", "calculator", "vscode"]:
            try:
                subprocess.call([app_name])
            except Exception as e:
                print(f"Could not open {app_name}: {e}")
