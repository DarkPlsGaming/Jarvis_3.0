# This file is related to the handling of keyboard (for both listening and sending inputs)

# Imports
import pynput.keyboard
from pynput.keyboard import Key


# Main Class
class KeyboardHandler:
    def __init__(self):  # source: str = "timer"):  # Source stands for from which file is this class being used
        self.targetKey = None
        self.listener = pynput.keyboard.Listener  # Initializing a keyboard listener object
        self.controller = pynput.keyboard.Controller()


    def __press_on(self, key):
        # print(self.targetKey, str(key))
        if str(key) == self.targetKey:  # If target key is pressed
            raise KeyboardInterrupt  # Break out of key listening


    def listenForKey(self, targetKey: str):
        self.targetKey = targetKey

        # Starting Listening for key input
        with self.listener(on_press=self.__press_on) as lis:
            lis.join()

        # If code reaches here, it means the desired key has been pressed
        return 1


    def pressKey(self, targetKey: str | Key):
        if targetKey == "Key.alt_gr":
            targetKey = Key.alt_gr

        self.controller.press(targetKey)
        self.controller.release(targetKey)


if __name__ == "__main__":
    kH = KeyboardHandler()
    kH.pressKey("l")
    # if kH.listenForKey("Key.alt_gr"):
    #     print("hehe boi")
