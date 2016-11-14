import random
import json
import os
import time

from pico2d import *
from lion import *
from map import *
from obstacle import *
import game_framework
import second_logo


name = "MainState"

lion = None
background = None
obstacle1 = None
obstacle3 = None
hurdle = None
current_time = 0.0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global lion, background, ground, obstacle1, obstacle3, hurdle, \
            start

    lion = Lion("Run")
    background = Background(800, 600)
    ground = Background(800, 150)
    obstacle1 = OB1().create()
    obstacle3 = OB3().create()
    hurdle = Hurdle().create()

    start = time.time()

def exit():
    global lion, background, ground, obstacle1, obstacle3, hurdle, start
    del(lion)
    del(background)
    del(ground)

    for fork in obstacle1:
        obstacle1.remove(fork)
        del(fork)
    del(obstacle1)

    for thorn in obstacle3:
        obstacle3.remove(thorn)
        del(thorn)
    del(obstacle3)

    for thorn in hurdle:
        double_thorn.remove(thorn)
        del(thorn)
    del(hurdle)

    end = time.time()

    print("Clear Time : ", (end - start))


def pause():
    pass


def resume():
    pass


def handle_events():
    global lion
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(second_logo)

        else:
            lion.handle_events(event)

def update():
    global lion, background, ground, obstacle1, obstacle3, hurdle

    frame_time = get_frame_time()
    lion.update()
    background.update(frame_time)
    ground.update(frame_time)

    for Fork in obstacle1:
        Fork.update(frame_time)
        if collide(lion, Fork) and lion.state != "Collide":
            lion.bump("Collide")
    for Thorn in obstacle3:
        Thorn.update(frame_time)
        if collide(lion, Thorn) and lion.state != "Collide":
            lion.bump("Collide")
    for Thorn in hurdle:
        Thorn.update(frame_time)
        if collide(lion, Thorn) and lion.state != "Collide":
            lion.bump("Collide")
            #Thorn.bump("Collide")

def draw():
    global lion, background, ground, obstacle1, obstacle3, hurdle
    clear_canvas()
    background.draw()
    ground.ground_draw()

    for Fork in obstacle1:
        Fork.draw()
        #Fork.draw_bb()
    for Thorn in obstacle3:
        Thorn.draw()
        #Thorn.draw_bb()
    for Thorn in hurdle:
        Thorn.draw()
        #Thorn.draw_bb()

    lion.draw()
#    lion.draw_bb()

    delay(0.03)
    update_canvas()