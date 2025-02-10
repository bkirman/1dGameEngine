from controller1d import Controller1d
from machine import I2C
from qwstpad import QwSTPad # type: ignore
from qwstpad import DEFAULT_ADDRESS as ADDRESS # type: ignore

class QwstPad1d(Controller1d):
    '''Pimoroni Qw/ST Pad I2C Controller interface. Note this requires the qwstpad-micropython library. See:
    https://shop.pimoroni.com/products/qwst-pad?variant=53514400596347
    '''
    
    def __init__(self,ID,SCL,SDA):
        ''' Expects id, scl, sda (i2c config)'''
        #Controller setup
        i2c = I2C(id=ID, scl=SCL, sda=SDA)
        try:
            self._pad = QwSTPad(i2c, ADDRESS)
        except OSError:
            print("QwSTPad: Not Connected ... Exiting")
            raise SystemExit

    def get(self,inputs):
        ''' Check and return button dict with value of controls. This handled by qwstpad_micropython '''
        inputs = self._pad.read_buttons()
        #TODO: Currently only supports one Qwstpad - need to figure out how chaining works.
        return inputs
    