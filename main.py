# importing tkinter library
from tkinter import *
from helpers import *
from math import sin, cos, tan, sqrt, pow, log

MAX_PRECISION = 7  # number of decimal digits

# making the the calculator interface
window = Tk()

# making the title of the calculator
window.title("My Calculator")

# making the border of the calculator
calculatorScreen = Entry(window, width=35, borderwidth=5, state='disabled')
calculatorScreen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

help_label = Label(window, fg='gray', width=30, borderwidth=5)


""" 
    =====================
    Basic Functionalities
    =====================
"""
operations = ['+', '-', '/', '*']


def button_click(number):
    addTextToScreen(calculatorScreen, number)


def button_clear():
    help_label.grid_forget()  # remove help message
    screenClear(calculatorScreen)


def button_delete():
    textOnScreen = calculatorScreen.get()
    # if there's text on screen, remove last letter then clear and add the new text
    if len(textOnScreen) > 0:
        textOnScreen = textOnScreen[0: -1]  # access string without the last element
        screenClear(calculatorScreen)
        addTextToScreen(calculatorScreen, textOnScreen)


def button_equal():
    help_label.grid_forget()

    textOnScreen = calculatorScreen.get()
    textOnScreen = changeAnglesInTextToRadians(textOnScreen)
    textToShow = ""
    try:
        value = eval(textOnScreen)
        value = round(value, MAX_PRECISION)  # to avoid redundant long numbers (eg 1.00000000002)
        # values that are supposed to be 0 but are very small due to calculation errors
        if 0 < float(value) < 1e-12:
            value = 0
        elif float(value) > 1e15:  # operation that resulted in infinity
            value = "Math Error!"

        textToShow = value
    except:
        textToShow = "Syntax or Math Error!"
    finally:
        screenClear(calculatorScreen)
        addTextToScreen(calculatorScreen, textToShow)


def button_operation(op):
    textOnScreen = calculatorScreen.get()
    if not errorCheck(textOnScreen, operations):
        return
    addTextToScreen(calculatorScreen, op)


""" 
    =====================
    Scientific Operations
    =====================
"""
def button_sin():
    addTextToScreen(calculatorScreen, "sin(")


def button_cos():
    addTextToScreen(calculatorScreen, "cos(")


def button_tan():
    addTextToScreen(calculatorScreen, "tan(")


def button_log():
    addTextToScreen(calculatorScreen, "log(")
    help_label.config(text="Log usage : log(number, base)")
    help_label.grid(row=0, column=3, columnspan=2)


def button_sqrt():
    addTextToScreen(calculatorScreen, "sqrt(")
    help_label.config(text="sqrt usage : sqrt(number)")
    help_label.grid(row=0, column=3, columnspan=2)


def button_pow():
    addTextToScreen(calculatorScreen, "pow(")
    help_label.config(text="Power usage : pow(number, power)")
    help_label.grid(row=0, column=3, columnspan=2)


""" 
    =====================
            GUI
    =====================
"""
# Creating Buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_clear = Button(window, text="clear", padx=78, pady=20, command=button_clear)
button_delete = Button(window, text="del", padx=40, pady=20, command=button_delete)

button_add = Button(window, text="+", padx=39, pady=20, command=lambda: button_operation('+'))
button_multiply = Button(window, text="*", padx=40, pady=20, command=lambda: button_operation('*'))
button_subtract = Button(window, text="-", padx=41, pady=20, command=lambda: button_operation('-'))
button_divide = Button(window, text="/", padx=41, pady=20, command=lambda: button_operation('/'))
button_equal = Button(window, text="=", padx=87, pady=20, command=button_equal)

# Scientific Buttons
button_sin = Button(window, text="sin", padx=40, pady=20, command=button_sin)
button_cos = Button(window, text="cos", padx=39, pady=20, command=button_cos)
button_tan = Button(window, text="tan", padx=40, pady=20, command=button_tan)
button_log = Button(window, text="log", padx=40, pady=20, command=button_log)
button_sqrt = Button(window, text="sqrt", padx=40, pady=20, command=button_sqrt)
button_pow = Button(window, text="pow", padx=40, pady=20, command=button_pow)

button_right_bracket = Button(window, text=")", padx=50, pady=20, command=lambda: button_click(')'))
button_left_bracket = Button(window, text="(", padx=45, pady=20, command=lambda: button_click('('))
button_comma = Button(window, text=",", font=10, padx=45, pady=13, command=lambda: button_click(','))
button_dot = Button(window, text=".", font=10, padx=40, pady=14, command=lambda: button_click('.'))


# placing the buttons of the calculator

# Row 1
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_sin.grid(row=1, column=3)
button_log.grid(row=1, column=4)

# Row 2
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_cos.grid(row=2, column=3)
button_sqrt.grid(row=2, column=4)

# Row 3
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_tan.grid(row=3, column=3)
button_pow.grid(row=3, column=4)

# Row 4
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_delete.grid(row=4, column=3)
button_comma.grid(row=4, column=4)

# Row 5
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_left_bracket.grid(row=5, column=3)
button_right_bracket.grid(row=5, column=4)

# Row 6
button_multiply.grid(row=6, column=1)
button_subtract.grid(row=6, column=2)
button_divide.grid(row=6, column=0)

button_dot.grid(row=6, column=3)


window.mainloop()

