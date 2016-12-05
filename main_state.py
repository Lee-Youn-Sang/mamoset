import random
import json
import os
import time

from pico2d import *
from ryan import *
from map import *
from obstacle import *
import game_framework
import second_logo


name = "MainState"

ryan = None
background = None
obstacle1 = None
obstacle2 = None
obstacle3 = None
obstacle4 = None
font = None

score = 0
current_time = 0.0


# 원인을 알 수 없는 error......
# 차후 고치기 (미치겠다...)
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

# Calculate frame_time

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global ryan, background, obstacle1, obstacle2, obstacle3, obstacle4, font

    ryan = Ryan("Run")
    background = Background(800, 600)
    font = load_font('goindol.TTF')
    obstacle1 = OB1().create()
    obstacle2 = OB2().create()
    obstacle3 = OB3().create()
    obstacle4 = OB4().create()

    start = time.time()

def exit():
    global ryan, background, obstacle1, obstacle2, obstacle3, obstacle4, font
    del(ryan)
    del(background)
    del(font)

    for obstacle1 in obstacle1:
        obstacle1.remove(obstacle1)
        del(obstacle1)

    for obstacle2 in obstacle2:
        obstacle2.remove(obstacle2)
        del(obstacle2)

    for obstacle3 in obstacle3:
        obstacle3.remove(obstacle3)
        del(obstacle3)

    for obstacle4 in obstacle4:
        obstacle4.remove(obstacle4)
        del(obstacle4)


    end = time.time()


def pause():
    pass


def resume():
    pass


def handle_events():
    global ryan
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(second_logo)

        else:
            ryan.handle_events(event)

# class update

def update():
    global ryan, background, obstacle1, obstacle2, obstacle3, obstacle4, score
    score += 10

    frame_time = get_frame_time()
    ryan.update()
    background.update(frame_time)

    for Obstacle1 in obstacle1:
        Obstacle1.update(frame_time)
        if collide(ryan, Obstacle1) and ryan.state != "Collide":
            ryan.bump("Collide")

    for Obstacle2 in obstacle2:
        Obstacle2.update(frame_time)
        if collide(ryan, Obstacle2) and ryan.state != "Collide":
            ryan.bump("Collide")

    for Obstacle3 in obstacle3:
        Obstacle3.update(frame_time)
        if collide(ryan, Obstacle3) and ryan.state != "Collide":
            ryan.bump("Collide")

    for Obstacle4 in obstacle4:
        Obstacle4.update(frame_time)
        if collide(ryan, Obstacle4) and ryan.state != "Collide":
            ryan.bump("Collide")

# draw class

def draw():
    global ryan, background, obstacle1, obstacle2, obstacle3, obstacle4, score, font
    clear_canvas()
    background.draw()

    font.draw(650, 550, 'SCORE : %d' % score)
    font.draw(490, 550, '<< Ryan Runner!! >>')

    for Obstacle1 in obstacle1:
        Obstacle1.draw_bb()

    for Obstacle2 in obstacle2:
        Obstacle2.draw_bb()

    for Obstacle3 in obstacle3:
        Obstacle3.draw_bb()

    for Obstacle4 in obstacle4:
        Obstacle4.draw_bb()

    ryan.draw_bb()
    delay(0.03)
    update_canvas()
