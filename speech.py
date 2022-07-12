from gtts import gTTS
import speech_recognition as sr
from pocketsphinx import LiveSpeech
import pyttsx3
from playsound import playsound
import time
import os

from playmusic import fade_out_while_speaking, unfade_in_while_speaking

# function to play audio.
def mp3tts(audio):
    print(audio)
    tts = gTTS(text=audio, lang="en")
    run = True
    num_errors = 0
    while run:
        if num_errors >= 5:
            print("not working, try again.")
            exit()
        try:
            tts.save('audio.mp3')
            time.sleep(1)
            playsound('../audio.mp3')
        
        except Exception as e:
            print("Exception"+e)
            num_errors += 1
            print("Number of errors: " + str(num_errors))
            print("\n")
            time.sleep(1)

    if os.path.exists("../audio.mp3"):
        os.remove("../audio.mp3")

# Another Function for Talking
def pytts(text):
    engine = pyttsx3.init()

    volume = engine.getProperty('volume')
    engine.setProperty('volume', float(volume) - 0.15)

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)

    gender = engine.getProperty('voices')
    engine.setProperty('voice', gender[0].id)

    fade_out_while_speaking()
    engine.say(text)
    print(text)
    engine.runAndWait()
    unfade_in_while_speaking()

# function to recognize my speech
def myCommand(prompt):
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required = index
    r = sr.Recognizer()
    pytts(prompt)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=4)
    try:
        userinput = r.recognize_google(audio)
        print("You said: " + userinput)
        return str(userinput)
    except sr.UnknownValueError:
        pytts("Google Speech Recognition API could not understand audio")
    except sr.RequestError as e:
        pytts("Could not request results from Google Speech Recognition API service; {0}".format(e))

