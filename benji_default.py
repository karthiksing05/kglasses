from speech import myCommand, pytts
from nlp import identify_action, execute_action
import pickle
import webbrowser
import time
import platform
import os

def setup():

    operating_system = platform.system()

    if operating_system != "Windows":
        print("This version of Benji only runs on Windows. Please install this app on windows and run the app again.")
        exit()

    try:
        with open('data\\credentials.pickle', 'rb') as f:
            name, gender, passphrase = pickle.load(f)

    except FileNotFoundError:
        pytts("This is your first time using Benji, so you will need to create a credential file first.")
        name = myCommand("What is your name?")
        gender = myCommand("Are you male or female?")
        gender = "male" if "fe" not in gender else "female"
        pytts(
            "Now you will need to define a passphrase. When I say 'speak your passphrase', you will say your "
            "passphrase. This will be the phrase you need to speak to unlock me every time. Ready?")
        time.sleep(1)
        passphrase = myCommand("Speak your passphrase.")
        pytts("Great! You're ready to start using Benji now!")
        with open('data\\credentials.pickle', 'wb') as f:
            pickle.dump([name, gender, passphrase], f)

    return name, gender, passphrase


def runVoiceShortcut(shortcutName):
    filename = os.getcwd() + r"\\" + str(shortcutName) + ".txt"
    with open(filename, 'r') as f:
        old_apps = f.readline()
        old_apps = old_apps.split(",")
        old_apps = [x for x in old_apps if x.strip()]
        old_websites = f.readline()
        old_websites = old_websites.split(",")
        old_websites = [x for x in old_websites if x.strip()]

    for app in old_apps:
        os.startfile(app)

    for website in old_websites:
        webbrowser.open(website, new=0, autoraise=True)

    pytts("Running shortcut: {}.".format(shortcutName))


# AI functions
def main(name, gender, passphrase):
    login = None
    while not login:
        login = myCommand("Speak your passphrase, {}.".format(name))

    if login.lower() == passphrase.lower():
        pytts("Welcome back, {}".format(name))

    else:
        pytts("Incorrect passphrase, exiting bot.")
        exit()

    while True:
        try:
            with open('data\\shortcuts.pickle', 'rb') as f:
                shortcuts = pickle.load(f)

        except EOFError:
            shortcuts = {}

        command = myCommand("i am ready for your command")
        if 'benji' in command.lower():
            if command in shortcuts:
                shortcutName = shortcuts[command]
                runVoiceShortcut(shortcutName)
            else:
                try:
                    intent, entities, text = identify_action(command)

                    execute_action(intent, entities, text)

                except IndexError:
                    pytts("Sorry, I don't understand.")
                    continue

if __name__ == "__main__":
    name, gender, passphrase = setup()
    main(name, gender, passphrase)
