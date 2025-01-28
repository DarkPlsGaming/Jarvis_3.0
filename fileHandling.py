import json


# noinspection PyBroadException,PyTypeChecker
class FileHandler:
    def __init__(self, path: str):
        self.path: str = path


    def writeFile(self, data, *, jsonOut: bool = False, openMode: str = "w") -> int | None:
        try:
            with open(self.path, f"{openMode}") as file:
                if jsonOut:
                    json.dump(data, file, indent=4)
                else:
                    file.write(data)
                return 1

        except FileNotFoundError:
            print("File was not found!")
            return None

        except Exception:
            print("There was an error loading the file!")
            return None


    def readFile(self, *, jsonOut: bool = False):
        try:
            with open(self.path, "r") as file:
                if jsonOut:
                    data: dict = json.load(file)
                else:
                    data: str = file.read()

            return data

        except Exception:
            return None


    def changeFile(self, path: str) -> None:
        self.path = path
        return None


if __name__ == "__main__":
    fh = FileHandler("Data/reminders.json")

    fh.writeFile({"a": "b"}, jsonOut=True, openMode='a')