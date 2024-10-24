import garbageFunctions as gF
from outputHandling import Speaker


class Commands:
    def __init__(self):
        self.speaker = Speaker()


    def shutDown(self):
        self.speaker.speak("Shutting Off!")
        gF.shutdown()


    def getTemp(self):
        self.speaker.speak(f"The temperature in {gF.getLocation()} is {gF.getTemperature()}")


    def greet(self):
        phrase = gF.getGreetPhrase()
        temp = f"The temperature outside is {gF.getTemperature()}"
        self.speaker.speak(phrase + temp)


    def dealOpen(self, query: str):
        app = gF.openWebApps(query)

        if not app:
            self.speaker.speak("Sorry, the application was not found!")
            return None

        self.speaker.speak(f"Opening {app}")