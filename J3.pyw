# This file is the main structure of Jarvis 3.0 and runs in background

# Importing Error Handling file
import errorHandling

# Checking for external packages
try:
    import commands
    import keyboardHandling
    import inputHandling
    import commandHandling
    import discordHandling
    import scheduleManager
    import activityDetector
except Exception as e:  # Error Handling
    errorHandling.ErrorHandling().handleError(e.__traceback__, e, '')  # Installing packages


class InitJarvis:
    def __init__(self):
        # noinspection GrazieInspection
        self.errorHandler = errorHandling.ErrorHandling()
        self.commands = commands.Commands()  # Initializing commands for the greet() command
        self.keyHandler = keyboardHandling.KeyboardHandler()  # Initializing for listening to user key
        self.inpHandler = inputHandling.InputListener()  # Initialized for speech input
        self.cmdHandler = commandHandling.CommandHandling()  # Initialized for command handling
        self.schManager = scheduleManager.ScheduleManager()  # Initialized for Schedule Handling
        self.disHandler = discordHandling.DiscordHandler()  # Initializer for Discord Handler
        self.actHandler = activityDetector.ActivityDetection()
        self.query = None

    def __startListen(self):  # Listening for particular user key for activation
        while True:
            if self.keyHandler.listenForKey("Key.ctrl_r") == 1:  # When right control key is pressed
                self.handleQuery(self.inpHandler.startListen())  # Starting voice input and processing it


    def __checkForReminders(self):
        self.commands.checkReminder()  # Checks for any reminders set for today

    def __startTodaySchedule(self):
        self.schManager.startSchedule()

    def __startDiscord(self):
        self.disHandler.run()

    def __startActivityListener(self):
        self.actHandler.check()  # Checking for report date
        self.actHandler.start()  # Starting Activity Detection in background

    def handleQuery(self, query: str):
        # print(query)
        self.query = query  # Setting query
        self.cmdHandler.handleCommand(query)  # Sending command to commandHandling.py file


    def start(self):
        try:
            self.commands.greet()  # Greeting the user
            self.__checkForReminders()  # Checking for possible reminders set up for today
            self.__startTodaySchedule()  # Starting today's schedule
            self.__startDiscord()  # Starting Discord Bot Services
            self.__startActivityListener()  # Starting Activity Detection
            self.__startListen()  # Starting listening for key input

        except Exception as ex:  # Error Handling
            self.errorHandler.handleError(e.__traceback__, ex, self.query)

if __name__ == "__main__":
    jarvis = InitJarvis()
    jarvis.start()

