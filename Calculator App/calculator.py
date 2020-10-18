# Simple Calculator
# by TokyoEdtech
# Python 3.8 using Geany Editor
# Ubuntu Linux (Mac and Windows Compatible)
# Topics: tkinter, grid geometry manager, eval, try/except, lambda

import tkinter

root = tkinter.Tk()
root.title("Calculator")

expression = ""

# Create functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)
            
# Create GUI
label_result = tkinter.Label(root, text="")
label_result.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(root, text="1", command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3", command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/", command=lambda: add("/"))
button_divide.grid(row=1, column=3)

button_4 = tkinter.Button(root, text="4", command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text="*", command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

button_7 = tkinter.Button(root, text="7", command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_subtract = tkinter.Button(root, text="-", command=lambda: add("-"))
button_subtract.grid(row=3, column=3)

button_clear = tkinter.Button(root, text="C", command=lambda: clear())
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(root, text="0", command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".", command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+", command=lambda: add("+"))
button_add.grid(row=4, column=3)

button_equals = tkinter.Button(root, text="=", width=16, command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)

root.mainloop()
