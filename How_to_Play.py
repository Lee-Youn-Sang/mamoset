from pico2d import *

class Background1:

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.image = load_image('Resource\\Map\\Spring.png')
        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h

        self.bgm = load_music('Resource\\Sound\\Spring_Song.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()

    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width-w, self.screen_height, w, 0)

    def update(self, frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.w
        self.speed = 100



class Background2:

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 30.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.background2 = load_image('Resource\\Map\\Sky.png')
        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h

        self.bgm = load_music('Resource\\Sound\\Skycastle_Laputa.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()

    def draw(self):
        x = int(self.left)
        w = min(self.background2.w - x, self.screen_width)
        self.background2.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.background2.clip_draw_to_origin(0, 0, self.screen_width-w, self.screen_height, w, 0)

    def update(self, frame_time):

        self.left = (self.left + frame_time * self.speed) % self.background2.w
        self.speed = 100
