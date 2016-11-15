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
    global lion, background, obstacle1, obstacle2, obstacle3, start

    lion = Lion("Run")
    background = Background(800, 600)
    obstacle1 = OB1().create()
    obstacle2 = OB2().create()
    obstacle3 = OB3().create()


    start = time.time()

def exit():
    global lion, background, obstacle1, obstacle2, obstacle3, start
    del(lion)
    del(background)

    for obstacle1 in obstacle1:
        obstacle1.remove(obstacle1)
        del(obstacle1)

    for obstacle2 in obstacle2:
        obstacle2.remove(obstacle2)
        del (obstacle2)

    for obstacle3 in obstacle3:
        obstacle3.remove(obstacle3)
        del(obstacle3)


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
    global lion, background, obstacle1, obstacle2, obstacle3

    frame_time = get_frame_time()
    lion.update()
    background.update(frame_time)

    for Obstacle1 in obstacle1:
        Obstacle1.update(frame_time)
        if collide(lion, Obstacle1) and lion.state != "Collide":
            lion.bump("Collide")

    for Obstacle2 in obstacle2:
        Obstacle2.update(frame_time)
        if collide(lion, Obstacle2) and lion.state != "Collide":
            lion.bump("Collide")

    for Obstacle3 in obstacle3:
        Obstacle3.update(frame_time)
        if collide(lion, Obstacle3) and lion.state != "Collide":
            lion.bump("Collide")


def draw():
    global lion, background, obstacle1, obstacle2, obstacle3
    clear_canvas()
    background.draw()

    for Obstacle1 in obstacle1:
        Obstacle1.draw()
        #Obstacle1.draw_bb()

    for Obstacle2 in obstacle2:
        Obstacle2.draw()
        #Obstacle2.draw_bb()

    for Obstacle3 in obstacle3:
        Obstacle3.draw()
        #Obstacle3.draw_bb()


    lion.draw()
#    lion.draw_bb()

    delay(0.03)
    update_canvas()