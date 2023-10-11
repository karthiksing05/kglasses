import webbrowser as web
import pyautogui as pg
from urllib.parse import quote
from bs4 import BeautifulSoup

import time
import datetime
import pickle
import os
import glob

class Messager(object):

    def __init__(self, load_contacts_by_def=True):
        self.contactsFN = "data\\contacts.pickle"
        self.width, self.height = pg.size()

        if load_contacts_by_def:
            self.load_contacts()

    def load_contacts(self):
        with open(self.contactsFN, "rb") as f:
            self.contacts = pickle.load(f)

    def get_contacts_online(self):
        if os.path.exists("data\\whatsapp.txt"):
            os.remove("data\\whatsapp.txt")

        web.open("https://web.whatsapp.com/")
        time.sleep(3)
        pg.hotkey("ctrl", "s")
        time.sleep(1)
        saveFilename = os.getcwd() + "\\data\\whatsapp.txt"
        pg.typewrite(saveFilename)
        pg.press("enter")
        time.sleep(5)
        pg.hotkey("ctrl", "w")

        for file in glob.glob("data\\whatsapp_files\\*.*"):
            os.remove(file)
        os.rmdir("data\\whatsapp_files")

        with open("data\\whatsapp.txt", "r", encoding='cp437') as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        
        

    def add_new_contact(self, name:str, number:str):
        if "+" not in number:
            number = "+1" + number
        self.contacts[name] = number
    
    def save_contacts(self):
        with open(self.contactsFN, "wb") as f:
            pickle.dump(self.contacts, f)

    def send_message(self, number:str, text:str):
        web.open(f"https://web.whatsapp.com/send?phone={number}&text={quote(text)}")
        time.sleep(10)
        pg.click(self.width / 2, self.height / 2)
        time.sleep(2)
        pg.press("enter")
        time.sleep(2)
        pg.hotkey("ctrl", "w")
        pg.press("enter")
        if number != self.contacts["Me"]:
            self.send_message(self.contacts["Me"], f"Message to {number} at {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} with content: {text}")

    def send_to_contact(self, contactName:str, text:str):
        self.send_message(self.contacts[contactName], text)

    def count_notifs(self):
        if os.path.exists("data\\whatsapp.txt"):
            os.remove("data\\whatsapp.txt")

        web.open("https://web.whatsapp.com/")
        time.sleep(3)
        pg.hotkey("ctrl", "s")
        time.sleep(1)
        saveFilename = os.getcwd() + "\\data\\whatsapp.txt"
        pg.typewrite(saveFilename)
        pg.press("enter")
        time.sleep(5)
        pg.hotkey("ctrl", "w")

        for file in glob.glob("data\\whatsapp_files\\*.*"):
            os.remove(file)
        os.rmdir("data\\whatsapp_files")

        with open("data\\whatsapp.txt", "r", encoding='cp437') as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        
        new_msgs = soup.find_all('div', {"class":"_1pJ9J"})
        totalUnread = 0
        for msg in new_msgs:
            totalUnread += int(msg.find('span').text)
        
        return totalUnread
    
    def preProcessText(self, cmd:str):
        # we need to create a command that converts all texts to be sent directly
        pass

if __name__ == "__main__":
    msgr = Messager()
    print(msgr.count_notifs())