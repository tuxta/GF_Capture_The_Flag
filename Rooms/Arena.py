from GameFrame import Level, Globals, RedFlag, BlueFlag
from Objects import Red1
from Objects import Blue1
import os


class Arena(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)
        print(os.getcwd())

        self.set_background_image("background.png")

        Globals.red_flag = RedFlag(self, 10, 274)
        Globals.blue_flag = BlueFlag(self, 758, 274)

        self.add_room_object(Globals.red_flag)
        self.add_room_object(Globals.blue_flag)

        rbot1 = Red1(self, 550, 100)
        Globals.red_bots.append(rbot1)
        Globals.red_bots.append(Red1(self, 550, 300))
        Globals.red_bots.append(Red1(self, 550, 468))
        Globals.red_bots.append(Red1(self, 700, 274))

        Globals.blue_bots.append(Blue1(self, 228, 100))
        Globals.blue_bots.append(Blue1(self, 228, 300))
        Globals.blue_bots.append(Blue1(self, 228, 468))
        Globals.blue_bots.append(Blue1(self, 68, 274))

        for i in range(len(Globals.red_bots)):
            self.add_room_object(Globals.red_bots[i])

        for i in range(len(Globals.blue_bots)):
            self.add_room_object(Globals.blue_bots[i])
