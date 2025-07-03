# This file is related to the opening or closing of websites and applications

# Imports
from pywinauto import application
import Data.UniversalVariables
import webbrowser


# Main Class
class OpenAppSites:
    def __init__(self):
        self.applic = application.Application()  # Initializing app for opening applications


    # Returns true if and only if the application's PATH is found
    def openApplication(self, app: str) -> bool:
        for apps in Data.UniversalVariables.applications:  # Looping through all the applications known in Data
            if app != apps:  # If not found, move on to the next application
                continue
            self.applic.start(Data.UniversalVariables.applications.get(apps))  # If found, start the application
            return True

        return False  # If not found, return False


    @staticmethod
    # Returns true if and only if the website's URL is found
    def openWebsite(website: str) -> bool:
        for web in Data.UniversalVariables.websites:  # Looping through all the websites known in Data
            if web != website:  # If not found, move on to the next website
                continue

            webbrowser.open(Data.UniversalVariables.websites.get(web))  # If found, start the application
            return True

        return False  # If not found, return False


if __name__ == "__main__":
    openApp = OpenAppSites()
    openApp.openWebsite("youtube")
