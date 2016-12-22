import game_framework
from score import *
from pico2d import *
import Spring_Map
import second_logo

name = "Result_State"
image = None;


def enter():
    global result, font, x, y, score, ranking_data, f

    result = load_image('Resource\\result.png')
    font = load_font('Resource\\goindol.ttf',70)

    score = Score()
    ranking_data = Spring_Map.ranking_data

    x = 0
    y = 0

    ranking_data.append({'score' : score.score})

def exit():
    global image
    del(image)

def update():
    global result_time

    if (result_time >1.0):
        result_time = 10

    result_time += 0.001


def handle_events():
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.button) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(second_logo)

def draw():
    global x, y, font, score

    clear_canvas()
    result.draw(400, 300)

    font.draw(250, 380, 'SCORE : %d' % score.score,(0, 0, 0))
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass






