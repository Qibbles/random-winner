import tkinter as tk
from tkinter import ttk
import random

#GUI
win = tk.Tk()
win.title("Random Winners")

#functions
def upload():
    pass

def submit():
    print(random.randint(5))
    pass

#labels
winnerLabel = ttk.Label(win, text="No. Winners")
winnerLabel.grid(column=0, row=0)

csvLabel = ttk.Label(win, text="Upload File")
csvLabel.grid(column=0, row=1)

headerLabel = ttk.Label(win, text="Has Header?")
headerLabel.grid(column=0, row=2)

#textboxes
winner = tk.StringVar()
winnerBox = ttk.Entry(win, width=12, textvariable=winner)

csv = tk.StringVar()
csvBox = ttk.Entry(win, width=12, textvariable=csv)

#checkbox

#buttons
uploadButton = ttk.Button(win, text="Upload", command=upload)
uploadButton.grid(column=1, row=1)

submitButton = ttk.Button(win, text="Submit", command=submit)
submitButton.grid(column=0, row=3)

win.mainloop()