import game_framework
import Spring_Map_select
import How_to_Play

from pico2d import *


name = "Second_logo"
image = None


def enter():
    global image
    image = load_image('Resource\\Logo\\Ryan_Runner.png')


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
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                if event.type == SDL_MOUSEMOTION:
                    x, y = event.x, 600 - event.y

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if (110 < x < 292) and (125 < y < 172):
                    game_framework.change_state(Spring_Map_select)
                elif (110 < x < 292) and (58 < y < 100):
                    game_framework.change_state(How_to_Play)

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






