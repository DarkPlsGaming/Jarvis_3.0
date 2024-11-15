# This file consists of all the commands that is used by the "commandHandling" file

# Imports
import garbageFunctions as gF  # All the non-important functions are located here
from outputHandling import Speaker  # Output Class


class Commands:
    def __init__(self):
        self.speaker = Speaker()  # Initializing output class


    def wow(self):
        gF.mao()
        self.speaker.speak("""\
        It's mao, not wow, go and correct your english first. He was a very kind (especially to farmers) 
        and talented person. He was very slim and loved all his wives. He also had very long and curly hair. He saved 80 million
        farmers from their miseries and also invented the computer which was his side project in France. He did not fail any of his exams
        and that was a lie made by his enemies to make him look bad. He loved all religions and was a pacifist, unfortunately his
        descendant Farhan became bad and ugly and bold and quite short, and starting spending 6 hours in Prakash everyday.
        He also now spends rest of his time watching anime and sleeping on anime waifu pillows.""")


    def mao(self):
        gF.mao()
        self.speaker.speak("Mao, also popularly known as Hilal Sir was a great man who brought peace to 80 million farmers")

    def setReminder(self, query: str):
        date = gF.setReminder(query)

        if not date:
            self.speaker.speak("Sorry sir, there was an error setting up the reminder! Please try again")
            return

        self.speaker.speak(f"Setting reminder on {date}")


    def checkReminder(self):
        output = gF.checkTimer()

        if not output:
            return output

        self.speaker.speak("You have a reminder set for today sir!")
        gF.remindTimer(f"Remember to {output}!")


    def setAlarm(self, query):
        output = gF.setAlarm(query)
        if not output:
            self.speaker.speak("Sorry Sir, there was an error setting up the timer. Please make sure the timer is set for today and not tomorrow!")
            return None

        self.speaker.speak(f"Setting alarm at {output}")


    def setTimer(self, query):
        self.speaker.speak(f"Setting timer for {gF.setTimer(query)}!")


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


if __name__ == "__main__":
    command = Commands()
    command.wow()