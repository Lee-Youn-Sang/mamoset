from back_ground import *
from pico2d import *
from ryan import *
import game_framework
import Spring_Map
import Sky_Map_select

name = "Spring_Map_Select"

background = None
ryan = None
lion_do = None
ryan_select = None
current_time = 0.0



def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global background, ryan, font, x, y, ryan_select

    x = 0
    y = 0

    background = Background1(800,600)
    ryan = Ryan_Select()
    ryan_select = None
    font = load_font('Resource\\goindol.ttf', 50)

def exit():
    global background, ryan
    del(background)
    del(ryan)


def handle_events():
    global x, y, lion_do, ryan_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
                game_framework.change_state(Sky_Map_select)


            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 600 - event.y

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if (280 <= x <= 620) and (130 <= y <= 300) and Ryan().hp > 0:
                    lion_do = Ryan()
                    ryan_select = True
                    game_framework.change_state(Spring_Map)



def draw():
    global ryan, score
    clear_canvas()
    background.draw()
    ryan.draw()
    font.draw(220, 470, '<< Stage Select >>')
    update_canvas()

def update():
    frame_time = get_frame_time()
    background.update(frame_time)
    ryan.update()
    delay(0.03)


def pause():
    pass


def resume():
    pass






