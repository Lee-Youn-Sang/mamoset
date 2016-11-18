from pico2d import *

class Background:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self, w, h):
        self.speed = 0
        self.left = 0
        self.left2 = 0
        self.width = w
        self.height = h
        self.Background = load_image('images\\Map\\backg.png')
        self.bgm = load_music('sound\\football.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def draw(self):
        x = int(self.left)
        w = min(self.Background.w - x, self.width)
        self.Background.clip_draw_to_origin(x, 0, w, self.height, 0, 0)
        self.Background.clip_draw_to_origin(0, 0, self.width - w, self.height, w, 0)

    def update(self, frame_time):
        self.speed = 1000
        self.left = (self.left + frame_time * self.speed) % self.Background.w