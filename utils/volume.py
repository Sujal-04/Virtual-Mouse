from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import sys


class VolumeController:
    def __init__(self):
        self.enabled = False
        self.volume = None
        self.minVol = -65.25
        self.maxVol = 0.0
        
        # Only try to initialize on Windows
        if sys.platform != 'win32':
            print("Volume control only available on Windows")
            return
            
        try:
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            self.volume = cast(interface, POINTER(IAudioEndpointVolume))
            self.minVol, self.maxVol, _ = self.volume.GetVolumeRange()
            self.enabled = True
            print(f"✓ Volume control initialized (Range: {self.minVol:.1f} to {self.maxVol:.1f})")
        except AttributeError as e:
            print(f"✗ Volume control error: pycaw version issue")
            print(f"  Try: pip uninstall pycaw && pip install pycaw")
        except Exception as e:
            print(f"✗ Volume control not available: {e}")

    def set_volume_percent(self, percent: int):
        if not self.enabled or self.volume is None:
            return
        
        try:
            percent = max(0, min(100, percent))
            vol = self.minVol + (percent / 100) * (self.maxVol - self.minVol)
            self.volume.SetMasterVolumeLevel(vol, None)
        except Exception as e:
            print(f"Error setting volume: {e}")
            self.enabled = False
