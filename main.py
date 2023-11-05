# Project NS-Stations zuil Lucas Baneke
# Documentation used:

# Imports
from datetime import datetime
import datetime
import csv
from pathlib import Path
import time


# Init stuff

# File writing functions
def CSV_Creator():
    with open('combined_file.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Timestamp", "User", "Message", "Station"])
        writer.writeheader()


def ReceiveInfoFromTkinter(data):
    if data[0] is None or data[0] is "":
        data[0] = "Annoniem"

    with open('combined_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # NOTE: data[0] is the name, data[1] is the main message, data[2] is the station
        writer.writerow([DateGrabber(), TimeStampGrabber(), data[0], data[1], data[2]])


# Helper functions
def DateGrabber():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def TimeStampGrabber():
    return time.time()
