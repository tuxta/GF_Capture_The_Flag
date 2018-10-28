from GameFrame import Level, Globals, RedFlag, BlueFlag
from Objects import Red1, Red2, Red3, Red4, Red5
from Objects import Blue1, Blue2, Blue3, Blue4, Blue5


class Arena(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)

        self.set_background_image("background.png")

        Globals.red_flag = RedFlag(self, 50, 274)
        Globals.blue_flag = BlueFlag(self, 718, 274)

        self.add_room_object(Globals.red_flag)
        self.add_room_object(Globals.blue_flag)

        Globals.red_bots.append(Red1(self, 550, 100))
        Globals.red_bots.append(Red2(self, 550, 300))
        Globals.red_bots.append(Red3(self, 550, 468))
        Globals.red_bots.append(Red4(self, 660, 234))
        Globals.red_bots.append(Red5(self, 660, 314))

        Globals.blue_bots.append(Blue1(self, 108, 234))
        Globals.blue_bots.append(Blue2(self, 108, 314))
        Globals.blue_bots.append(Blue3(self, 228, 100))
        Globals.blue_bots.append(Blue4(self, 228, 300))
        Globals.blue_bots.append(Blue5(self, 228, 468))

        for i in range(len(Globals.red_bots)):
            self.add_room_object(Globals.red_bots[i])

        for i in range(len(Globals.blue_bots)):
            self.add_room_object(Globals.blue_bots[i])
            Globals.blue_bots[i].rotate(180)
