from GameFrame import RoomObject
from GameFrame import Globals


class Bot(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.starting_x = x
        self.starting_y = y
        self.has_flag = False

    def step(self):
        if self.x <= 0:
            self.blocked()
        elif self.x >= Globals.SCREEN_WIDTH - self.width:
            self.blocked()

        if self.y <= 0:
            self.blocked()
        elif self.y >= Globals.SCREEN_HEIGHT - self.height:
            self.blocked()

        self.frame()

    def frame(self):
        pass

    def turn_left(self, speed=Globals.SLOW):
        pass

    def turn_right(self, speed=Globals.SLOW):
        pass

    def turn_towards(self, x, y, speed=Globals.SLOW, direction=Globals.RIGHT):
        pass

    def turn_away(self, x, y, speed, direction=Globals.LEFT):
        pass

    def drive_forward(self, speed=Globals.SLOW):
        pass

    def drive_backward(self):
        pass
