import game_framework
import main_state
import logo
import How_to_play

from pico2d import *


name = "Second_logo"
image = None


def enter():
    global image
    image = load_image('images\\Logo\\lion_il.png')


def exit():
    global image
    del(image)


def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_MOUSEMOTION:
                x, y = event.x, 600 - event.y
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                if 110 < x < 292 and 125 < y < 172:
                    game_framework.change_state(main_state)
                elif 110 < x < 292 and 58 < y < 100:
                    game_framework.change_state(How_to_play)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






