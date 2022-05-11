import serial
import time

def display(text, coordx, coordy, clear_oled=False):
    """
    A basic function to transmit text and the coordinate placement of the text
    over the serial hub. 
    
    No idea if this will work on Pi, but should work on Windows for testing. 
    
    Remember each text written should be 10 px apart to prevent overlap, and 
    at most you should have three lines on screen, each line being no more 
    than ~16 characters (including spaces).
    """
    ser = serial.Serial()
    ser.baudrate = (115200)

    if clear_oled:
        text = "code: clear"

    bytetext = bytearray(str(text + "\n"), encoding="utf-8")
    bytenumbers = bytearray(str([coordx, coordy]), encoding="utf-8")

    ser.port = "COM5" # CHANGE THIS PORT
    ser.open()

    time.sleep(0.1)
    ser.write(bytetext)
    time.sleep(0.1)
    ser.write(bytenumbers)

    return True


def format_display(text:str="", line1:str="", line2:str="", line3:str=""):
    """
    A simple helper function to wrap any given amount of text onto the OLED.

    Choose between the "text" argument (if you only want to wrap the text you
    currently have to the screen) or the "lineX" arguments (if you have three 
    lines you want to display)
    """

    if len(text) > 0:
        numChars = len(text)
        if numChars > 48:
            print("you are being notified that some text at the end will be cropped off")

        line1 = text[:16]
        line2 = text[16:32]
        line3 = text[32:48]

    display(line1, 0, 10)
    display(line2, 0, 20)
    display(line3, 0, 30)
