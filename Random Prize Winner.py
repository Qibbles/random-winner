import tkinter as tk
from tkinter import ttk

#GUI
win = tk.Tk()
win.title("Random Winners")

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


win.mainloop()