import serial
import time

def display(text, coordx, coordy, clear_oled=False):
    """
    A basic function to transmit text and the coordinate placement of the text
    over the serial hub. 
    
    No idea if this will work on Pi, but should work on Windows for testing. 
    
    Remember each text written should be 10 px apart to prevent overlap, and 
    at most you should have 6 lines on screen, each line being no more 
    than ~16 characters (including spaces).
    """
    ser = serial.Serial()
    ser.baudrate = (115200)

    if clear_oled:
        text = "code: clear"

    bytetext = bytearray(str(text + "\n"), encoding="utf-8")
    bytenumbers = bytearray(str([coordx, coordy]), encoding="utf-8")

    ser.port = "COM7"
    ser.open()

    time.sleep(0.1)
    ser.write(bytetext)
    time.sleep(0.1)
    ser.write(bytenumbers)
    time.sleep(0.1)

    

    ser.close()

    return True


def format_display(text:str="", lines:list=[]):
    """
    A simple helper function to wrap any given amount of text onto the OLED.

    Choose between the "text" argument (if you only want to wrap the text you
    currently have to the screen) or the "lines" argument (just pass a list of 
    lines and it will automatically list the lines in order)
    """

    charsPerLine = 16
    numLines = 6
    spaceBtwLines = 10

    if len(text) > 0:
        numChars = len(text)
        if numChars > (charsPerLine * numLines):
            print("you are being notified that some text at the end will be cropped off")

        lines = [text[i * charsPerLine:(i + 1) * charsPerLine] for i in range(numLines)]

    for i, line in enumerate(lines):
        display(line, 0, i * spaceBtwLines)
        time.sleep(0.1)

if __name__ == '__main__':
    print("displaying a thingy")
    while True:
        print(display("hello world", 0, 0))
        time.sleep(1)
        print("waiting...")
