from GameFrame import RoomObject


class BlueFlag(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        red_flag_image = self.load_image('flag_blue.png')
        self.set_image(red_flag_image, 32, 32)
