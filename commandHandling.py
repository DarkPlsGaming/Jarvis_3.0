# The purpose of this file is to look for specific keywords in the user query and perform the appropriate action.

# Imports
import commands


# Main Class
class CommandHandling:
    def __init__(self):
        self.command = commands.Commands()  # An instance of the class "Commands"


    # The main method that handles user query
    def handleCommand(self, query: str):
        if "wow" in query:
            self.command.wow()


        if "mau" in query:
            self.command.mao()

        if "set" in query and "reminder" in query:
            self.command.setReminder(query)  # UNDER DEVELOPMENT

        if "set" in query and "alarm" in query:
            self.command.setAlarm(query)

        if "set" in query and "timer" in query:
            self.command.setTimer(query)

        if "terminate" in query:
            self.command.selfTerminate()

        if "open" in query:
            self.command.dealOpen(query)

        if "shut" in query and "down" in query:
            self.command.shutDown()

        if "what" in query and "temperature" in query:
            self.command.getTemp()
