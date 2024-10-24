import garbageFunctions as gF
from outputHandling import Speaker


class Commands:
    def __init__(self):
        self.speaker = Speaker()


    def greet(self):
        phrase = gF.getGreetPhrase()
        temp = f"The temperature outside is {gF.getTemperature()}"
        self.speaker.speak(phrase + temp)