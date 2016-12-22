import random
import json
import os
import time

from ryan import *
from back_ground import *
from obstacle import *
from item import *
from score import *

import game_framework
import second_logo
import result_state
import Spring_Map_select
import Sky_Map_select

name = "Sky_Map"

background2 = None
ob5 = None
ob6 = None
ob7 = None
ob8 = None
hp_heart = None
objects = []
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
    global lion, background2, score,  ob5, ob6, ob7, ob8, start, hp_heart, font, objects, ryan

    lion = Sky_Map_select.lion_do
    ryan = Sky_Map_select.ryan_select
    background2 = Background2(800, 600)
    score = Score()

    ob5 = OB5().create()
    ob6 = OB6().create()
    ob7 = OB7().create()
    ob8 = OB8().create()
    hp_heart = Hp_Heart().create()
    objects = [ob5, ob6, ob7, ob8, hp_heart]

    font = load_font('Resource\\goindol.ttf')

def exit():
    global lion, background2, ob5, ob6, ob7, ob8, start, end, hp_heart, objects
    del(lion)
    del(background2)


    for list in objects:
        for dicti in list:
            list.remove(dicti)
            del(dicti)
        del(list)

def pause():
    pass


def resume():
    pass


def handle_events():
    global cookie
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(second_logo)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            game_framework.change_state(Spring_Map_select)

        else:
            lion.handle_events(event)

def update():
    global lion, ryan, background2, ob5, ob6, ob7, ob8, hp_heart, objects, score

    frame_time = get_frame_time()
    lion.update(frame_time)
    background2.update(frame_time)
    score.sky_map_score()


    for list in objects:
        for dict in list:
            dict.update(frame_time)
            if collide(lion, dict):
                if list == hp_heart:
                    list.remove(dict)
                    lion.heal(dict)
                    for dict in list:
                        dict.state = "None"
                else:
                    lion.state = "Smashing"

    if (Ryan.hp <= 0):
        game_framework.change_state(result_state)


def draw():
    global lion, background2, objects, score

    clear_canvas()
    background2.draw()

    for list in objects:
        for dict in list:
            dict.draw()

    font.draw(680, 550, 'SCORE : %d' % score.score)
    font.draw(490, 550, '<< Ryan Runner!! >>')
    font.draw(70, 550, 'BGM - Skycastle_Laputa')
    lion.draw()

    delay(0.03)
    update_canvas()