import json
from urllib.request import urlopen
import requests
import os
from bs4 import BeautifulSoup
import openAppSites


def getAppWeb(query: str) -> str | None:  # For open, gets the application or website name
    try:
        startLoc = query.find("open") + 5
        endLoc = startLoc
        while query[endLoc] != " " and endLoc < len(query)-1:
            endLoc += 1

        return query[startLoc:endLoc+1].strip()

    except IndexError:
        return None


def openWebApps(query: str):
    appName: str | None = getAppWeb(query)
    openAppSite = openAppSites.OpenAppSites()

    if not appName:
        return None

    if not openAppSite.openApplication(appName):
        openAppSite.openWebsite(appName)

    del openAppSite
    return appName


def shutdown():
    os.system("shutdown /s /t 1")


def getLocation():
    data = json.load(urlopen("http://ipinfo.io/json"))
    city = data.get("city")
    region = data.get("region")

    return f"{region}, {city}"


def getTemperature():
    # Searching on Google
    url = f"https://www.google.com/search?q={'Temperature in' + getLocation()}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text

    return temp


def getGreetPhrase():
    return "Good afternoon Sir!"


if __name__ == "__main__":
    print(openWebApps("open notepad"))