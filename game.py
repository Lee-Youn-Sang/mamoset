import random
from pico2d import *
from map import *
from character import *
from obstacle import *
import game_framework
import second_logo

name = "Game"

block = None
background = None
lion = None
enemy = None
tank = None

def enter():
    global block, background, lion, enemy, tank
    block = Block()
    background = Background()
    lion = Lion()
    enemy = Enemy()
    tank = Tank()

def exit():
    global block, background, lion, enemy, tank
    del(block)
    del(background)
    del(lion)
    del(enemy)
    del(tank)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(second_logo)

def update():
    lion.update()
    enemy.update()
    tank.update()
    pass

def draw():
    clear_canvas()
    block.draw()
    background.draw()
    lion.draw()
    enemy.draw()
    tank.draw()
    update_canvas()

def main():

    open_canvas()

    global boy
    global running

    running = True

    current_time = get_time()

    while running:
        handle_events()

        clear_canvas()
        update_canvas()

        frame_time = get_time() - current_time
        frame_rate = 1.0 / frame_time
        print("Frame Rate: %f fps, Frame Time : %f sec, " %(frame_rate, frame_time))

        current_time += frame_time

    close_canvas()


if __name__ == '__main__':
    main()