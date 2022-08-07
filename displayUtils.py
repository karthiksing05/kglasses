import gaugette.gpio
import gaugette.ssd1306
import gaugette
from gaugette.fonts import stencil_33, magneto_24, arial_24
from PIL import Image, ImageFont, ImageDraw
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

images = {
    "whatsapp":"WHATSAPPFN",
    "music":"MUSICFN",
    "play":"PLAYFN",
    "settings":"SETTINGSFN",
    "sunny":"SUNNYFN",
    "rainy":"RAINYFN",
    "cloudy":"CLOUDYFN"
}

def clear_display():
    oled.clear_display()

def disp_util(coordx:int, coordy:int, image):
    width = image.width
    height = image.height

    for x in range(coordx, width + coordx):
        for y in range(coordy, height + coordy):
            oled.draw_pixel(x, y, bool(int(image.getpixel((x, y)))))


def write_text(coordx:int, coordy:int, text:str, fonttype:str):
    
    font = fonttypes[fonttype]
    
    oled.draw_text3(coordx, coordy, text, font)
    
    oled.display()

def custom_write_text(coordx:int, coordy:int, text:str, filename:str, fontsize:int):

    font = ImageFont.truetype(filename, fontsize)
    image = Image.new("1", (len(text) * 5, fontsize)) # TODO edit these constants as necessary

    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font)

    disp_util(coordx, coordy, image)

    oled.display()


def write_image(coordx:int, coordy:int, imageName:str="", filename:str=""):

    if len(imageName) > 0:
        image = Image.open(images[image])
    elif len(filename) > 0:
        image = Image.open(filename)
    else:
        raise Exception("Please specify either the filename or a preselected file image name")
    imageBW = image.convert("1")
    
    disp_util(coordx, coordy, imageBW)

    oled.display()

# default screen displays

def display_dt_screen():
    clear_display()
    now = datetime.datetime.now()
    time = now.strftime("%-I:%M:%S")
    date = now.strftime(r"%-m/%-d/%y")
    write_text(0, 0, time, "time")
    write_text(0, 33, date, "date")

def display_messages_screen(numUnread:int):
    clear_display()
    write_image(0, 0, imageName="whatsapp")
    write_text(0, 32, f"{numUnread} unread msgs")

def display_weather_screen(temp, desc):
    clear_display()
    if ("sun" in desc):
        write_image(0, 0, "sunny")
    elif ("rain" in desc):
        write_image(0, 0, "rainy")
    elif ("cloud" in desc):
        write_image(0, 0, "cloudy")
    write_text(34, 0, temp + "°F")

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

