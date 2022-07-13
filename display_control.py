import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Change these to the right size for your display!
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

fonttypes = {
    "header":("/fonts/tahomabold.ttf", 24),
    "body":("/fonts/tahoma.ttf", 15),
    "special":("/fonts/magneto.ttf", 24) # used for like time and date and stuff ig, i like the font
    
}

def clear_display():
    oled.fill(0)
    oled.show()

def update_image():
    oled.image(image)
    oled.show()

def write_text(text:str, coords:tuple, fonttype:str):

    font = ImageFont.truetype(fonttypes[fonttype][0], fonttypes[fonttype][1])

    # Draw Some Text
    draw.text(coords, text, font=font, fill=255)

    update_image()

clear_display()

def test_font():
    write_text("xxxxxxxxxxxxxxxx", (0, 0), "body") # 16 characters
    write_text("abcdefghijklm", (0, fonttypes["body"][1]), "body")
    write_text("nopqrstuvwxyz", (0, fonttypes["body"][1] * 2), "body")
    write_text("1234567890", (0, fonttypes["body"][1] * 3), "body")
    write_text("/.,'\";:][}{\\~`|", (0, fonttypes["body"][1] * 4), "body")

test_font()
