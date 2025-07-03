# You are using this for starting VMWare, idiot!

# Imports
import pyautogui
from pyautogui import ImageNotFoundException


# Class Image Detector
class ImageDetector:
    def __init__(self):
        pass


    @staticmethod
    def detectImage(path: str, confidence: float = 0.7):
        try:
            return pyautogui.locateOnScreen(path, confidence=confidence)
        except ImageNotFoundException:
            return -1