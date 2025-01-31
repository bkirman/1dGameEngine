import time
import random

from displays.dotstar1d import DotStarDisplay
from controllers.pot import PotController
from games.flappy import Flappy

NUM_LEDS = 144
display = DotStarDisplay(PIN_DATA=3,PIN_CLOCK=2,NUM_LEDS=NUM_LEDS) #DotStar display, with green on pin 3 and yellow on pin 2.
controls = PotController(PIN_POT=26,NUM_LEDS=NUM_LEDS) #Potentiometer controller, attached to pin 26
FPS = 60
last_pos = 0

game = Flappy()
game.gameInit()
pixels = [(0,0,0) for i in range(NUM_LEDS)] #start blank
buttons = {}

while True:
    buttons = controls.get(buttons) #Update the input state from the controller
    #Note it is possible to have multiple controls and chain them here.
    new_pixels = game.draw(buttons,pixels)
    for i in range(len(new_pixels)): #only change updated pixels - you might instead do some smoothing or animated shenanigans here
        if new_pixels[i] != pixels[i]:
            display.setRgb(i,new_pixels[i])
    display.refresh() #write pixels to the LED strip
    pixels = new_pixels
    time.sleep(1.0 / FPS)