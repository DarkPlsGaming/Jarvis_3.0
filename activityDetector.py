# This file helps J3 to SPY on our user!

# Imports
import psutil
from Data.UniversalVariables import games


class ActivityDetection:
    def __init__(self):
        self.applications: list = games


    @staticmethod
    def __check_application_running(app_name: str) -> bool:
        # Iterate through all running processes
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # Check if the application's name is in the process name
                if app_name.lower() in proc.info['name'].lower():
                    return True

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        return False


    def startCheck(self):
        for app in self.applications:
            self.__check_application_running(app)
