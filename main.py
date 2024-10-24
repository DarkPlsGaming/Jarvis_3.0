import outputHandling


class InitJarvis:
    def __init__(self):
        self.speaker = outputHandling.Speaker()


    def greet(self):
        self.speaker.speak("Good morning Sir, the temperature outside is 9 degree Celsius")


    def start(self):
        self.greet()


if __name__ == "__main__":
    jarvis = InitJarvis()
    jarvis.start()

