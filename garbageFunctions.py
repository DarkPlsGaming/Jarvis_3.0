import json
from urllib.request import urlopen
import requests
import os
from bs4 import BeautifulSoup


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
    print(getTemperature())