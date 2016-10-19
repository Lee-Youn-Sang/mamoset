from pico2d import *
import game_framework

class Lion:
    image = None

    def __init__(self):
        self.x = 100
        self.y = 90
        self.frame = 0
        self.image = load_image('image\\lion.png')

    def update(self):
        self.frame = (self.frame) % 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 50, 80, self.x, self.y)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                self.y = self.y + 150
            elif event.key == SDLK_DOWN:
                self.y = self.y - 150
