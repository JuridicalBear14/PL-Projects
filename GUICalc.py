from tkinter import *

root = Tk()

root.title("Calculator")

entry = Entry(root, width = 50)
entry.grid(row = 0, columnspan = 10)


numButtons = []
operator = ""
num1 = 0

#Creates the number buttons and places them on screen
for i in range(9):

    numButtons.append(Button(root, padx = 50, pady = 50, text = str(i + 1), command = lambda m = i + 1: entry.insert(len(entry.get()), str(m))))
    numButtons[i].grid(row = int(i / 3) + 1, column = (i + 3) % 3)

def operation(op):
    global operator
    global num1
    global entry

    if (op == "+"):
        operator = "+"
        num1 = entry.get()
        entry.delete(first = 0, last = END)

def equal():
    global operator
    global num1
    global entry

    if (operator == "+"):
        num2 = entry.get()
        entry.delete(first = 0, last = END)
        entry.insert(0, float(num1) + float(num2))


plus = Button(root, padx = 50, pady = 50, text = "+", command = lambda: operation("+"))
plus.grid(row = 1, column = 3)

equals = Button(root, padx = 50, pady = 100, text = "=", command = equal)
equals.grid(row = 2, column = 3, rowspan = 2)

#testButton = Button(root, width = 20, height = 20, text = "Click Me!", command = makeLine)
#testButton.grid(row = 1)

root.mainloop()