import pygame
import logging
import sys
import abc
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def logged(class_):
    class_.logger = logging.getLogger(class_.__name__)
    class_.logger.debug('From decorator "logged": name of logger: {name}'.format(name=class_.__name__))
    return class_


@logged
class GameStatus:
    def __init__(self):
        raw_data = open_file(） # FIXME: Ended here
        self.__dict__.update({
            'scene': 'loading',
            
        })
        self.logger.warn('Please check the realization of initialization for class GameStatus')

    def update(self, data):
        self.logger.warn('This may not be a very good realization for updating')
        if not isinstance(data, dict):
            self.logger.error('The argument given to method update() is not a dictionary. \
                            This could cause a sudden stop of program.')
        for key in data.keys():
            if key not in self.__dict__.keys():
                del data[key]
        self.__dict__.update(data)


@logged
class Mob:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.blood = 0
        self.images = {'walking': {'left': [], 'right': []}, 'attacking': {'left': [], 'right': []}, 'die': {'left': [], 'right': []}
        self.pos = ()  # Abstract position
        self.exp = 0
        self.frame = 0
        self.facing = 'left'

    @abc.abstractmethod
    def make_policy(self, player_status):
        """Decide what to do (attack, move, die) via current situation"""
        pass


@logged
class NormalMob(Mob):
    def __init__(self, speed, blood, images, exp, speed, harm, attack_range='middle'):
        super(NormalMob, self).__init__()

        if isinstance(images, dict) and len(images) == 4:
            self.images = images
        else:
            if not isinstance(images, dict):
                self.logger.error('Received a non-dict-item when initializing NormalMob instance. \
                                This could cause display problems')
            elif len(images) != 4:
                self.logger.error('Received instance which has a not-4 length.\
                                This could cause display problems')

        self.speed = speed
        self.blood = blood
        self.exp = exp
        self.speed = speed
        self.attack_range = attack_range
        self.harm = harm
        self.state = 'walking'
        self.pos = (0, 5)  # Abstract position
        if attack_range == 'short':
            self.attack_range = 3
        elif attack_range == 'middle':
            self.attack_range = 7
        elif attack_range == 'long':
            self.attack_range = 11

    def make_policy(self, player_status):
        # FIXME: finish me
        if self.state == 'die':
            self.frame += 1
        else:
            if self.blood <= 0:
                self.state = 'die'
            elif player_status.pos[0] - self.pos[0] > self.attack_range:
                if self.facing != 'right':
                    x = self.pos[0] - self.speed
                    y = self.pos[1]
                    self.state = 'walking'
                    self.facing = 'right'
                    self.frame = 0
                else:
                    self.frame += 1
            elif -(player_status.pos[0] - self.pos[0]) > self.attack_range:
                if self.facing != 'left':
                    x = self.pos[0] + self.speed
                    y = self.pos[1]
                    self.state = 'walking'
                    self.facing = 'left'
                    self.frame = 0
                else:
                    self.frame += 1
            else: # attack
                if self.state == 'attacking': # just attacking
                    self.frame += 1
                else:
                    self.state = 'attacking'
        images = self.images[self.state][self.facing]
        if self.state == 'attacking': harm = self.harm / len(images)
        else: harm = 0
        if self.frame > len(images):
            if self.state == 'die':
                return (None, None)
            else:
                return (images[self.frame], 0)


@logged
class HorizVertiMoveMob(NormalMob):
    def __init__(self, speed, blood, images, exp):
        super(HorizVertiMoveMob, self).__init__(speed, blood, images, exp)
        
    def make_policy(self, player_status):
        # TODO: Still haven't thought about it
        pass
 
@logged
class SkillMob(NormalMob):
    def __init__(self, speed, blood, images, exp, skill):
        super(SkillMob, self).__init__(speed, blood, images, exp)
        self.skill = list(skill)
    
    def make_policy(self, player_status):
        # TODO
        pass



@logged
class Skill:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.image_surf = None
        self.image_rect = None
        self.buff = None
        self.harm = 0  # Maybe later I'll add 'count & minus', like -1 blood/s
        # Maybe later I'll add cold down time

    @abc.abstractmethod
    def activate(self, player_status):
        """Activate the skill"""
        pass


@logged
class PlayerSkill(Skill):
    def __init__(self, image, buff, harm=0):
        """Object given to 'image' attribute should be a tuple
        with a Surface instance at first place and a Rect instance second.
        Or a string, which is a path leading to an existing image.

        Creating instance of PlayerSkill should be something like this:
            PlayerSkill((Surface, Rect), Buff, int)
        or
            PlayerSkill(str, Buff, int)
        """

        super(PlayerSkill, self).__init__()
        if isinstance(image, str):
            try:
                img_surf, img_rect = open_file('image', image)
            except pygame.error:
                img_surf, img_rect = pygame.Surface(), pygame.Rect()
                self.logger.error('String given to PlayerSkill while creating an instance\
                                   was not a complete path or had lead to a not existing file: {string}. \
                                  This could cause display errors.'.format(string=image))
        elif isinstance(image, tuple):
            if isinstance(image[0], pygame.Surface):
                img_surf = image[0]
            else:
                img_surf = pygame.Surface()
                self.logger.error("The first object of the tuple given to 'image' attribute is not a \
                                  pygame.Surface instance. This could cause display errors.")
            if isinstance(image[1], pygame.Rect):
                img_rect = image[1]
            else:
                img_rect = pygame.Rect
                self.logger.error("The second object of the tuple given to 'image' attribute is not a \
                                pygame.Rect instance. This could cause clicking errors.")
        self.image_surf = img_surf
        self.image_rect = img_rect
        self.buff = buff
        self.harm = harm

    def activate(self, player_status):
        player_status.add_buff(self.buff)
        player_status.minus_blood(self.harm)


@logged
class MobSkill(Skill):
    def __init__(self):
        # TODO: Still leaving a blank, because I don't know how to add the skill for a specific mob.
        pass


@logged
class Buff:
    def __init__(self, name, image, time,
                 blood_effect=0,
                 speed_effect=0,
                 harm_effect=0):
        self.name = name
        self.image = image
        self.time = time
        self.effect = {'blood': blood_effect, 'speed': speed_effect, 'harm': harm_effect}

@logged
class PlayerStatus:
    def __init__(self):
        pass  # later adding attributes

"""=========Under this line it's functions========="""


def open_file(mode, path):
    if mode == 'image':
        image_surface = pygame.image.load(path)
        image_rect = image_surface.get_rect()
        return image_surface, image_rect
    elif mode == 'text':
        f = open(path)
        text = f.read()
        return text


if __name__ == '__main__':
    GameStatus().update({})
