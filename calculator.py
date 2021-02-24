#
#  Number finder
#  Few codes to tell you what type of number you plugin.
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

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