import gaugette.gpio
import gaugette.ssd1306
from gaugette.fonts import arial_16

RESET_PIN = 15
DC_PIN    = 16

_gpio = gaugette.gpio.GPIO()
_spi = gaugette.spi.SPI(bus=0, device=0)
oled = gaugette.ssd1306.SSD1306(_gpio, _spi, reset_pin=RESET_PIN, dc_pin=DC_PIN)
oled.begin()

fonttypes = {}

def write_text(text:str, coordx:int, coordy:int, fonttype:str):
    pass

