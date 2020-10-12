from tkinter import *


root = Tk()
root.title("VK_CALCULATOR")

E = Entry(root, width=55, borderwidth=4)
E.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = E.get()
    E.delete(0, END)
    E.insert(0, str(current) + str(number))


def button_add():
    first_number = E.get()
    global f_number
    f_number = int(first_number)
    E.delete(0, END)
    global indentifier
    indentifier = 1


def button_minus():
    first_number = E.get()
    global f_number
    f_number = int(first_number)
    E.delete(0, END)
    global indentifier
    indentifier = 2


def button_multiply():
    first_number = E.get()
    global f_number
    f_number = int(first_number)
    E.delete(0, END)
    global indentifier
    indentifier = 3


def button_divide():
    first_number = E.get()
    global f_number
    f_number = int(first_number)
    E.delete(0, END)
    global indentifier
    indentifier = 4


def button_ans():
    second_number = E.get()
    E.delete(0, END)
    global s_number
    s_number = int(second_number)
    if indentifier == 1:
        result = f_number + s_number
        E.insert(0, result)
    elif indentifier == 2:
        result = f_number - s_number
        E.insert(0, result)
    elif indentifier == 3:
        result = f_number * s_number
        E.insert(0, result)
    elif indentifier == 4:
        result = f_number / s_number
        E.insert(0, result)


def button_clear():
    E.delete(0, END)


# CREATING BUTTONS:
Button_1 = Button(root, text='1', borderwidth=3, padx=49, pady=30, command=lambda: button_click(1))
Button_2 = Button(root, text='2', borderwidth=3, padx=49, pady=30, command=lambda: button_click(2))
Button_3 = Button(root, text='3', borderwidth=3, padx=49, pady=30, command=lambda: button_click(3))

Button_4 = Button(root, text='4', borderwidth=3, padx=49, pady=30, command=lambda: button_click(4))
Button_5 = Button(root, text='5', borderwidth=3, padx=49, pady=30, command=lambda: button_click(5))
Button_6 = Button(root, text='6', borderwidth=3, padx=49, pady=30, command=lambda: button_click(6))

Button_7 = Button(root, text='7', borderwidth=3, padx=49, pady=30, command=lambda: button_click(7))
Button_8 = Button(root, text='8', borderwidth=3, padx=49, pady=30, command=lambda: button_click(8))
Button_9 = Button(root, text='9', borderwidth=3, padx=49, pady=30, command=lambda: button_click(9))

Button_0 = Button(root, text='0', borderwidth=3, padx=49, pady=30, command=lambda: button_click(0))

Button_add = Button(root, text='+', borderwidth=3, padx=49, pady=30, command=button_add)
Button_minus = Button(root, text='-', borderwidth=3, padx=49, pady=30, command=button_minus)
Button_multiply = Button(root, text='*', borderwidth=3, padx=49, pady=30, command=button_multiply)
Button_divide = Button(root, text='/', borderwidth=3, padx=49, pady=30, command=button_divide)
Button_ans = Button(root, text='ANS', borderwidth=3, padx=40, pady=30, command=button_ans)
Button_clear = Button(root, text='CLEAR', borderwidth=3, padx=154, pady=30, command=button_clear)


# DISPLAYING BUTTONS

# Row-1 Buttons
Button_7.grid(row=1, column=0, columnspan=1)
Button_8.grid(row=1, column=1, columnspan=1)
Button_9.grid(row=1, column=2, columnspan=1)

# Row-2 Buttons
Button_4.grid(row=2, column=0, columnspan=1)
Button_5.grid(row=2, column=1, columnspan=1)
Button_6.grid(row=2, column=2, columnspan=1)

# Row-3 Buttons
Button_1.grid(row=3, column=0, columnspan=1)
Button_2.grid(row=3, column=1, columnspan=1)
Button_3.grid(row=3, column=2, columnspan=1)

# Row-4 Buttons
Button_0.grid(row=4, column=0, columnspan=1)
Button_add.grid(row=4, column=1, columnspan=1)
Button_ans.grid(row=4, column=2, columnspan=1)

# Row-5 Buttons
Button_minus.grid(row=5, column=0, columnspan=1)
Button_multiply.grid(row=5, column=1, columnspan=1)
Button_divide.grid(row=5, column=2, columnspan=1)


# Row-6 Buttons
Button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()
