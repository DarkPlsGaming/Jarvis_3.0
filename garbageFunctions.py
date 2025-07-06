# This file consists of all the non-important functions that are required by other classes/files (particularly commands.py)

# Imports
import json
from urllib.request import urlopen
import requests
import datetime
import os
import sys
from bs4 import BeautifulSoup
import keyboardHandling
import openAppSites
import imageDetection
import reminder
import JTime
import time


def openReport():
    os.system('notepad Data/ProgressReport.txt')


def formProgressReport(totalData, totalTime, gamesData, browserData, programmingData, messagingData, otherData, startDate, endDate):
    data = f"""
    PROGRESS REPORT BY JARVIS
    
    Good Morning Sir, your progress report from last week is ready.
    
    Your total screentime was {totalTime} starting from date {startDate} and ending on {endDate} 
    
    You spent a total of {convertMinutesToTime(sum(programmingData.values()))} programming.
    You spent a total of {convertMinutesToTime(sum(gamesData.values()))} gaming.
    You spent a total of {convertMinutesToTime(sum(browserData.values()))} browsing.
    You spent a total of {convertMinutesToTime(sum(messagingData.values()))} messaging.
    You spent a total of {convertMinutesToTime(sum(otherData.values()))} on other activities.
    
    Your recorded activity in detail:
    """
    data += str(totalData)
    return data


def convertMinutesToTime(minutes: int) -> str:
    hours = 0
    while minutes > 60:
        minutes -= 60
        hours += 1
    outStr = ""
    if hours > 1:
        outStr += f'{hours} hours '
    if hours == 1:
        outStr += f'{hours} hour '
    if minutes > 1:
        outStr += f'{minutes} minutes'
    if minutes == 1:
        outStr += f'{minutes} minute'
    if not outStr:
        outStr = None
    return outStr


def startVM():
    imgDet = imageDetection.ImageDetector()
    time.sleep(3)
    pos = imgDet.detectImage('Data/Images/start.png')
    if isinstance(pos, int):
        return 0
    mouseHandler = keyboardHandling.MouseHandler()
    mouseHandler.set_pos((pos.left + pos.width / 2, pos.top + pos.height / 2))
    mouseHandler.click(Button="left")
    del imgDet
    del mouseHandler
    return 1


def mao():
    openMao = openAppSites.OpenAppSites()

    openMao.openWebsite("mao")

    del openMao


def isLeapYear(year: int, *, outForm="bool") -> bool | int:
    if outForm == "int":
        return 29 if year % 4 == 0 else 28
    return True if year % 4 == 0 else False


def getDays(year: int, month: int) -> int:
    return isLeapYear(year, outForm="int") if month == 2 else 30 if month % 2 == 0 else 31


def getTomorrow(*, year:int = datetime.datetime.now().year, month:int = datetime.datetime.now().month, date:int = datetime.datetime.now().day) -> str:
    # Checking date                     Special Case of Feb                 # 29th of any month              30th of special months
    if date < 28 or (date == 28 and (month != 2 or isLeapYear(year))) or (date == 29 and month != 2) or (date == 30 and getDays(year, month) == 31):
        return f"{year}:{month}:{date+1}"

    # Checking month
    if month < 12:
        return f"{year}:{month+1}:1"

    # Updating year
    return f"{year+1}:1:1"


def getMonth(month: str) -> int | str:
    match month:
        case 'january':
            return 1
        case 'february':
            return 2
        case 'march':
            return 3
        case 'april':
            return 4
        case 'may':
            return 5
        case 'june':
            return 6
        case 'july':
            return 7
        case 'august':
            return 8
        case 'september':
            return 9
        case 'october':
            return 10
        case 'november':
            return 11
        case 'december':
            return 12
        case _:
            return month


def increaseMonth(month: int, threshold: int):
    for i in range(threshold):
        month = (month % 12) + 1

    return month


def extractDetails(query: str):
    tmrKey = query.find("tomorrow") # Checking for tomorrow key word
    loc = query.find("on") + 3

    # If no keyword
    if loc < 0 and tmrKey < 0:
        return None, None

    # Getting date
    date = ""
    month = ""
    year = datetime.datetime.now().year
    rem = ""
    try:
        if tmrKey > -1:  # In case of keyword tomorrow
            date = getTomorrow()
            loc = tmrKey + 8
            raise ValueError

        while loc < len(query) and query[loc] != " ":  # Getting date
            date += query[loc]
            loc += 1

        # Checking for month
        loc += 1
        while loc < len(query) and query[loc] != " ":
            month += query[loc]
            loc += 1

        month = getMonth(month.lower())
        if type(month) is str:  # If no month
            rem += f"{month} ".capitalize()
            month = datetime.datetime.now().month

            # If date is past
            if int(date) < datetime.datetime.now().day:
                month = increaseMonth(month, 1)
            raise ValueError

        # If previous month or previous date, set for next year
        if month < datetime.datetime.now().month or (month == datetime.datetime.now().month and int(date) < datetime.datetime.now().day):
            year += 1

        raise ValueError

    # Getting reminder
    except ValueError:
        loc += 1

        while loc < len(query):
            rem += query[loc]
            loc += 1

    return [date, rem] if tmrKey > -1 else [f"{year}:{month}:{date}", rem]


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

    if loc < 0:
        loc = query.find("on")

    # Finding starting of time
    try:
        while query[loc] != " ":
            loc += 1
    except IndexError:
        return -1, -1, -1

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
    if "at" not in query and "for" not in query and "on" not in query:
        return None

    alarm = JTime.Alarm()
    hour, minute, second = extractTimeAlarm(query)

    if hour < 0 or minute < 0 or second < 0:
        return None

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
        raise ValueError("That's the wrong value idiot!")

    # In case of half an hour:
    if "half" in query and "hour" in query:
        return 0 if (time == "hour" or time == "second") else 30

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
        if second == 0 and minute != 0:
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
        # Old Condition: while query[endLoc] != " " and endLoc < len(query)-1:, Note: Old condition will ignore everything after whitespace, e.g. 'jarvis open discord please', please will be ignored but in something like 'open kali linux', linux will also be ignored which will cause errors. Current condition ensures that all words are included regardless of the whitespace e.g. 'kali linux' will be included but 'discord please' will also be included which will cause unexpected behaviours. Choose the condition which suits you the best! - Liman
        while endLoc < len(query)-1:
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
    try:
        temp = data.find("div", class_="BNeawe").text
    except Exception:
        temp = "too difficult for me to find, sorry!"
    return temp


def getGreetPhrase():
    return "Good afternoon Sir!"  # To be changed to multiple random phrases by Lafiz


if __name__ == "__main__":
    # print(extractDetails("Set a reminder on 30 October Play Minecraft"))
    print(startVM())