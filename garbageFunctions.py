import json
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

def getLocation():
    data = json.load(urlopen("http://ipinfo.io/json"))
    city = data.get("city")
    region = data.get("region")

    return f"{region}, {city}"


def getTemperature():
    # Getting Location
    location = getLocation()

    # Searching on Google
    search = "Temperature in "
    url = f"https://www.google.com/search?q={search + location}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text

    return temp



def getGreetPhrase():
    return "Good afternoon Sir!"



if __name__ == "__main__":
    print(getTemperature())