from display1d import Display1d
from plasma import plasma_stick

class PlasmaDisplay(Display1d):
    '''Display for 1dEngine for the Pimoroni Plasma WS2812B/Neopixel board. Needs plasma library, see:
    https://shop.pimoroni.com/products/plasma-stick-2040-w?variant=40359072301139
    '''

    def __init__(self,NUM_LEDS,FPS):
        self._NUM_LEDS = NUM_LEDS
        self._FPS = FPS
        self._leds = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_GRB)
        self._leds.start(FPS)
    
    def setRgb(self,i,rgb):
        self._leds.set_rgb(i,rgb)
        
    def refresh(self):
        #not implemented for neopixel
        pass
