import Data.schedule
import outputHandling as oH
from garbageFunctions import extractTime
import JTime


class ScheduleManager:
    @staticmethod
    def __loadSchedule():
        return Data.schedule.todaySchedule if Data.schedule.todaySchedule else Data.schedule.defaultSchedule

    def __init__(self):
        self.schedule = self.__loadSchedule()
        self.timer = JTime.Timer()
        self.speaker = oH.Speaker()


    def __setTimer(self, query):
        query = query.lower()
        hour = extractTime(query, "hour")
        minute = extractTime(query, "minute")
        second = extractTime(query, "second")
        self.timer.setSmartTimer(hour, minute, second)


    def __giveIntro(self):
        self.speaker.speak("Starting today's Schedule, Sir!")
        self.speaker.speak("To pause the schedule at any time, hit right alt button!")


    def __giveOutro(self):
        self.speaker.speak("Today's schedule has ended. Good work, Sir!")
        del self.speaker


    def __speakSchedule(self, schedule):
        self.speaker.speak(f"Sir, it's time to do {schedule} for {self.schedule[schedule]} time!")


    def startSchedule(self):
        self.__giveIntro()
        for schedule in self.schedule:
            self.__speakSchedule(schedule)
            self.__setTimer(self.schedule[schedule])
        self.__giveOutro()


if __name__ == "__main__":
    sMan = ScheduleManager()
    sMan.startSchedule()
