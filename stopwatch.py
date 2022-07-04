import time
import os

seconds = 55
minutes = 59
hours = 0

while True:
    os.system("cls")
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    if hours < 1:
        if minutes < 1:
            print(f"Currently going for: {seconds} seconds!")
        else:
            print(f"Currently going for: {minutes} minutes and {seconds} seconds!")
    else:
        print(f"Currently going for: {hours} hours, {minutes} minutes and {seconds} seconds!")
    seconds += 1
    time.sleep(1)