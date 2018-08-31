from GameFrame import RoomObject


class Bot(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
