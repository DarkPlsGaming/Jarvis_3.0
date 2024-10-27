import time
import threading
import datetime
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


    def __remind(self, outStr) -> None:
        self.remindLoop = True
        threading.Thread(target=self.__checkRemindLoopEnd).start()

        speaker = outputHandling.Speaker()

        while self.remindLoop is True:
            speaker.speak(outStr)

        del speaker
        return None


    def __setTimer(self, outStr, hour: int = 0, minute: int = 0, second: int = 0) -> None:
        # We are not using a single sleep statement as I plan on adding pausing / cancelling to timers soon
        for i in range((hour*60*60)+(minute*60)+second):
            time.sleep(1)

        return self.__remind(outStr)


    def setTimer(self, hour: int = 0, minute: int = 0, second: int = 0, *, outStr: str = "The timer has ended Sir!"):
        timer = threading.Thread(target=self.__setTimer, args=[outStr, hour, minute, second])
        timer.daemon = True
        timer.start()


class Alarm:
    def __init__(self):
        pass


    @staticmethod
    def __getTime() -> [int, int, int]:
        curTime = datetime.datetime.now()
        hour = int(curTime.strftime("%H"))
        minute = int(curTime.strftime("%M"))
        second = int(curTime.strftime("%S"))

        return hour, minute, second


    @staticmethod
    def __checkAlarmCompat(hour: int = 0, minute: int = 0, second: int = 0, curHour: int = 0, curMin: int = 0, curSec: int = 0) -> bool:  # Checks if the timer is on the same day
        if curHour < hour:
            return True

        if curHour > hour:
            return False

        if curMin < minute:
            return True

        if curMin > minute:
            return False

        if curSec < second:
            return True

        return False  # Hour and minute is same but second is incompatible


    @staticmethod  # Returns the time difference in seconds
    def __getTimerSec(hour: int = 0, minute: int = 0, second: int = 0, curHour: int = 0, curMin: int = 0, curSec: int = 0) -> int:
        targetSec = (hour * 60 * 60) + (minute * 60) + second
        curSec = (curHour * 60 * 60) + (curMin * 60) + curSec

        return targetSec - curSec


    def setAlarm(self, hour: int = 0, minute: int = 0, second: int = 0) -> bool:  # Inputs are military time
        curHour, curMin, curSec = self.__getTime()
        if not self.__checkAlarmCompat(hour, minute, second, curHour, curMin, curSec):
            return False

        timer = Timer()
        timerSec: int = self.__getTimerSec(hour, minute, second, curHour, curMin, curSec)

        timer.setTimer(second=timerSec, outStr="Sir your alarm is going off!")
        del timer

        return True


if __name__ == "__main__":
    myAlarm = Alarm()
    myAlarm.setAlarm(22, 3, 0)
