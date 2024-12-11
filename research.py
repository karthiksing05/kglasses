"""
This script is enabled and ran whenever the F1 key is pressed --> it takes
advantage of the already open bing menu to automate googling for my research
"""

import pyautogui
import time
import pytesseract
from PIL import ImageGrab
import webbrowser
import urllib.parse
import random

from transformers import pipeline

def extract_research_lines(lines):
    # ADDITIONAL CLASSIFIER INFORMATION HERE
    classifier = pipeline("text-classification", model="distilbert-base-uncased", return_all_scores=True)

    relevant_lines = []

    for line in lines:
        if line.strip():
            scores = classifier(line)
            relevant_score = next((item['score'] for item in scores[0] if item['label'] == 'LABEL_1'), 0)

            if relevant_score > 0.6:
                relevant_lines.append(line)

    return relevant_lines

screenshot = ImageGrab.grab(bbox=(0, 0, 800, 800))
extracted_text = pytesseract.image_to_string(screenshot, lang='eng')
lines = [line for line in extracted_text.split('\n') if line.strip()]
search_query = extract_research_lines(lines) if lines else "test"

print(lines)

query = search_query
pyautogui.moveTo(351, 147, duration=0.5)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite(query)
pyautogui.press('enter')

"""
Code below controlled my mouse and wouldn't let me navigate properly
"""

start_y = 300
end_y = 600
step = 15

previous_window = pyautogui.getActiveWindow()

for y in range(start_y, end_y, step):
    pyautogui.moveTo(351, y, duration=0.2)
    pyautogui.click()
    time.sleep(0.01)
    current_window = pyautogui.getActiveWindow()
    if current_window != previous_window:
        time.sleep(10) # this time fluctuated significantly due to the screen recording software
        previous_window.activate()