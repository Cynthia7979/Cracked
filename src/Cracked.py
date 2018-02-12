import pygame
import logging
import sys
import abc
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def logged(class_):
    class_.logger = logging.getLogger(class_.__name__)
    return class_


@logged
class GameStatus:
    def __init__(self):
        self.logger.debug('Name of the logger: {0}'.format(self.__class__.__name__))
        self.scene = 'loading'
        self.__dict__.update({
            'floor': 1,
            'scene': 'loading',
        })
        self.logger.warn('Please check the realization of initialization for class GameStatus')

    def update(self, data):
        self.logger.warn('This may not be a very good realization for updating')
        assert isinstance(data, dict), 'The argument given to method update() is not a dictionary'
        for key in data.keys():
            if key not in self.__dict__.keys():
                del data[key]
        self.__dict__.update(data)


@logged
class Mob(metaclass=abc.ABCMeta):
    def __init__(self):
        self.blood = 0
        self.images = {'left': [], 'right': [], 'attack': [], 'die': []}
        self.pos = ()  # Abstract position

    @abc.abstractmethod
    def make_policy(self):
        """Decide what to do (attack, move, die) via current situation"""
        pass


@logged
class Skill(metaclass=abc.ABCMeta):
    def __init__(self):
        self.image = None
        self.buff = None
        self.harm = 0

    @abc.abstractmethod
    def activate(self):
        """Activate the skill"""
        pass


class Buff:
    def __init__(self, name, image, time,
                 blood_effect=0,
                 speed_effect=0,
                 harm_effect=0):
        self.name = name
        self.image = image
        self.time = time
        self.effect = {'blood': blood_effect, 'speed': speed_effect, 'harm': harm_effect}
if __name__ == '__main__':
    GameStatus().update({'scene': 'opening'})
