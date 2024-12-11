import datetime
import subprocess

from speech import myCommand, pytts

def take_note():
    text = myCommand("What would you like me to write down?")
    date = datetime.datetime.now()
    file_name = "notes\\" + str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w+") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

    pytts("I've made a note of that.")
