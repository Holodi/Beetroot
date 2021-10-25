# Custom exception
import datetime

class CustomException(Exception):

    def __init__(self, message: str = "Помилка!"):
        self.message = message
        super().__init__(self.message)
        self.current_time = datetime.today()
        with open("log.txt", "a") as self.file:
            self.file.write(f"{self.current_time} - {message}!\n")

    def __repr__(self):
        return str(self.current_time)

raise CustomException("Custom Exception")