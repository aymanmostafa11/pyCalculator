# importing tkinter library
from tkinter import *
from helpers import *
# making the the calculator interface
window = Tk()

# making the title of the calculator

window.title("my calculator")

# making the border of the calculator
calculatorScreen = Entry(window, width=35, borderwidth=5, state='disabled')
calculatorScreen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

help_label = Label(window, fg='gray', width=30, borderwidth=5)


# defining the different functions of the calculator
operations = ['+', '-', '/', '*']


def button_click(number):
    addCharacterToScreen(calculatorScreen, number)


def button_clear():
    help_label.grid_forget()
    screenClear(calculatorScreen)


def button_delete():
    textOnScreen = calculatorScreen.get()
    # if there's text on screen, remove last letter then clear and add the new text
    if len(textOnScreen) > 0:
        textOnScreen = textOnScreen[:-1]
        screenClear(calculatorScreen)
        addCharacterToScreen(calculatorScreen, textOnScreen)


def button_equal():
    help_label.grid_forget()
    textOnScreen = calculatorScreen.get()
    textOnScreen = changeAnglesInTextToRadians(textOnScreen)
    # if errorCheck(textOnScreen, operations):
    #     value = eval(textOnScreen)
    #     screenClear(calculatorScreen)
    #     addCharacterToScreen(calculatorScreen, value)
    # else:
    #     screenClear(calculatorScreen)
    #     addCharacterToScreen(calculatorScreen, "Syntax Error!")
    textToShow = ""
    try:
        value = eval(textOnScreen)
        # values that are supposed to be 0 but are very small due to calculation errors
        if float(value) < 1e-12:
            value = 0

        textToShow = value
    except:
        textToShow = "Syntax or Math Error!"
    finally:
        screenClear(calculatorScreen)
        addCharacterToScreen(calculatorScreen, textToShow)



def button_operation(op):
    textOnScreen = calculatorScreen.get()
    if not errorCheck(textOnScreen, operations):
        return
    addCharacterToScreen(calculatorScreen, op)

# Scientific Operations
def button_sin():
    addCharacterToScreen(calculatorScreen, "sin(")

def button_cos():
    addCharacterToScreen(calculatorScreen, "cos(")

def button_tan():
    addCharacterToScreen(calculatorScreen, "tan(")

def button_log():
    addCharacterToScreen(calculatorScreen, "log(")
    help_label.config(text="Log usage : log(number, base)")
    help_label.grid(row=0,column=3,columnspan=2)

def button_sqrt():
    addCharacterToScreen(calculatorScreen, "sqrt(")
    help_label.config(text="sqrt usage : sqrt(number)")
    help_label.grid(row=0, column=3, columnspan=2)

def button_pow():
    addCharacterToScreen(calculatorScreen, "pow(")
    help_label.config(text="Power usage : pow(number, power)")
    help_label.grid(row=0, column=3, columnspan=2)

# initializing buttons
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

button_add = Button(window, text="+", padx=39, pady=20, command=lambda: button_operation('+'))

button_equal = Button(window, text="=", padx=87, pady=20, command=button_equal)

button_clear = Button(window, text="clear", padx=79, pady=20, command=button_clear)

button_delete = Button(window, text="del", padx=40, pady=20, command=button_delete)

button_multiply = Button(window, text="*", padx=40, pady=20, command=lambda: button_operation('*'))

button_subtract = Button(window, text="-", padx=41, pady=20, command=lambda: button_operation('-'))

button_divide = Button(window, text="/", padx=41, pady=20, command=lambda: button_operation('/'))

button_right_bracket = Button(window, text=")", padx=41, pady=20, command=lambda: button_click(')'))
button_left_bracket = Button(window, text="(", padx=41, pady=20, command=lambda: button_click('('))

# Scientific Buttons
button_sin = Button(window, text="sin", padx=40, pady=20, command=button_sin)
button_cos = Button(window, text="cos", padx=40, pady=20, command=button_cos)
button_tan = Button(window, text="tan", padx=40, pady=20, command=button_tan)
button_log = Button(window, text="log", padx=40, pady=20, command=button_log)
button_sqrt = Button(window, text="sqrt", padx=40, pady=20, command=button_sqrt)
button_pow = Button(window, text="pow", padx=40, pady=20, command=button_pow)
button_comma = Button(window, text=",", padx=40, pady=20, command=lambda: button_click(','))
button_dot = Button(window, text=".", padx=40, pady=20, command=lambda: button_click('.'))

# placing the buttons of the calculator
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_tan.grid(row=3, column=3)
button_pow.grid(row=3, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_cos.grid(row=2, column=3)
button_sqrt.grid(row=2, column=4)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_sin.grid(row=1, column=3)
button_log.grid(row=1, column=4)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_delete.grid(row=4, column=3)
button_right_bracket.grid(row=5, column=3)
button_comma.grid(row=4, column=4)
button_dot.grid(row=5, column=4)

button_multiply.grid(row=6, column=1)
button_subtract.grid(row=6, column=2)
button_divide.grid(row=6, column=0)
button_left_bracket.grid(row=6, column=3)

window.mainloop()

