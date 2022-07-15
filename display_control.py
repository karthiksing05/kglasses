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
    "header":("/home/pi/kglasses/fonts/tahomabold.ttf", 24),
    "body":("/home/pi/kglasses/fonts/minecraftia.ttf", 16),
    "special":("/home/pi/kglasses/fonts/magneto.ttf", 24)
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
