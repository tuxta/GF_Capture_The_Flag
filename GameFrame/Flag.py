from GameFrame import RoomObject, Globals


class Flag(RoomObject):
    def __init__(self, room, x, y, image_file_name):
        RoomObject.__init__(self, room, x, y)

        flag_image = self.load_image(image_file_name)
        self.set_image(flag_image, 32, 32)

    def step(self):
        if self.x <= 0 or self.rect.right >= Globals.SCREEN_WIDTH:
            self.blocked()

        if self.y <= 0 or self.rect.bottom >= Globals.SCREEN_HEIGHT:
            self.blocked()
