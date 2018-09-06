from GameFrame import BlueBot
from GameFrame import Globals
import math


class Blue1(BlueBot):
    def __init__(self, room, x, y):
        BlueBot.__init__(self, room, x, y)

    def step(self):
        BlueBot.step(self)

        if self.x <= Globals.SCREEN_WIDTH/2:
            distance = self.direct_to_closest_enemy()
            if distance < 100:
                self.move_in_direction(self.curr_rotation, Globals.FAST)
            else:
                self.move_in_direction(self.curr_rotation, Globals.SLOW)
        else:
            self.rotate_to_coordinate(Globals.blue_flag.x, Globals.blue_flag.y)
            self.move_in_direction(self.curr_rotation, Globals.FAST)

    def handle_collision(self, other):
        BlueBot.handle_collision(self, other)

    def direct_to_closest_enemy(self):
        closest_bot = Globals.red_bots[0]
        x_dist = abs(closest_bot.x - self.x)
        y_dist = abs(closest_bot.y - self.y)
        shortest_distance = x_dist*x_dist + y_dist*y_dist
        for curr_bot in Globals.red_bots:
            x_dist = abs(curr_bot.x - self.x)
            y_dist = abs(curr_bot.y - self.y)
            if x_dist == 0 or y_dist == 0:
                curr_bot_dist = x_dist*x_dist + y_dist*y_dist
            else:
                curr_bot_dist = x_dist*x_dist + y_dist*y_dist
            if curr_bot_dist < shortest_distance:
                shortest_distance = curr_bot_dist
                closest_bot = curr_bot

        self.rotate_to_coordinate(closest_bot.x, closest_bot.y)
        return math.sqrt(shortest_distance)
