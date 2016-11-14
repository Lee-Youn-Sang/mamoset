from pico2d import *

class Background:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.speed = 0
        self.left = 0
        self.left2 = 0
        self.screen_width = w
        self.screen_height = h
        self.Background = load_image('images\\Map\\map\\bac.png')
        self.Ground = load_image('images\\Map\\map\\ground.png')

    def draw(self):
        x = int(self.left)
        w = min(self.Background.w - x, self.screen_width)
        self.Background.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.Background.clip_draw_to_origin(0, 0, self.screen_width-w, self.screen_height, w, 0)

    def ground_draw(self):
        x = int(self.left2)
        ww = min(self.Ground.w - x, self.screen_width)
        self.Ground.clip_draw_to_origin(x, 0, ww, self.screen_height, 0, 0)
        self.Ground.clip_draw_to_origin(0, 0, self.screen_width - ww, self.screen_height, ww, 0)

    def update(self, frame_time):
        self.speed = 100
        self.left = (self.left + frame_time * self.speed) % self.Background.w
        self.left2 = (self.left2 + frame_time * self.speed) % self.Ground.w