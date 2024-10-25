# This file consists of all the commands that is used by the "commandHandling" file

# Imports
import garbageFunctions as gF  # All the non-important functions are located here
from outputHandling import Speaker  # Output Class


class Commands:
    def __init__(self):
        self.speaker = Speaker()  # Initializing output class


    def selfTerminate(self):
        self.speaker.speak("Terminating myself!")
        gF.terminate()


    def shutDown(self):
        self.speaker.speak("Shutting Off!")
        gF.shutdown()


    def getTemp(self):
        self.speaker.speak(f"The temperature in {gF.getLocation()} is {gF.getTemperature()}")


    def greet(self):
        phrase = gF.getGreetPhrase()
        temp = f"The temperature outside is {gF.getTemperature()}"
        self.speaker.speak(phrase + temp)


    def dealOpen(self, query: str):  # All queries related to opening applications or websites are processed here
        app = gF.openWebApps(query)
        if not app:
            self.speaker.speak("Sorry, the application was not found!")
            return None
        self.speaker.speak(f"Opening {app}")