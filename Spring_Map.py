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

name = "Spring_Map"

lion = None
background = None
ob1 = None
ob2 = None
ob3 = None
ob4 = None
hp_heart = None
object = []
ranking_data = []
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
    global lion, background, ob1, ob2, ob3, ob4, start, hp_heart, font, objects, score, ryan, f, ranking_data

    lion = Spring_Map_select.lion_do
    ryan = Spring_Map_select.ryan_select
    background = Background1(800, 600)
    score = Score()
    ob1 = OB1().create()
    ob2 = OB2().create()
    ob3 = OB3().create()
    ob4 = OB4().create()
    hp_heart = Hp_Heart().create()
    objects = [ob1, ob2, ob3, ob4, hp_heart]
    font = load_font('Resource\\goindol.ttf')

def exit():
    global lion, background, ob1, ob2, ob3, ob4, start, hp_heart, objects, score
    del(lion)
    del(background)

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
    global lion
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(second_logo)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_framework.change_state(Sky_Map_select)
        else:
            lion.handle_events(event)

def update():
    global lion, ryan, background, ob1, ob2, ob3, ob4, hp_heart, objects, score

    frame_time = get_frame_time()
    background.update(frame_time)
    score.spring_map_score()
    lion.update(frame_time)


    for list in objects:
        for dicti in list:
            dicti.update(frame_time)
            if collide(lion, dicti):
                if list == hp_heart:
                    list.remove(dicti)
                    lion.heal(dicti)
                    for dicti in list:
                        dicti.state = "None"
                else:
                    lion.state = "Smashing"

    if (Ryan.hp <= 0):
        game_framework.change_state(result_state)

def draw():
    global lion, background, objects, score
    clear_canvas()
    background.draw()

    for list in objects:
        for dicti in list:
            dicti.draw()

    font.draw(680, 550, 'SCORE : %d' % score.score)
    font.draw(490, 550, '<< Ryan Runner!! >>')
    font.draw(70, 550, 'BGM - Spring Song')
    lion.draw()

    delay(0.03)
    update_canvas()