# This file handles all the speech output of Jarvis

# Imports
import pyttsx3


# Main Class
class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")  # Initializing pyttsx3 engine
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)  # Setting the second voice installed (subject to change)


    def speak(self, audio):
        self.engine.say(audio)  # Voice output
        self.engine.runAndWait()


if __name__ == "__main__":
    speaker = Speaker()
    speaker.speak("hehe boi it's me mar- i mean Jarvis")
    del speaker