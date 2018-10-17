from tkinter import *
import math

def evaluate(event):
    res.configure(text = "Answer: " + str(eval(entry.get())))

window = Tk()
Label(window, text="Your Expression:").pack()

entry = Entry(window)
entry.bind("<Return>", evaluate)
entry.pack()

res = Label(window)
res.pack()

window.mainloop()