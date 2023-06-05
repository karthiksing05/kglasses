import pickle

import wikipedia
import wolframalpha

from speech import pytts

# App-ID for Wolfram Alpha
with open('data\\token.pickle', 'rb') as f:
    APP_ID = pickle.load(f)[1]

# initalizing the client
client = wolframalpha.Client(app_id=APP_ID)

def answer_question(command):
    values = [command, None]
    try:
        wiki_res = wikipedia.summary(values[0], sentences=3)
        wolfram_res = next((client.query(values[0])).results).text
        pytts("Answer: "+wolfram_res)
        print("Answer: " + wolfram_res, "\nMore Details: " + wiki_res)

    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next((client.query(values[0])).results).text
        pytts("Answer: "+wolfram_res)
        # print(wolfram_res)

    except wikipedia.exceptions.PageError:
        wolfram_res = next((client.query(values[0])).results).text
        pytts("Answer: "+wolfram_res)
        # print(wolfram_res)

    except:
        wiki_res = wikipedia.summary(values[0], sentences=3)
        pytts("Answer: "+wiki_res)
        # print(wiki_res)


if __name__ == '__main__':
    run = True
    while run:
        command = input("ready")
        if "exit" in command:
            exit()
        else:
            answer_question(command)