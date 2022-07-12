import glob
import os
import subprocess
import webbrowser
import time
from os import startfile
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import requests
import random

import speech

def is_playing():
    if pygame.mixer.music.get_busy():
        return True
    else:
        return False

def fade_out_while_speaking():
    try:
        if is_playing():
            pygame.mixer.music.set_volume(0.2)
    except Exception as e:
        if str(e) == "mixer not initialized":
            pass
            # print("It's ok, nothing's wrong.")
        else:
            print("Different Exception: {}".format(e))

def unfade_in_while_speaking():
    try:
        pygame.mixer.music.set_volume(0.7)
    except Exception as e:
        if str(e) == "mixer not initialized":
            # print("It's ok, nothing's wrong.")
            pass
        else:
            print("Different Exception: {}".format(e))


def pygame_play(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def pygame_pause():
    try:
        pygame.mixer.music.pause()
    
    except Exception as e:
        if str(e) == "mixer not initialized":
            print("You have no songs playing currently.")
        
        else:
            print("Different Exception: {}".format(e))

def pygame_unpause():
    try:
        pygame.mixer.music.unpause()
    
    except Exception as e:
        if str(e) == "mixer not initialized":
            print("You have no songs playing currently.")
        
        else:
            print("Different Exception: {}".format(e))

def pygame_stop():
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    
    except Exception as e:
        if str(e) == "mixer not initialized":
            print("You have no songs playing currently.")
        
        else:
            print("Different Exception: {}".format(e))


def play_song(name_of_song):
    
    
    for file in glob.glob(R"youtube-dl\*.mp3"):
        os.remove(file)

    if "soothing" in name_of_song:
        list_of_soothing = ["https://www.youtube.com/watch?v=lFcSrYw-ARY", 
                            "https://www.youtube.com/watch?v=2OEL4P1Rz04", 
                            "https://www.youtube.com/watch?v=1ZYbU82GVz4", 
                            "https://www.youtube.com/watch?v=EbnH3VHzhu8"]
        song_url = random.choice(list_of_soothing)

    else:
        url = 'https://www.youtube.com/results?q=' + name_of_song
        count = 0
        cont = requests.get(url)
        data = str(cont.content)
        lst = data.split('"')
        for i in lst:
            count+=1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count-5] == "/results":
            raise Exception("No video found.")
        
        #print("Videos found, opening most recent video")
        song_url = "https://www.youtube.com"+lst[count-5]
    
    youtube_dl_dir = os.getcwd() + "\youtube-dl"

    os.system(R"cd "+youtube_dl_dir+" && youtube-dl.exe -x --audio-format mp3 "+song_url)

    song_mp3_file = []

    for file in glob.glob(R"youtube-dl\*.mp3"):
        song_mp3_file.append(file)

    song_path = song_mp3_file[0]

    speech.pytts("Playing {}".format(name_of_song))

    pygame_play(song_path)

if __name__ == '__main__':
    play_song("Blinding lights by the weeknd")
