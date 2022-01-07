from speech import pytts
from nlp import identify_action, execute_action
import pickle
import time

def setup():

    try:
        with open('data\\credentials.pickle', 'rb') as f:
            name, gender, passphrase = pickle.load(f)

    except FileNotFoundError:
        pytts("This is your first time using Benji, so you will need to create a credential file first.")
        name = input("What is your name?")
        gender = input("Are you male or female?")
        gender = "male" if "fe" not in gender else "female"
        pytts(
            "Now you will need to define a passphrase. When I say 'speak your passphrase', you will say your "
            "passphrase. This will be the phrase you need to speak to unlock me every time. Ready?")
        time.sleep(1)
        passphrase = input("Speak your passphrase.")
        pytts("Great! You're ready to start using Benji now!")
        with open('data\\credentials.pickle', 'wb') as f:
            pickle.dump([name, gender, passphrase], f)

    return name, gender, passphrase


# AI functions
def main(name, gender, passphrase):
    login = input("Speak your passphrase, {}.".format(name))

    if login == passphrase:
        pytts("Welcome back, {}!".format(name))

    else:
        pytts("Incorrect passphrase, exiting bot.")
        exit()

    while True:

        command = input("i am ready for your command")
        try:
            intent, entities, text = identify_action(command)

            execute_action(intent, entities, text)

        except IndexError:
            pytts("Sorry, I don't understand.")
            continue


