import fileHandling
from datetime import datetime


# noinspection PyTypeChecker
class Reminder:
    def __init__(self):
        self.fileHand = fileHandling.FileHandler("Data/reminders.json")


    def __checkReminder(self, date: str) -> str | None:
        # Loading data from JSON file
        data: dict = self.fileHand.readFile(jsonOut=True)

        try:
            return data[date]

        except KeyError:
            return None


    def __addReminder(self, reminder: str, time: str):
        # Loading data from JSON file
        data: dict = self.fileHand.readFile(jsonOut=True)

        # Saving reminder to data
        data[time] = reminder

        # Writing reminder to JSON file
        self.fileHand.writeFile(data, jsonOut=True)


    def checkForReminders(self) -> str | None:
        # Acquiring today's date
        today = f"{datetime.now().year}:{datetime.now().month}:{datetime.now().day}"

        # Checking for reminders for today
        reminder: str | None = self.__checkReminder(today)
        if not reminder:
            return None

        self.removeReminder(today)
        return reminder


    def removeReminder(self, date: str):
        # Loading Reminders
        data: dict = self.fileHand.readFile(jsonOut=True)

        # Deleting Target Reminder
        data.pop(date)

        # Writing back the updated reminder dictionary
        self.fileHand.writeFile(data, jsonOut=True)


    def setReminder(self, reminder: str, time: str):  # Time in format %Y:%M:%H
        # Appending to JSON File
        self.__addReminder(reminder, time)



if __name__ == "__main__":
    rem = Reminder()
    print(f"The reminder for today is {rem.checkForReminders()}")
