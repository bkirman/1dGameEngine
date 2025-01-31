class Controller1d:
    '''
    Abstract class for implementing different kinds of game controller.
    The basic pattern is that the controller will be asked to return its current state each "frame".
    The state is returned as a map/dict of named elements and values, to be interpreted by the game.
    This same state, or an empty dict should be passed as the inputs parameters to get. This allows different controllers to be chained and used simultaneously
    '''

    def get(self,inputs):
        '''
        Return a map/dict of current controller values
        '''
        return inputs
    