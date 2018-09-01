from GameFrame import RoomObject
from GameFrame import Globals


class Bot(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

    def step(self):
        if self.x <= 0:
            self.blocked()
        elif self.x >= Globals.SCREEN_WIDTH - self.width:
            self.blocked()

        if self.y <= 0:
            self.blocked()
        elif self.y >= Globals.SCREEN_HEIGHT - self.height:
            self.blocked()
