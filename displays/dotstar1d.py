from display1d import Display1d
from lib import micropython_dotstar as dotstar
from machine import Pin, SPI

class DotStarDisplay(Display1d):
    '''Display for 1dEngine using the DotStar protocol.
    Note you might need to edit this for things like colour order, brightness tweaking, etc.
    It depends on the manufacturer and sometimes things are inconsistent.
    '''
    def __init__(self,PIN_DATA,PIN_CLOCK,NUM_LEDS):
        spi = SPI(0,sck=Pin(PIN_CLOCK), mosi=Pin(PIN_DATA), miso=Pin(4)) # Configure SPI - note: miso is unused
        self.dots = dotstar.DotStar(spi, NUM_LEDS, brightness=0.2,auto_write=False)
        self.NUM_LEDS = NUM_LEDS
    
    def setRgb(self,i,rgb):
        self.dots[i] = rgb
        
    def refresh(self):
        self.dots.show()
