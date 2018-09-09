from GameFrame import Bot, Globals
import random


class RedBot(Bot):
    def __init__(self, room, x, y):
        Bot.__init__(self, room, x, y)
        red_bot_image = self.load_image('bot_red.png')
        self.set_image(red_bot_image, 16, 16)

        self.rotate(90)

        self.register_collision_object('Blue1')
        self.register_collision_object('RedFlag')

    def frame(self):
        if self.has_flag:
            Globals.red_flag.x = self.x
            Globals.red_flag.y = self.y
        self.tick()

    def tick(self):
        pass

    def handle_collision(self, other):
        other_type = type(other).__name__
        if other_type == 'BlueFlag':
            pass
        elif other_type == 'RedFlag':
            self.has_flag = True
        else:
            if self.rect.centerx < Globals.SCREEN_WIDTH / 2 - self.width / 2:
                self.has_flag = False
                self.curr_rotation = 0
                self.rotate(90)
                self.x = self.starting_x
                self.y = random.randint(50, 550)

