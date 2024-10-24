from pywinauto import application
import Data.Details
import webbrowser


class OpenAppSites:
    def __init__(self):
        self.applic = application.Application()


    # Returns true if and only if the application's PATH is found
    def openApplication(self, app: str) -> bool:
        for apps in Data.Details.applications:
            if app != apps:
                continue

            self.applic.start(Data.Details.applications.get(apps))
            return True

        return False


    @staticmethod
    # Returns true if and only if the website's URL is found
    def openWebsite(website: str) -> bool:
        for web in Data.Details.websites:
            if web != website:
                continue

            webbrowser.open(Data.Details.websites.get(web))
            return True

        return False


if __name__ == "__main__":
    openApp = OpenAppSites()
    openApp.openWebsite("youtube")
