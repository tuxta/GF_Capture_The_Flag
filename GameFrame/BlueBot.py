from GameFrame import Bot, Globals
import random


class BlueBot(Bot):
    def __init__(self, room, x, y):
        Bot.__init__(self, room, x, y)
        blue_bot_image = self.load_image('bot_blue.png')
        self.set_image(blue_bot_image, 16, 16)

        self.rotate(-90)

        self.register_collision_object('Red1')
        self.register_collision_object('BlueFlag')

    def frame(self):
        if self.has_flag:
            if self.x > Globals.SCREEN_WIDTH/2 - 40:
                Globals.blue_flag.x = self.x + self.rect.width + 2
                Globals.blue_flag.y = self.y

                if Globals.blue_flag.x <= 0:
                    Globals.blue_flag.x = 0
                    self.x = self.prev_x
                    self.y = self.prev_y
                elif Globals.blue_flag.x >= Globals.SCREEN_WIDTH - 34:
                    Globals.blue_flag.x = Globals.SCREEN_WIDTH - 34
                    self.x = self.prev_x
                    self.y = self.prev_y

                if Globals.blue_flag.y <= 0:
                    Globals.blue_flag.y = 2
                    self.x = self.prev_x
                    self.y = self.prev_y
                elif Globals.blue_flag.rect.bottom >= Globals.SCREEN_HEIGHT:
                    Globals.blue_flag.y = Globals.SCREEN_HEIGHT - Globals.blue_flag.rect.height
                    self.x = self.prev_x
                    self.y = self.prev_y
            else:
                self.has_flag = False

        self.tick()

    def tick(self):
        pass

    def handle_collision(self, other):
        other_type = type(other).__name__

        if other_type == 'BlueFlag':
            self.has_flag = True
            for bot in Globals.blue_bots:
                if bot.has_flag and bot is not self:
                    bot.has_flag = False
        else:
            if self.rect.right > Globals.SCREEN_WIDTH / 2:
                self.has_flag = False
                self.curr_rotation = 0
                self.rotate(-90)
                self.x = self.starting_x
                self.y = random.randint(50, 550)
