# This file is related to the handling of keyboard (for both listening and sending inputs)

# Imports
import pynput.keyboard


# Main Class
class KeyboardHandler:
    def __init__(self):  # source: str = "timer"):  # Source stands for from which file is this class being used
        self.targetKey = None
        self.listener = pynput.keyboard.Listener  # Initializing a keyboard listener object


    def __press_on(self, key):
        if str(key) == self.targetKey:  # If target key is pressed
            raise KeyboardInterrupt  # Break out of key listening


    def listenForKey(self, targetKey: str):
        self.targetKey = targetKey

        # Starting Listening for key input
        with self.listener(on_press=self.__press_on) as lis:
            lis.join()

        # If code reaches here, it means the target key has been pressed
        return 1



if __name__ == "__main__":
    kH = KeyboardHandler()
    if kH.listenForKey("Key.ctrl_l"):
        print("test")
