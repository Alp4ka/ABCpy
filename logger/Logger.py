from enum import Enum
import datetime


class LogType(Enum):
    WARNING = 0,
    ERROR = 1,
    INFO = 2,
    DEBUG = 3


def log(msg: str, log_type=None):
    """
        Log message.

        Args:
            msg: Message to log.
            log_type: log type enumeration.
    """
    if log_type is None:
        log_type = LogType.INFO
    print(f"[{log_type.name} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}]")


def log_file(msg: str, output_file: str, log_type=None):
    """
        Log into file.

        Args:
            msg: Message to log.
            output_file: output file
            log_type: log type enumeration.
    """
    if log_type is None:
        log_type = LogType.INFO
    with open(output_file, "a") as f:
        f.write(f"[{log_type.name} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}]\n")
