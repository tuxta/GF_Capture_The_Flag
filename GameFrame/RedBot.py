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
            Globals.red_flag.x = self.x - Globals.red_flag.rect.width - 2
            Globals.red_flag.y = self.y

            if Globals.red_flag.x <= 0:
                Globals.red_flag.x = 0
                self.x = self.prev_x
                self.y = self.prev_y
            elif Globals.red_flag.rect.right >= Globals.SCREEN_WIDTH:
                Globals.red_flag.x = Globals.SCREEN_WIDTH - Globals.red_flag.rect.width
                self.x = self.prev_x
                self.y = self.prev_y

            if Globals.red_flag.y <= 0:
                Globals.red_flag.y = 0
                self.x = self.prev_x
                self.y = self.prev_y
            elif Globals.red_flag.rect.bottom >= Globals.SCREEN_HEIGHT:
                Globals.red_flag.y = Globals.SCREEN_HEIGHT - Globals.red_flag.rect.height
                self.x = self.prev_x
                self.y = self.prev_y
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
            if self.rect.left < Globals.SCREEN_WIDTH / 2:
                self.has_flag = False
                self.curr_rotation = 0
                self.rotate(90)
                self.x = self.starting_x
                self.y = random.randint(50, 550)

