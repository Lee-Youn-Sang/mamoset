from pico2d import *
import time
import game_framework

class Lion:

    image = None

    JUMP, JUMP2 = 0, 1

    def __init__(self):
        self.x = 100
        self.y = 90
        self.frame = 0
        self.image = load_image('image\\lion.png')

    def update(self):
        self.frame = (self.frame) % 5
        self.state = self.JUMP
        if self.state == self.JUMP:
            self.x = min(800, self.x + 50)
        elif self.state == self.JUMP2:
            self.x = max(0, self.x - 50)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 50, 80, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.y, self.JUMP):
                self.state = self.JUMP


def handle_events():
    global running
    global lion
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif (events.type == SDL_KEYDOWN and
              event.key == SDLK_ESCAPE):
            running = False
        else:
            lion.handle_event(event)
