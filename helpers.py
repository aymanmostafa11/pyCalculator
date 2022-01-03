import math
from tkinter import END, Button


def addTextToScreen(screen, text):
    """
        Enables the screen to add text then locks it again to prevent user from typing manually
        Parameters:
            screen :  tkinter.Entry  screen to add character to
            text : text to be added
    """
    screen.config(state='normal')
    elementsOnScreen = screen.get()
    screen.insert(len(elementsOnScreen), str(text))
    screen.config(state='disabled')


def screenClear(screen):
    screen.config(state='normal')
    screen.delete(0, END)
    screen.config(state='disabled')


def errorCheck(screenText, operations):
    """
        Checks if input makes sense to the current expression on screen
        Parameters:
           screenText : current Text on screen
           operations : list of supported operations
        Returns:
            True : if text is valid
            False : if there's a problem in the text
    """

    # check if trying to enter operation as a first character
    if len(screenText) == 0:
        return False

    # check if trying to enter two operations next to each other
    # or at the end of text to evaluate
    if screenText[-1] in operations:
        return False

    return True


def changeAnglesInTextToRadians(text):
    """
        Since math library in python takes the angles as radians this function
        locates angles in string and converts it to radians
    :param text:
    :return: text after converting angles to radians
    """
    text = str(text)
    text = findTrigFunctionAndReplaceAngle(text, "sin(")
    text = findTrigFunctionAndReplaceAngle(text, "cos(")
    text = findTrigFunctionAndReplaceAngle(text, "tan(")
    return text


def findTrigFunctionAndReplaceAngle(mainText, textToFind):
    """
    Helper function for changeAnglesInTextToRadians
    :param textToFind: sin cos or tan
    :return: text after converting angle
    """
    index = mainText.find(textToFind)
    # if not found return
    if index == -1:
        return mainText

    index += len(textToFind)
    angleString = ""
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for character in mainText[index:]:
        if character == ')':
            break
        elif character in numbers:  # make sure the character is a number
            angleString += character
        else:  # if invalid character found return
            return mainText

    if angleString == "":
        return mainText

    angle = float(angleString)
    angle = angle * (math.pi / 180)
    mainText = mainText.replace(angleString, str(angle))
    return mainText





