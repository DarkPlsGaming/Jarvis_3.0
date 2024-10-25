# This file is the main structure of Jarvis 3.0

# Inputs
from commands import Commands
import keyboardHandling
import inputHandling
import commandHandling


class InitJarvis:
    def __init__(self):
        # noinspection GrazieInspection
        self.commands = Commands()  # Initializing commands for the greet() command
        self.keyHandler = keyboardHandling.KeyboardHandler()  # Initializing for listening to user key
        self.inpHandler = inputHandling.InputListener()  # Initialized for speech input
        self.cmdHandler = commandHandling.CommandHandling()  # Initialized for command handling


    def __startListen(self):  # Listening for particular user key for activation
        while True:
            if self.keyHandler.listenForKey("Key.ctrl_r") == 1:  # When key is pressed
                self.handleQuery(self.inpHandler.startListen())  # Starting voice input


    def handleQuery(self, query: str):
        # print(query)
        self.cmdHandler.handleCommand(query)  # Sending command to commandHandling.py file


    def start(self):
        self.commands.greet()  # Greeting the user
        self.__startListen()  # Starting listening for key input


if __name__ == "__main__":
    jarvis = InitJarvis()
    jarvis.start()

