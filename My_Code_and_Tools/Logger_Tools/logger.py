import os
from datetime import datetime
from typing import Optional

def get_now_time() -> str:
    now_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return now_time

def get_now_time_milliseconds() -> str:
    milliseconds_time = datetime.now().strftime("%m_%d_%H_%M_%S_%f")
    return milliseconds_time

class Logger:
    """
    This class is used to log any information we need in the program.
    Here is the way to use this class:

    eg:
        logger = Logger("setting", "./Logger/")
        logger.info("This is the setting.")
    """
    def __init__(self, logger_file_name: str, logger_file_path: Optional[str]):
        if not os.path.exists(logger_file_path):
            os.mkdir(logger_file_path)
        open(f"{logger_file_path}\{logger_file_name}.txt", "w").close()
        self.logger_file_path = f"{logger_file_path}\{logger_file_name}.txt"

    def info(self, message: str) -> None:
        """
        This method is used to log information.
        """
        time = get_now_time_milliseconds()
        file = open(self.logger_file_path, "a")
        file.write(f"Info_{time}:\t{message}\n")
        file.close()

    def warning(self, message: str) -> None:
        """
        This method is used to log warning.
        """
        time = get_now_time_milliseconds()
        file = open(self.logger_file_path, "a")
        file.write(f"Warning_{time}:\t{message}\n")
        file.close()

    def error(self, message: str) -> None:
        """
        This method is used to log error.
        """
        time = get_now_time_milliseconds()
        file = open(self.logger_file_path, "a")
        file.write(f"Error_{time}:\t{message}\n")
        file.close()