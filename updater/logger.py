"""
==========================================================
Azziano Marathi News
logger.py

Purpose:
    Simple logging utility.

Features
--------
✓ Console logging
✓ File logging
✓ Automatic log folder creation
✓ Timestamp
✓ INFO / WARNING / ERROR levels
✓ Works with __file__ and interactive environments

Version : 1.0
==========================================================
"""

from pathlib import Path
from datetime import datetime


# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

try:
    # Running as a normal Python file
    BASE_DIR = Path(__file__).resolve().parent.parent
except NameError:
    # Running in IDLE / Jupyter / Interactive Window
    BASE_DIR = Path.cwd()

LOG_FOLDER = BASE_DIR / "logs"
LOG_FILE = LOG_FOLDER / "update.log"

LOG_FOLDER.mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------
# Internal Logger
# ----------------------------------------------------------

def _write(level, message):
    """
    Write log message to console and log file.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{timestamp}] [{level}] {message}"

    # Console
    print(line)

    # File
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(line + "\n")
    except Exception as ex:
        print(f"Unable to write log file: {ex}")

    return line


# ----------------------------------------------------------
# Public Functions
# ----------------------------------------------------------

def info(message):
    return _write("INFO", message)


def warning(message):
    return _write("WARNING", message)


def error(message):
    return _write("ERROR", message)


# ----------------------------------------------------------
# Session Functions
# ----------------------------------------------------------

def start_session():

    separator = "=" * 60

    info(separator)
    info("News Update Started")
    info(separator)


def end_session():

    separator = "=" * 60

    info(separator)
    info("News Update Finished")
    info(separator)


# ----------------------------------------------------------
# Test (Runs only when executed directly)
# ----------------------------------------------------------

if __name__ == "__main__":

    start_session()

    info("This is an INFO message.")

    warning("This is a WARNING message.")

    error("This is an ERROR message.")

    end_session()

    print()
    print("Log file created at:")
    print(LOG_FILE)