import math
from tkinter import END, Button


def addCharacterToScreen(screen, character):
    """
        Enables the screen to add a character then locks it again to prevent user from typing manually
        Parameters:
            screen :  tkinter.Entry  screen to add character to
            character : character to be added
    """
    screen.config(state='normal')
    elementsOnScreen = screen.get()
    screen.insert(len(elementsOnScreen), str(character))
    screen.config(state='disabled')


def screenClear(screen):
    screen.config(state='normal')
    screen.delete(0, END)
    screen.config(state='disabled')


def extractNumbersAndOperations(text, operations):
    """
        Parameters:
           text : string to extract numbers and operations from
           operations : list of supported operations
        Returns:
            list containing each number and each operation separately
    """
    extractedElements = []
    numberString = ""

    for character in text:
        # if it's a number add it to number string
        if character not in operations:
            numberString += character
        # if it's an operation then the number is finished so add it to extracted elements
        else:
            extractedElements.append(numberString)
            numberString = ""  # reset number string for next numbers
            extractedElements.append(character)  # add found operation to extracted elements

    # to add the last number since the loop exits before it's added
    if numberString != "":
        extractedElements.append()

    return extractedElements


def evaluateExpression(extractedElements):
    """
        Parameters:
           extractedElements : elements to evaluate
        Returns:
            value of expression or None to indicate an error while evaluating
    """
    pass


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

    # check if trying to enter two operations next to each other
    # or at the end of text to evaluate
    if (screenText[-1] in operations):
        return False

    # check if trying to enter operation as a first character
    if (len(screenText) == 0):
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
    for character in mainText[index:]:
        if character == ')':
            break
        else:
            angleString += character
    angle = float(angleString)
    angle = angle * (math.pi / 180)
    mainText = mainText.replace(angleString, str(angle))
    return mainText

