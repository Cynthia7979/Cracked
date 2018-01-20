import pygame
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def logged(class_):
    class_.logger = logging.getLogger(class_.__name__)
    return class_

@logged
class GameStatus:
    def __init__(self):
        self.logger.debug('Name of the logger: {0}'.format(self.__class__.__name__))
        self.scene = 'loading'

    def update(self,data):
        self.logger.warn('This may not be a very good realization for updating')
        assert isinstance(data,dict), 'The argument given to method update() is not a dictionary'
        for key in data.keys():
            if key not in self.__dict__.keys():
                del data[key]
        self.__dict__.update(data)

@logged
class Mob:
    def __init__(self):
        self.blood = 0
        self.images = {'left':(),'right':(),'attack':(),'die':()}
        self.pos = ()
if __name__ == '__main__':
    GameStatus().update({'scene':'opening'})