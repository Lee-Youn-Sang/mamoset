import random
from pico2d import *
from map import *
from character import *
from obstacle import *
import game_framework
import second_logo

name = "Game"

block = None
background = None
lion = None
enemy = None
tank = None

def enter():
    global block, background, lion, enemy, tank
    block = Block()
    background = Background()
    lion = Lion()
    enemy = Enemy()
    tank = Tank()

def exit():
    global block, background, lion, enemy, tank
    del(block)
    del(background)
    del(lion)
    del(enemy)
    del(tank)


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
        else:
            lion.handle_event(event)



def update():
    lion.update()
    enemy.update()
    tank.update()
    pass

def draw():
    clear_canvas()
    block.draw()
    background.draw()
    lion.draw()
    enemy.draw()
    tank.draw()
    update_canvas()


