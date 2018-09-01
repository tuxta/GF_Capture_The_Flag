from GameFrame import Level
from Objects import Red1
from Objects import Blue1
import os


class Arena(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)
        print(os.getcwd())

        self.set_background_image("background.png")

        red_bots = []
        blue_bots = []

        red_bots.append(Red1(self, 550, 100))
        red_bots.append(Red1(self, 550, 200))
        red_bots.append(Red1(self, 550, 368))
        red_bots.append(Red1(self, 550, 468))
        red_bots.append(Red1(self, 700, 274))

        blue_bots.append(Blue1(self, 228, 100))
        blue_bots.append(Blue1(self, 228, 200))
        blue_bots.append(Blue1(self, 228, 368))
        blue_bots.append(Blue1(self, 228, 468))
        blue_bots.append(Blue1(self, 68, 274))

        for i in range(5):
            self.add_room_object(red_bots[i])

        for i in range(5):
            self.add_room_object(blue_bots[i])
