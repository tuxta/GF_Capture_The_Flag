from GameFrame import BlueBot
from GameFrame import Globals
import pygame


class Blue1(BlueBot):
    def __init__(self, room, x, y):
        BlueBot.__init__(self, room, x, y)

        self.handle_key_events = True
        self.handle_mouse_events = True

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.rotate(10)
        elif key[pygame.K_RIGHT]:
            self.rotate(-10)

        if key[pygame.K_UP]:
            x, y = self.get_direction_coordinates(self.curr_rotation, 5)
            self.x += x
            self.y += y

        if key[pygame.K_DOWN]:
            new_angle = self.curr_rotation + 180

            next_x, next_y = self.get_direction_coordinates(new_angle, 2)
            self.x += next_x
            self.y += next_y

    def mouse_event(self, mouse_x, mouse_y, button_left, button_middle, button_right):
        if button_left:
            self.rotate_to_coordinate(mouse_x, mouse_y)

    def step(self):
        BlueBot.step(self)

    def handle_collision(self, other):
        BlueBot.handle_collision(self, other)

