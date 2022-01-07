import datetime
import subprocess
import tkinter as tk
from tkinter import simpledialog

from speech import myCommand, pytts

def input_dialog_box(title, prompt):
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    input_dialog = simpledialog.askstring(title=title, prompt=prompt)
    
    return input_dialog

def take_note():
    text = myCommand("What would you like me to write down?")
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

    pytts("I've made a note of that.")

def date_today():

    x = datetime.datetime.now()

    pytts("Today is " + str(x.strftime(r"%b / %d / %Y")))

def time_today():
    
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")
    pytts("The time is " + str(current_time))