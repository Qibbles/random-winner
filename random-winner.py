import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import random
import pandas as pd

#GUI
win = tk.Tk()
win.title("Random Winners")

#functions
def browse():
    global filename
    filename = filedialog.askopenfile(initialdir="root", title="Select file")
    csv.set(filename.name)

def submit():
    numWinners = winner.get()
    winnerList = []
    #Open output file and clear(truncate) all data
    f = open("Results.csv", "w+")
    if chVarHeader.get() == 1:     
        try:
            dataframe = pd.read_csv(filename.name, header=1)
            #count number of rows
            numRows = dataframe.shape[0]
        except:   
            dataframe = pd.read_excel(filename.name, header=1)
            #count number of rows
            numRows = dataframe.shape[0]
    else:
        try:        
            dataframe = pd.read_csv(filename.name, header=0)
            #count number of rows
            numRows = dataframe.shape[0]
        except:
            dataframe = pd.read_excel(filename.name, header=1)
            #count number of rows
            numRows = dataframe.shape[0]

    #Loop through number of winners required, for each choose a random number from 0 to total number of rows
    #If random number is not in winner list, append it in and increase loop count by 1
    i = 1
    while i <= numWinners:
        try:
            randomWinner = random.randint(0,numRows)
            if randomWinner not in winnerList:
                winnerList.append(randomWinner)
                #Open output file and append data
                with open("Results.csv", "a") as f:
                    dataframe.iloc[[randomWinner]].to_csv(f, header=False)
                i += 1
        except:
            messagebox.showinfo("Failed!", "You have chosen " + str(numWinners) + " winners which exceeds number of rows.")
    
    messagebox.showinfo("Success!", str(numWinners) + " winners successfully selected!")

#labels
winnerLabel = ttk.Label(win, text="No. Winners")
winnerLabel.grid(column=0, row=0)

csvLabel = ttk.Label(win, text="Upload File")
csvLabel.grid(column=0, row=1)

#textboxes
winner = tk.IntVar()
winnerBox = ttk.Entry(win, width=12, textvariable=winner)
winnerBox.grid(column=1, row=0)

csv = tk.StringVar()
csvBox = ttk.Entry(win, width=50, textvariable=csv)
csvBox.grid(column=0, row=1)

#checkbox
chVarHeader = tk.IntVar()
headerCh = tk.Checkbutton(win, text="Has Header?", variable=chVarHeader)
headerCh.select()
headerCh.grid(column=0, row=2, sticky=tk.W)

#buttons
uploadButton = ttk.Button(win, text="Browse", command=browse)
uploadButton.grid(column=1, row=1)

submitButton = ttk.Button(win, text="Submit", command=submit)
submitButton.grid(column=0, row=3)

win.mainloop()