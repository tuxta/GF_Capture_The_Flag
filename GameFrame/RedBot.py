from GameFrame import Bot


class RedBot(Bot):
    def __init__(self, room, x, y):
        Bot.__init__(self, room, x, y)
        red_bot_image = self.load_image('arrow.png')
        self.set_image(red_bot_image, 32, 32)

        self.rotate(90)
