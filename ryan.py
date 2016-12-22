from pico2d import *

import game_framework

class Ryan:

    image = None;
    state_sound = None;
    hp = 240

    def __init__(self):
        self.x = 100
        self.y = 20
        self.frame = 0
        self.jump = 0
        self.jump_strentgh = 0
        self.collision_time = 0
        self.state = "Running"

        if Ryan.image == None:
            self.Ryan_run = load_image('Resource\\Character\\run.png')
            self.Ryan_slide = load_image('Resource\\Character\\slide.png')
            self.Ryan_jump1 = load_image('Resource\\Character\\hug_jump.png')
            self.Ryan_jump2 = load_image('Resource\\Character\\leap_jump.png')
            self.Ryan_collide = load_image('Resource\\Character\\collide.png')
            self.Ryan_hp = load_image('Resource\\Item\\hp.png')


    def smash(self):
        if self.collision_time < 0.9:
            Ryan.hp -= 60
            self.collision_time += 1
        else:
            self.state = "Running"


    def heal(self, item):
        Ryan.hp += 70

    def update(self, frame_time):
        if frame_time < 0.8:
            Ryan.hp -= 0.1

        self.strentgh()
        if self.state == "Running":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Jumping" and self.y <= 200:
            self.state = "Running"
        elif self.state == "Running":
            self.collision_time = 0
        elif self.state == "Sliding":
            self.collision_time = 0
        elif self.state == "Jumping":
            self.collision_time = 0
        elif self.state == "Smashing":
            self.smash()


    def strentgh(self):
        if (self.y - 40 - self.jump_strentgh) > 160:
            self.jump_strentgh += 3.5
            self.y -= self.jump_strentgh / 2
        else:
            self.y = 200
            self.jump_strentgh = 0

    def draw(self):
        if self.state == "Running":
            self.Ryan_run.draw(self.x, self.y)
        elif self.state == "Sliding":
            self.Ryan_slide.draw(self.x, self.y - 25)
        elif self.state == "Smashing":
            self.Ryan_collide.draw(self.x - 5, self.y)
        elif self.state == "Jumping":
            if self.jump % 2 == 1:
                self.Ryan_jump1.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.Ryan_jump2.draw(self.x, self.y)
        self.Ryan_hp.draw_to_origin(500, 500, Ryan.hp, 50)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state == "Running":
            return self.x - 20, self. y - 30, self.x + 15, self.y + 10
        elif self.state == "Sliding":
            return self.x - 5 , self. y - 50, self.x + 25, self.y - 30
        elif self.state == "Jumping":
            return self.x - 15, self. y - 10, self.x + 25, self.y + 10
        elif self.state == "Smashing":
            return self.x - 0, self. y - 0, self.x + 0, self.y + 0

    def handle_events(self, event):
        events = get_events()

        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                self.state = "Sliding"

            elif event.key == SDLK_UP:
                self.state = "Jumping"
                self.jump += 1
                if (self.y - 40) == 160:
                    self.jump_strentgh = -40

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                self.state = "Running"

class Ryan_Select:
    image = None

    def __init__(self):
        self.x = 400
        self.y = 270
        self.frame = 0
        self.state = "Running"

        if Ryan.image == None:
            self.Ryan_run = load_image('Resource\\Ryan_Fighting.png')
            self.Ryan_select = load_image('Resource\\Game_Start.png')

    def update(self):
        self.state = "Running"
        self.frame = (self.frame + 1) % 6

    def draw(self):
        if self.state == "Running":
            self.Ryan_run.draw(self.x, self.y)
            self.Ryan_select.draw(400, 150)

