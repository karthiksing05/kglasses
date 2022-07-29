from turtle import clear
import gaugette.gpio
import gaugette.ssd1306
import gaugette
from gaugette.fonts import stencil_33, magneto_24, arial_24
from PIL import Image
import datetime
import time

RESET_PIN = 15
DC_PIN    = 16

_gpio = gaugette.gpio.GPIO()
_spi = gaugette.spi.SPI(bus=0, device=0)
oled = gaugette.ssd1306.SSD1306(_gpio, _spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=64, cols=128)
oled.begin()

fonttypes = {
    "time": stencil_33,
    "date": magneto_24,
    "normal":arial_24
}

def clear_display():
    oled.clear_display()

def write_text(text:str, coordx:int, coordy:int, fonttype:str):
    
    font = fonttypes[fonttype]
    
    oled.draw_text3(coordx, coordy, text, font)
    
    oled.display()

def write_image(filename:str, coordx:int, coordy:int):

    image = Image.open(filename)
    imageBW = image.convert("1")
    width = image.width
    height = image.height

    for x in range(coordx, width + coordx):
        for y in range(coordy, height + coordy):
            oled.draw_pixel(x, y, bool(int(imageBW.getpixel((x, y)))))

    oled.display()

# default screen displays

def display_dt_screen():
    clear_display()
    now = datetime.datetime.now()
    time = now.strftime("%-I:%M:%S")
    date = now.strftime(r"%-m/%-d/%y")
    write_text(time, 0, 0, "time")
    write_text(date, 0, 33, "date")

def display_messages_screen(numUnread:int):
    clear_display()
    write_image("WHATSAPP-IMAGE-FN", 0, 0)
    write_text("")

def display_weather_screen(temp, desc):
    clear_display()

def display_voice_assistant_screen():
    clear_display()

def display_music_screen():
    clear_display()

def display_settings_screen():
    clear_display()


if __name__ == "__main__":
    while True:
        display_dt_screen()
        time.sleep(0.1)

