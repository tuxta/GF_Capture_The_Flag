from GameFrame import Level
from Objects import Red1
import os


class Arena(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)
        print(os.getcwd())

        self.set_background_image("background.png")


        arrow_object = Red1(self, 400, 300)
        self.add_room_object(arrow_object)
