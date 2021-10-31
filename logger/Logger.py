from enum import Enum
import datetime

class LogType(Enum):
    WARNING = 0,
    ERROR = 1,
    INFO = 2,
    DEBUG = 3

class Loggerinho:
    @staticmethod
    def log(msg:str, log_type = None):
        if log_type is None:
            log_type = LogType.INFO
        print(f"[{log_type.name} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}]")

