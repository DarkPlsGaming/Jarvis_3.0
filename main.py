from commands import Commands


class InitJarvis:
    def __init__(self):
        self.commands = Commands()


    def start(self):
        self.commands.greet()


if __name__ == "__main__":
    jarvis = InitJarvis()
    jarvis.start()

