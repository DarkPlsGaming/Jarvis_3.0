# This file is related to the handling of keyboard (for both listening and sending inputs)

# Imports
import pynput.keyboard


# Main Class
class KeyboardHandler:
    def __init__(self):
        self.listener = pynput.keyboard.Listener  # Initializing a keyboard listener object


    @staticmethod
    def __press_on(key):
        if key == pynput.keyboard.Key.ctrl_r:  # If target key for starting of voice input is pressed
            raise KeyboardInterrupt  # Break out of key listening


    def listenForKey(self):
        # Starting Listening for key input
        with self.listener(on_press=self.__press_on) as lis:
            lis.join()

        # If code reaches here, it means user wants to send a voice input to Jarvis
        return 1



if __name__ == "__main__":
    kH = KeyboardHandler()
    kH.listenForKey()
