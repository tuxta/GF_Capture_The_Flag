from GameFrame import Level, Globals, RedFlag, BlueFlag, TextObject
from Objects import Red1, Red2, Red3, Red4, Red5
from Objects import Blue1, Blue2, Blue3, Blue4, Blue5


class Arena(Level):
    def __init__(self, screen):
        Level.__init__(self, screen)

        self.set_background_image("background.png")

        Globals.red_flag = RedFlag(self, 200, Globals.SCREEN_HEIGHT / 2 - 26)
        Globals.blue_flag = BlueFlag(self, Globals.SCREEN_WIDTH - 232, Globals.SCREEN_HEIGHT / 2 - 26)

        self.add_room_object(Globals.red_flag)
        self.add_room_object(Globals.blue_flag)

        Globals.red_bots.append(Red1(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4))
        Globals.blue_bots.append(Blue1(self, 108, Globals.SCREEN_HEIGHT / 3))
        Globals.red_bots.append(Red2(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4 * 2))
        Globals.blue_bots.append(Blue2(self, 108, Globals.SCREEN_HEIGHT / 3 * 2))
        Globals.red_bots.append(Red3(self, Globals.SCREEN_WIDTH - 250, Globals.SCREEN_HEIGHT / 4 * 3))
        Globals.blue_bots.append(Blue3(self, 228, Globals.SCREEN_HEIGHT / 4))
        Globals.red_bots.append(Red4(self, Globals.SCREEN_WIDTH - 140, Globals.SCREEN_HEIGHT / 3))
        Globals.blue_bots.append(Blue4(self, 228, Globals.SCREEN_HEIGHT / 4 * 2))
        Globals.red_bots.append(Red5(self, Globals.SCREEN_WIDTH - 140, Globals.SCREEN_HEIGHT / 3 * 2))
        Globals.blue_bots.append(Blue5(self, 228, Globals.SCREEN_HEIGHT / 4 * 3))

        for i in range(len(Globals.red_bots)):
            self.add_room_object(Globals.red_bots[i])

        for i in range(len(Globals.blue_bots)):
            self.add_room_object(Globals.blue_bots[i])
            Globals.blue_bots[i].rotate(180)

        Globals.background_music = self.load_sound('battle-music.ogg')
        Globals.background_music.play(-1)

        self.counter = 3600
        self.seconds = 120
        text_minutes = int(self.seconds / 60)
        text_seconds = self.seconds % 60
        self.counter_text = TextObject(self, Globals.SCREEN_WIDTH/2 - 50, 10, "{}:{:02d}".format(text_minutes, text_seconds))
        self.add_room_object(self.counter_text)
        self.counter_text.x = Globals.SCREEN_WIDTH / 2 - self.counter_text.width/2

        self.blue_score_text = TextObject(self, Globals.SCREEN_WIDTH / 2 - 50, 10, str(Globals.blue_enemy_side_time), 30)
        self.add_room_object(self.blue_score_text)
        self.blue_score_text.x = Globals.SCREEN_WIDTH / 3 - self.counter_text.width / 2

        self.red_score_text = TextObject(self, Globals.SCREEN_WIDTH / 2 - 50, 10, str(Globals.red_enemy_side_time), 30)
        self.add_room_object(self.red_score_text)
        self.red_score_text.x = Globals.SCREEN_WIDTH / 3 * 2 - self.counter_text.width / 2

        self.set_timer(3600, self.timed_out)

    def tick(self):
        self.counter -= 1
        if self.counter % 30 == 0:
            self.seconds -= 1
            text_minutes = int(self.seconds / 60)
            text_seconds = self.seconds % 60
            self.counter_text.text = "{}:{:02d}".format(text_minutes, text_seconds)
            self.counter_text.update_text()
            self.counter_text.x = Globals.SCREEN_WIDTH / 2 - self.counter_text.width / 2

            self.blue_score_text.text = str(Globals.blue_enemy_side_time)
            self.blue_score_text.update_text()

            self.red_score_text.text = str(Globals.red_enemy_side_time)
            self.red_score_text.update_text()

    def timed_out(self):
        if Globals.red_enemy_side_time > Globals.blue_enemy_side_time:
            Globals.winner = 'Red'
        elif Globals.blue_enemy_side_time > Globals.red_enemy_side_time:
            Globals.winner = 'Blue'
        else:
            Globals.winner = 'Draw'
        self.running = False

