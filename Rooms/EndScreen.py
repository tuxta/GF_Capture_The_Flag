from GameFrame import Level, TextObject, Globals
import gc


class EndScreen(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)
        winner = Globals.winner + ' Wins'
        winner_text = TextObject(self, 250, 250, winner, 80)
        winner_text.colour = (255, 255, 255)
        winner_text.update_text()
        self.add_room_object(winner_text)

        self.set_timer(120, self.restart)

    def restart(self):
        Globals.red_flag = 0
        Globals.blue_flag = 0
        Globals.red_bots = []
        Globals.blue_bots = []
        gc.collect()
        self.running = False
