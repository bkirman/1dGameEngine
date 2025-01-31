from controller1d import Controller1d
from machine import ADC

class PotController(Controller1d):
    '''Example controller scheme using a typical 10k potentiometer. 
    This example returns an index to a specific LED based on the position of the potentiometer from 0-Max'''
    
    def __init__(self,PIN_POT,NUM_LEDS):
        ''' Expects int pin location of potentiometer output and number of LEDs'''
        self.pot = ADC(PIN_POT)
        self.leds = NUM_LEDS

    def get(self,inputs):
        ''' Check and return button dict with value of pot in 'pot' '''
        pot_total = 0
        for i in range(20):#sampling a bunch of times to reduce noise
            pot_total += self.pot.read_u16()
        pot_value = pot_total/20 
        inputs['pot'] = max(0,(self.leds - int(pot_value/65535*(self.leds)) -1))
        return inputs
    