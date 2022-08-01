import os
import random
import time
import pyautogui


def HelloWorld():
    print("Hello World")
def randomNum(LowestNumber: int, HighestNumber: int):
    return random.randint(LowestNumber, HighestNumber)
def printRandomNum(LowestNumber: int, HighestNumber: int):
    print(random.randint(LowestNumber, HighestNumber))
def printMousePosition():
    time.sleep(3)
    print(pyautogui.position())
def getMousePosition():
    return pyautogui.position()
def mouseClick(x: int, y: int):
    pyautogui.click(x, y)
def readFile(fileName: str):
    with open(fileName, "r") as file:
        return file.read()
def printReadFile(fileName: str):
    with open(fileName, "r") as file:
        contents = file.read()
    print(contents)
def writeFile(fileName: str, userInput):
    with open(fileName, "w") as file:
        file.write(userInput)
def clearFile(filename: str):
    with open(filename, "w") as file:
        file.write("")
def resetTerminal():
    os.system("cls")
def sleep(timeSleeping: int):
    time.sleep(timeSleeping)
def toString(input: any):
    return f"{input}"
