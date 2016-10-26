import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "My_game"

boy = None
grass = None
font = None



class Block:
    def __init__(self):
        self.image = load_image('block.png')

    def draw(self):
        self.image.draw(400, 20)

class Sky:
    def __init__(self):
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


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(start_title)


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


def main():
    pass



