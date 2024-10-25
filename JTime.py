import time
import threading
import outputHandling
import keyboardHandling


# Main Class
class Timer:
    def __init__(self):
        self.inpHandler = keyboardHandling.KeyboardHandler()
        self.remindLoop = False  # ----


    def __checkRemindLoopEnd(self) -> None:
        self.inpHandler.listenForKey("Key.ctrl_l")
        self.remindLoop = False
        return None


    def __remind(self) -> None:
        self.remindLoop = True
        threading.Thread(target=self.__checkRemindLoopEnd).start()

        speaker = outputHandling.Speaker()

        while self.remindLoop is True:
            speaker.speak("The timer has ended sir!")

        del speaker
        return None


    def __setTimer(self, hour: int = 0, minute: int = 0, second: int = 0) -> None:
        # We are not using a single sleep statement as I plan on adding pausing / cancelling to timers soon
        for i in range((hour*60*60)+(minute*60)+second):
            time.sleep(1)

        return self.__remind()


    def setTimer(self, hour: int = 0, minute: int = 0, second: int = 0):
        timer = threading.Thread(target=self.__setTimer, args=[hour, minute, second])
        timer.daemon = True
        timer.start()


if __name__ == "__main__":
    myTimer = Timer()

    myTimer.setTimer(second=5)