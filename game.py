import random
import json
import os

from pico2d import *

import game_framework
import second_logo



name = "Game"

block = None
sky = None
lion = None
font = None



class Block:
    def __init__(self):
        self.image = load_image('block.png')

    def draw(self):
        self.image.draw(400, 30)


class Sky:
    def __init__(self):
        self.image = load_image('sky.png')

    def draw(self):
        self.image.draw(400, 330)


class Lion:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('lion.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def enter():
    global block, sky, lion
    block = Block()
    sky = Sky()
    lion = Lion()
    pass


def exit():
    global block, sky, lion
    del(block)
    del(sky)
    del(lion)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(second_logo)
    pass


def update():
    lion.update()
    pass


def draw():
    clear_canvas()
    block.draw()
    sky.draw()
    lion.draw()
    update_canvas()
    pass

hide_cursor()


