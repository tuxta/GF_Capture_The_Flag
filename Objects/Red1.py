from GameFrame import RedBot, Globals
import math


class Red1(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)

    def tick(self):

        if self.x >= Globals.SCREEN_WIDTH/2:
            distance = self.direct_to_closest_enemy()
            if distance < 100:
                if self.x > (Globals.SCREEN_WIDTH / 2 + 200):
                    self.move_in_direction(self.curr_rotation, Globals.FAST)
                else:
                    self.rotate_to_coordinate(Globals.red_flag.x, Globals.red_flag.y)
                    self.move_in_direction(self.curr_rotation, Globals.FAST)
            else:
                self.move_in_direction(self.curr_rotation, Globals.SLOW)
        else:
            self.rotate_to_coordinate(Globals.red_flag.x, Globals.red_flag.y)
            self.move_in_direction(self.curr_rotation, Globals.FAST)

    def direct_to_closest_enemy(self):
        closest_bot = Globals.blue_bots[0]
        x_dist = abs(closest_bot.x - self.x)
        y_dist = abs(closest_bot.y - self.y)
        shortest_distance = x_dist*x_dist + y_dist*y_dist
        for curr_bot in Globals.blue_bots:
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
