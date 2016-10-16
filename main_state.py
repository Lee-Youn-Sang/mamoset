import random
import json
import os

from pico2d import *

import game_framework


name = "MainState"

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
    def __init(self):
        self.image = load_image('sky.png')

    def draw(self):
        self.image.draw(400, 330)


class Lion:
    def __init__(self):
        self.image = load_image('lion.png')

    def draw(self):
        self.image.draw(90, 100)



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
            game_framework.change_state(title_state)
    pass


def update():
    pass


def draw():
    clear_canvas()
    block.draw(400, 30)
    sky.draw(400, 300)
    lion.draw(90, 100)
    update_canvas()
    pass

open_canvas()


running = True;

x = 0
frame = 0
hide_cursor()
while running:
    handle_events()


    clear_canvas()

    block.draw()
    sky.draw()
    lion.draw()

    update_canvas()
    delay(0.05)

close_canvas()




