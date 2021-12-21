import datetime
import os
import os.path
import random
import re
import json
import subprocess
import tkinter as tk
import requests
import pickle
import webbrowser
from time import sleep
import time
from tkinter import simpledialog

import pyautogui
import win32com.client as win32
import xlsxwriter
import yfinance as yf
from playsound import playsound
from win32com.client import Dispatch

from speech import myCommand, pytts

def input_dialog_box(title, prompt):
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    input_dialog = simpledialog.askstring(title=title, prompt=prompt)
    
    return input_dialog


def open_website(website):
    domain = website
    
    url = 'https://www.' + domain
    webbrowser.open(url)
    
    pytts('Opening ' + domain)

def take_note():
    text = myCommand("What would you like me to write down?")
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

    pytts("I've made a note of that.")

def open_powerpoint():

    PPTApp = win32.Dispatch("PowerPoint.Application")
    PPTApp.Visible = True

    PPTPresentation = PPTApp.Presentations.Add()

    PPTPresentation.Slides.Add(Index=1, Layout=12)
    
    pytts("I've created your presentation.")

def open_word():
    filename = myCommand("What would you like the file name to be?")
    new_file = filename + ".docx"
    try:
        open(new_file, "x")

    except FileExistsError:
        print("The file name already exists in your directory.")

    working_file = str(os.getcwd()) + r"\\" + new_file

    myWord = Dispatch('Word.Application')
    myWord.Visible = 1  # comment out for production

    myWord.Documents.Open(working_file)  # open file

    pytts("I've successfully opened your file.")

def open_excel():
    workbook_name = myCommand("What would you like the name of the workbook to be?")
    workbook = xlsxwriter.Workbook(workbook_name+".xlsx")
    
    num_sheets = myCommand("How many sheets would you like to make in the workbook?")
    
    for x in range(1, int(num_sheets)+1):
        worksheet_name = myCommand("What would you like worksheet "+str(x)+"'s name to be?")
        worksheet = workbook.add_worksheet(worksheet_name)
        
    workbook.close()
    pytts("I've created your workbook.")

def date_today():

    x = datetime.datetime.now()

    pytts("Today is " + str(x.strftime(r"%b / %d / %Y")))

def time_today():
    
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")
    pytts("The time is " + str(current_time))