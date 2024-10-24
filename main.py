from commands import Commands
import keyboardHandling
import inputHandling


class InitJarvis:
    def __init__(self):
        self.commands = Commands()
        self.keyHandler = keyboardHandling.KeyboardHandler()
        self.inpHandler = inputHandling.InputListener()


    def handleQuery(self, query: str):
        print(query)


    def __startListen(self):
        while True:
            if self.keyHandler.listenForKey() == 1:
                self.handleQuery(self.inpHandler.startListen())


    def start(self):
        self.commands.greet()
        self.__startListen()


if __name__ == "__main__":
    jarvis = InitJarvis()
    jarvis.start()

