from tkinter import END


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
