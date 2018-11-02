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

        Globals.red_bots.append(Red1(self, 550, 92))
        Globals.blue_bots.append(Blue1(self, 108, 192))
        Globals.red_bots.append(Red2(self, 550, 282))
        Globals.blue_bots.append(Blue2(self, 108, 392))
        Globals.red_bots.append(Red3(self, 550, 492))
        Globals.blue_bots.append(Blue3(self, 228, 92))
        Globals.red_bots.append(Red4(self, 660, 192))
        Globals.blue_bots.append(Blue4(self, 228, 282))
        Globals.red_bots.append(Red5(self, 660, 392))
        Globals.blue_bots.append(Blue5(self, 228, 492))

        for i in range(len(Globals.red_bots)):
            self.add_room_object(Globals.red_bots[i])

        for i in range(len(Globals.blue_bots)):
            self.add_room_object(Globals.blue_bots[i])
            Globals.blue_bots[i].rotate(180)
