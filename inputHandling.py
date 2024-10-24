import speech_recognition as sr
from outputHandling import Speaker


class InputListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = Speaker()


    # Private Method
    def __recognizeAudio(self, audio):
        try:
            query: str = self.recognizer.recognize_google(audio, language="en-in")
            return query.lower()

        except:
            self.speaker.speak("Sorry Sir, I did not get that!")
            return None


    def startListen(self) -> str:
        # Input
        with sr.Microphone() as source:
            self.recognizer.pause_threshold = 1
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