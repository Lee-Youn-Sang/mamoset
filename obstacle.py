import random
from pico2d import *

class Enemy:
    image = None

    RUN = 0

    def handle_run(self):
        self.x = 700
        if self.x < 0:
            self.state = self.RUN
            self.x = 0

    handle_state = {
        RUN: handle_run
    }

    def update(self):
        self.handle_state[self.state](self)

    def __init__(self):
        self.x, self.y = random.randint(400, 700),100
        self.frame = random.randint(0, 7)
        self.state = self.RUN
        if Enemy.image == None:
            self.image = load_image('image\\enemy.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Tank:
    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def handle_left_run(self):
        self.x += 0.2
        if self.x > 700:
            self.state = self.LEFT_RUN
            self.x = 700

    def handle_right_run(self):
        self.x -= 0.2
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run
    }


    def __init__(self):
        self.x, self.y = random.randint(100, 700),75
        self.frame = random.randint(0, 7)
        self.state = self.RIGHT_RUN
        if Tank.image == None:
            Tank.image = load_image('image\\tank.png')

    def update(self):
        self.handle_state[self.state](self)

    def draw(self):
        self.image.draw(self.x, self.y)
