# This file helps J3 to SPY on our user!

# Imports
import psutil
import json
import time
import datetime
import threading
from Data.UniversalVariables import gamesForDetection as games
from Data.UniversalVariables import appsForDetection as apps
import garbageFunctions as gF
import outputHandling


class ActivityDetection:
    def __init__(self):
        self.data = None
        self.applications: list = games + apps
        self.__loadData()

    @staticmethod
    def __check_application_running(app_name: str) -> bool:  # I have to admit, this function is (probably) provided by ChatGPT. (I understand how it works!) -Liman
        # Iterate through all running processes
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # Check if the application's name is in the process name
                if app_name.lower().replace(' ', '') in proc.info['name'].lower().replace(' ', ''):
                    return True

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        return False

    @staticmethod
    def __getGroupedData(data: dict[str, int]) -> tuple[dict, dict, dict, dict, dict]:
        gamesData = {}
        browserData = {}
        programmingData = {}
        messagingData = {}
        otherData = {}

        for key, value in data.items():
            if key in str(games).lower():  # For games
                gamesData[key] = value
                continue

            if key.lower() in 'chrome firefox tor brave':  # For browsers
                browserData[key] = value
                continue

            if key.lower() in 'code pycharm vmware.exe':
                programmingData[key] = value
                continue

            if key.lower() in 'whatsapp discord':
                messagingData[key] = value
                continue

            if key.lower() in str(apps).lower():  #  For additional applications
                otherData[key] = value

        return gamesData, browserData, programmingData, messagingData, otherData

    @staticmethod
    def __saveReport(data):
        with open('Data/ProgressReport.txt', 'w') as f:
           f.write(data)

    @staticmethod
    def __getReportDate():
        with open('Data/PresentationDate.txt') as f:
            date = f.read()
        return date

    @staticmethod
    def __checkDate(presentDate, reportDate) -> bool:
        return str(presentDate) >= str(reportDate)

    @staticmethod
    def __saveNewDate(date: datetime.date):
        new_date = date + datetime.timedelta(days=7)
        with open('Data/PresentationDate.txt', 'w') as f:
            f.write(str(new_date))

    @staticmethod
    def __speakPresentation():
        speaker = outputHandling.Speaker()
        speaker.speak("Your presentation report is ready Sir. Opening it now.")
        del speaker

    # noinspection PyTypeChecker
    def __saveData(self):
        with open('Data/activity.json', 'w') as f:
           json.dump(self.data, f, indent=4)

    def __loadData(self):
        with open('Data/activity.json') as f:
            self.data = json.load(f)

    def __addTimeToLoadedDictionary(self, app):
        try:
            self.data[app] += 5  # Add 5 minutes to the app in our loaded data dictionary
        except KeyError:  # If app is not loaded in our dictionary
            self.data[app] = 5  # Then add it

    def __getReportData(self):
        totalTime = gF.convertMinutesToTime(self.data['total'])  # Getting total screen time in hours
        gamesData, browserData, programmingData, messagingData, otherData = self.__getGroupedData(self.data)  # Getting screenTime for games and applications

        data = gF.formProgressReport(self.data, totalTime, gamesData, browserData, programmingData, messagingData, otherData, self.data['startDate'], datetime.date.today())  # Getting formed report
        return data

    def __startCheck(self):  # Add 5 minutes to all applications and total time per iteration. If an application is running and not saved in data, then dynamically appends it to the dictionary and saves it to the json file.  - Liman
        while True:
            time.sleep(5 * 60)
            for app in self.applications:
                if not self.__check_application_running(app):
                    continue
                self.__addTimeToLoadedDictionary(app)  # Adds 5 minutes to our data dictionary for the particular app

            self.data['total'] += 5  # Adds 5 minutes to total time
            self.__saveData()  # Saving data to json file

    def __constructPresentation(self):
        # Construction
        data = self.__getReportData()

        # Saving and Presentation
        self.__saveReport(data)
        gF.openReport()

        # Resetting Data
        self.data = {'startDate': f'{datetime.date.today()}', 'total': 0}
        self.__saveData()

    def start(self):
        t = threading.Thread(target=self.__startCheck)
        t.daemon = True
        t.start()

    def check(self):  # Checks for report presentation date
        presentDate = datetime.date.today()  # Getting present date
        reportDate = self.__getReportDate()  # Getting report date
        if self.__checkDate(presentDate, reportDate):  # If we are on or have passed the report date
            self.__speakPresentation()  # Voice Output to user
            self.__constructPresentation()  # Then construct the presentation
            self.__saveNewDate(datetime.date.today())  # Saves next date for presenting progress report

if __name__ == "__main__":
    pass
    # ActivityDetection().startCheck()
    # ActivityDetection().constructPresentation()
    # print(gF.convertMinutesToTime(61))