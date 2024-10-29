# This file contains all the methods related to taking user input

# Imports
import speech_recognition as sr
from outputHandling import Speaker


# Main Class
class InputListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()  # Initializing an instance of speech input
        self.speaker = Speaker()  # Initializing an instance of the Speaker() class for speech output


    # Private Method
    # noinspection PyBroadException,PyUnresolvedReferences
    def __recognizeAudio(self, audio):
        try:
            query: str = self.recognizer.recognize_google(audio, language="en-in")  # Recognizing using google
            return query.lower()

        except Exception:
            self.speaker.speak("Sorry Sir, I did not get that!")  # In case of an unexpected exception
            return None


    # Starts listening for speech input
    def startListen(self) -> str:
        # Input
        with sr.Microphone() as source:
            self.recognizer.pause_threshold = 2
            audio = self.recognizer.listen(source)

        # Recognition
        query: str | None = self.__recognizeAudio(audio)

        # Error Handling
        if query is None:
            return self.startListen()

        # Returning User Query
        return query


if __name__ == "__main__":
    inputStart = InputListener()

    print(inputStart.startListen())