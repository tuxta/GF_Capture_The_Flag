from GameFrame import RedBot, Globals
import math


class Red1(RedBot):
    def __init__(self, room, x, y):
        RedBot.__init__(self, room, x, y)

    def tick(self):
        if self.has_flag:
            self.turn_towards(Globals.SCREEN_WIDTH, self.y)
            self.drive_forward(Globals.FAST)
        elif self.x >= Globals.SCREEN_WIDTH/2:
            distance = self.direct_to_closest_enemy()
            if distance < 100:
                self.drive_forward(Globals.FAST)
            else:
                self.drive_forward(Globals.SLOW)
        else:
            self.turn_towards(Globals.red_flag.x, Globals.red_flag.y, Globals.FAST)
            self.drive_forward(Globals.FAST)

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

        self.turn_towards(closest_bot.x, closest_bot.y, Globals.FAST)
        return math.sqrt(shortest_distance)
