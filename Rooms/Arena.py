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

        red_bot_1 = Red1(self, 550, 100)
        self.add_room_object(red_bot_1)
        red_bots.append(red_bot_1)

        blue_bot_1 = Blue1(self, 250-32, 100)
        self.add_room_object(blue_bot_1)
        blue_bots.append(blue_bot_1)

        red_bot_2 = Red1(self, 550, 200)
        self.add_room_object(red_bot_2)
        red_bots.append(red_bot_2)

        blue_bot_2 = Blue1(self, 250-32, 200)
        self.add_room_object(blue_bot_2)
        blue_bots.append(blue_bot_2)

        red_bot_3 = Red1(self, 550, 400-32)
        self.add_room_object(red_bot_3)
        red_bots.append(red_bot_3)

        blue_bot_3 = Blue1(self, 250-32, 400-32)
        self.add_room_object(blue_bot_3)
        blue_bots.append(blue_bot_3)

        red_bot_4 = Red1(self, 550, 500-32)
        self.add_room_object(red_bot_4)
        red_bots.append(red_bot_4)

        blue_bot_4 = Blue1(self, 250-32, 500-32)
        self.add_room_object(blue_bot_4)
        blue_bots.append(blue_bot_4)

        red_bot_5 = Red1(self, 700, 300-26)
        self.add_room_object(red_bot_5)
        red_bots.append(red_bot_5)

        blue_bot_5 = Blue1(self, 100-32, 300-26)
        self.add_room_object(blue_bot_5)
        blue_bots.append(blue_bot_5)
