from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("VKY")

def popup():
    messagebox.showinfo("In the TAB", "POPING_UP")

Button(root, text='Pop- up', command=popup).pack()

root.mainloop()

