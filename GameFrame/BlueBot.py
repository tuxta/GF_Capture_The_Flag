from GameFrame import Bot, Globals


class BlueBot(Bot):
    def __init__(self, room, x, y):
        Bot.__init__(self, room, x, y)
        blue_bot_image = self.load_image('arrow_blue.png')
        self.set_image(blue_bot_image, 32, 32)

        self.rotate(-90)

        self.register_collision_object('Red1')
        self.register_collision_object('Red2')
        self.register_collision_object('Red3')
        self.register_collision_object('Red4')
        self.register_collision_object('Red5')

    def step(self):
        Bot.step(self)

    def handle_collision(self, other):
        print('In Blue Collision')
        other_type = type(other).__name__
        if other_type == 'BlueFlag':
            pass
        elif other_type == 'RedFlag':
            pass
        else:
            if self.rect.centerx > Globals.SCREEN_WIDTH / 2 - self.width / 2:
                self.curr_rotation = 0
                self.rotate(-90)
                self.x = 68
                self.y = 274

