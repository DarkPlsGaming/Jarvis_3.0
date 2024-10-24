import commands


class CommandHandling:
    def __init__(self):
        self.command = commands.Commands()


    def handleCommand(self, query: str):
        if "open" in query:
            self.command.dealOpen(query)

        if "shut" in query and "down" in query:
            self.command.shutDown()

        if "what" in query and "temperature" in query:
            self.command.getTemp()
