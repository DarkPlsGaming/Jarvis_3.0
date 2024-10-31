# This file installs all the necessary libraries of Python needed to run J3

# Imports
import os
import fileHandling
import socket


class InstallPackages:
    def __init__(self):
        dataLoad = fileHandling.FileHandler("Data/ExternalPackages.txt")
        self.packages: list = dataLoad.readFile().splitlines()


    @staticmethod
    def __installPackage(package: str):
        os.system(f"pip install {package}")


    @staticmethod
    def __checkInternet() -> bool:
        # noinspection PyBroadException
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=5)  # Attempting to connect to google
            return True

        except Exception:
            return False


    @staticmethod
    def __getConfirmation() -> bool:
        userInp = input("Do you want to continue [y/n]... ").lower()

        if userInp == "1" or userInp == "y" or userInp == "yes":
            return True

        return False


    def __printPackages(self):
        print(", ".join(self.packages))


    def __installPackages(self):
        for package in self.packages:
            self.__installPackage(package)


    def install(self) -> bool:
        try:
            print("Checking for internet connectivity..")
            if self.__checkInternet is False:
                print("Error! Please check your internet connection and try again later..")
                return False

            print("Jarvis 3 will proceed to install the following packages:")
            self.__printPackages()
            if not self.__getConfirmation():
                print("Exiting..")
                return False
            print("Starting Installation Process..")
            self.__installPackages()
            print("Package installation was successful!")
            input("You will have to restart J3. Press Enter to continue...")

        except Exception as e:
            print("Sorry an error occurred while installing the packages. Please contact the software developer to resolve this issue.")
            raise e

if __name__ == "__main__":
    install = InstallPackages()
    install.install()