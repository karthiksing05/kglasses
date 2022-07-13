import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

disp = Adafruit_SSD1306.SSD1306_128_64(rst=0)
disp.begin()

FONT_PATH = '/usr/share/fonts/truetype/piboto/PibotoCondensed-Regular.ttf'
FONT = ImageFont.truetype(FONT_PATH, 22)

image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)

def clear_display():
    disp.clear()

def display_text(text:str, coordx:int, coordy:int, fontSize:int):
    pass

def display_img(filepath:str, coordx:int, coordy:int):
    pass

