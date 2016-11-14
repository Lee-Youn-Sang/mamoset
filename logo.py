import game_framework
import second_logo
from pico2d import *


name = "StartState"
image = None
kakao = None
logo_time = 0.0


def enter():
    global image, title
    image = load_image('images\\LY_company.png')

def exit():
    global image
    del(image)
    close_canvas()


def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        game_framework.push_state(second_logo)
    delay(0.05)
    logo_time += 0.02

def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()
    pass


def pause(): pass

def resume(): pass




