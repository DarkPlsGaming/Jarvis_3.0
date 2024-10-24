import pynput.keyboard


class KeyboardHandler:
    def __init__(self):
        self.listener = pynput.keyboard.Listener


    @staticmethod
    def __press_on(key):
        if key == pynput.keyboard.Key.ctrl_r:
            raise KeyboardInterrupt


    def listenForKey(self):
        # Starting Listening for key input
        with self.listener(on_press=self.__press_on) as lis:
            lis.join()

        # If code reaches here, it means user wants to run jarvis
        return 1



if __name__ == "__main__":
    kH = KeyboardHandler()

    kH.listenForKey()