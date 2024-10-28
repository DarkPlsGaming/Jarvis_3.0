# This file consists of all the non-important functions that are required by other classes/files (particularly commands.py)

# Imports
import json
from email.errors import InvalidBase64CharactersDefect
from urllib.request import urlopen
import requests
import datetime
import os
import sys
from bs4 import BeautifulSoup
import openAppSites
import reminder
import JTime


def extractDetails(query: str):
    loc = query.find("on") + 3

    # If no keyword
    if loc < 0:
        return None, None

    # Getting date
    date = ""
    rem = ""
    try:
        while loc < len(query):
            date += str(int(query[loc]))
            loc += 1

    # Getting reminder
    except ValueError:
        rem = ""
        loc += 1
        while loc < len(query):
            rem += query[loc]
            loc += 1


    return f"{datetime.datetime.now().year}:{datetime.datetime.now().month}:{date}", rem


def setReminder(query: str) -> str | None:
    # Set a reminder on 69 January Play Minecraft
    date, remind = extractDetails(query)

    # Error setting up reminder
    if not remind:
        return None

    myRem = reminder.Reminder()
    myRem.setReminder(remind, date)

    return f"{date}"


def checkTimer():
    myRem = reminder.Reminder()
    output = myRem.checkForReminders()
    del myRem
    return output

def extractTimeAlarm(query: str) -> [int, int, int]:
    hour, minute, second = 0, 0, 0

    # Finding position of "at" or "for"
    loc = query.find("at")
    if loc < 0:
        loc = query.find("for")

    # Finding starting of time
    while query[loc] != " ":
        loc += 1
    loc += 1

    timeStr = ""

    # Extracting time
    while loc < len(query) and query[loc] != " " and query[loc] != "p":
        timeStr += query[loc]
        loc += 1

    # Checking for minute in time
    loc = timeStr.find(":")

    if loc < 0: # If no minute
        return int(timeStr), minute, second

    # if minute
    hour = ""
    minute = ""

    # Extracting hour
    for i in range(0, loc):
        hour += timeStr[i]

    # Extracting minute
    for i in range(loc+1, len(timeStr)):
        minute += timeStr[i]

    return int(hour), int(minute), second


def setAlarm(query: str) -> str | None:
    if "at" not in query and "for" not in query:
        return None

    alarm = JTime.Alarm()
    hour, minute, second = extractTimeAlarm(query)

    # Converting to military time
    if "p.m." in query:
        hour += 12

    if not alarm.setAlarm(hour, minute, second):
        return None

    # Not returning minute if it is 0
    if minute == 0:
        return f"{hour} o clock"

    return f"{hour}:{minute}"


def extractTime(query, time: str) -> int | None:
    if time != "hour" and time != "minute" and time != "second":
        raise InvalidBase64CharactersDefect

    pos = query.find(f"{time}")
    timeNeed = 0
    if pos != -1:
        timeNeed = ""
        pos -= 2
        while query[pos] != " ":
            timeNeed += query[pos]
            pos -= 1

            if pos <= -1:
                break

        timeNeed = int(timeNeed[::-1])
    return timeNeed


def setTimer(query: str) -> str:
    timer = JTime.Timer()

    hour = extractTime(query, "hour")
    minute = extractTime(query, "minute")
    second = extractTime(query, "second")

    timer.setTimer(hour, minute, second)
    del timer

    outStr: str = ""
    if hour != 0:
        outStr += f"{hour} hours "
        if second == 0:
            outStr += "and "
    if minute != 0:
        outStr += f"{minute} minutes "
    if (hour != 0 or minute != 0) and second != 0:
        outStr += "and "
    if second != 0:
        outStr += f"{second} seconds"

    return outStr


def remindTimer(output: str):
    myTimer = JTime.Timer()
    myTimer.setTimer(second=1, outStr=output)

def terminate():
    sys.exit(0)


def getAppWeb(query: str) -> str | None:  # For openWebApps function, gets the application or website name
    try:
        startLoc = query.find("open") + 5  # Locating "open" in user query
        endLoc = startLoc
        while query[endLoc] != " " and endLoc < len(query)-1:
            endLoc += 1

        return query[startLoc:endLoc+1].strip()  # Returning the word that is after "open" in user query

    except IndexError:
        return None


def openWebApps(query: str):
    appName: str | None = getAppWeb(query)  # Identifies the application/website name
    openAppSite = openAppSites.OpenAppSites()  # Instance of the class "OpenAppSites"

    if not appName:
        return None

    if not openAppSite.openApplication(appName):
        result = openAppSite.openWebsite(appName)

        if not result:  # If the requested app is neither application nor website
            return None

    del openAppSite  # Deleting the instance as it is not needed anymore
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
    return "Good afternoon Sir!"  # To be changed to multiple random phrases by Lafiz


if __name__ == "__main__":
    print(setReminder("Set a reminder on 24 play minecraft"))