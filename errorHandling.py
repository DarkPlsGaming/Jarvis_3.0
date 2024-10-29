# This file handles the proper handling of any exceptions that may arise in J3

# Imports
import traceback
import fileHandling
import datetime


class Error:
    def __init__(self, file, line, function, code):
        self.file = file
        self.line = line
        self.function = function
        self.code = code


class ErrorHandling:
    def __init__(self):
        self.fileOutput = fileHandling.FileHandler("Data/logs.txt")
        self.errors = []


    def __saveOutput(self, err):
        output = f"Error log on: {datetime.datetime.now().strftime("%D : %H:%M")}\n"
        output += f"The following error occurred: {err}\n\n"

        for error in self.errors:
            output += f"In File: {error.file} Function: {error.function} on {error.line} Code: {error.code} caused an error!\n\n"

        output += "\n\n"
        self.fileOutput.writeFile(output, openMode="a")


    def handleError(self, errorTraceback, err):
        tb = traceback.extract_tb(errorTraceback)

        for file, line, function, code in tb:
            self.errors.append(Error(file, line, function, code))

        # Handle specific Errors
        # To be done by Lord Lafiz

        self.__saveOutput(err)