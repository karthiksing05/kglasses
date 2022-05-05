from speech import pytts, myCommand

import datetime
import os
import glob

def write_reminder(text, dt_to_remind):

    if not text:
        text = myCommand("What would you like me to remind you about?")
    if not dt_to_remind:
        dt_to_remind = myCommand("When would you like me to remind you?")

    file_name = "reminders\\" + dt_to_remind + "-reminder.txt"
    with open(file_name, "w") as f:
        f.write(text)

    pytts("I'll remind you to {} at {}".format(text, dt_to_remind))

def check_reminders():

    for file in glob.glob(R"reminders\*.txt"):
        remind_date = file.split("\\")[1].split(".txt")[0]
        if datetime.datetime.now() >= datetime.datetime.strptime(remind_date, "%Y-%m-%d %H-%M"):
            with open(file, 'r') as f:
                contents = f.read()
            pytts(contents)
            os.remove(file)
