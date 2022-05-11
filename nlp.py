import pickle

from pprint import pprint

from wit import Wit

with open('data\\token.pickle', 'rb') as f:
    ACCESS_TOKEN = pickle.load(f)[0]

Client = Wit(ACCESS_TOKEN)

from automation import *
from factbot import answer_question
from weather import get_weather
from playmusic import play_song, pygame_pause, pygame_unpause, pygame_stop
from conversation import converse
from news import get_news
from demo import demo
from reminders import write_reminder

def identify_action(command):
    resp = Client.message(command)
    # print(resp)

    intent_name = str(resp['intents'][0]['name'])

    entities = resp['entities']
    userText = resp['text']

    # It should return the name of the action that should be completed and the keywords of the action
    return intent_name, entities, userText

def execute_action(intent_name, entities, userText):
    # Lots of if/else statements in this function to decide what to do.
    if intent_name is None:
        print("The error occured when you said: {}.".format(userText))
        print("Problem with Wit.AI engine, please try again.")
        exit()

    elif "exit" in userText:
        pytts("Powering down...")
        exit()

    elif intent_name == "conversation":
        pytts(converse(userText))

    elif intent_name == "play_song":
        try:
            pygame_stop()
        except:
            pass
        try:
            song_title = entities['song_title:song_title'][0]['body']
            play_song(song_title)
        except:
            pytts("No song specified, sorry.")

    elif intent_name == "pause_song":
        pygame_pause()

    elif intent_name == "unpause_song":
        pygame_unpause()

    elif intent_name == "stop_song":
        pygame_stop()

    elif intent_name == "take_note":
        take_note()

    elif intent_name == "trivia":
        query = userText
        answer_question(query)

    elif intent_name == "date_today":
        date_str = date_today()

    elif intent_name == "time_today":
        time_str = time_today()

    elif intent_name == "get_weather":
        try:
            location = entities['location:location'][0]['body']
        except:
            location = "present"
        get_weather(location)

    elif intent_name == "news":
        headlines = get_news()
        pprint([headline[0] for headline in headlines])
        pytts("Top headlines have been display in the log for you.")

        return headlines

    elif intent_name == "demo":
        demo()
    
    elif intent_name == 'reminder': # train Wit.ai clf on reminders
        reminder = entities['song_title:song_title'][0]['body']
        dt_to_remind = entities['song_title:song_title'][0]['body']
        write_reminder(reminder, dt_to_remind)