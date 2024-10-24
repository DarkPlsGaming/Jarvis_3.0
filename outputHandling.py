import pyttsx3


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)


    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()


if __name__ == "__main__":
    speaker = Speaker()
    speaker.speak("Then I used the whip at them just as you asked me to")
    del speaker