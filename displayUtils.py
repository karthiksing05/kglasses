from asyncore import write
import gaugette.gpio
import gaugette.ssd1306
import gaugette
from gaugette.fonts import tahoma_16, arial_24, stencil_33, magneto_16
import datetime
import time

RESET_PIN = 15
DC_PIN    = 16

_gpio = gaugette.gpio.GPIO()
_spi = gaugette.spi.SPI(bus=0, device=0)
oled = gaugette.ssd1306.SSD1306(_gpio, _spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=64, cols=128)
oled.begin()

fonttypes = {
    "body":tahoma_16,
    "header":arial_24,
    "time": stencil_33,
    "date": magneto_16
}

def clear_display():
    oled.clear_display()

def write_text(text:str, coordx:int, coordy:int, fonttype:str):
    
    font = fonttypes[fonttype]
    
    oled.draw_text3(coordx, coordy, text, font)
    
    oled.display()

def display_home_screen(numMsgs:int):
    clear_display()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    write_text(time, 0, 0, "time")
    write_text("{} unread", 0, 34, "body")

if __name__ == "__main__":
    while True:
        display_home_screen()
        time.sleep(0.1)
