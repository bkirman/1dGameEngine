import time
from displays.plasma1d import PlasmaDisplay
from controllers.qwstpad_1d import QwstPad1d
from games.snake1d import Snake


NUM_LEDS = 300
FPS = 60

display = PlasmaDisplay(NUM_LEDS,FPS)
controls = QwstPad1d(ID=0,SCL=5,SDA=4)

game = Snake()
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
    pixels = new_pixels
    time.sleep(1.0 / FPS)



