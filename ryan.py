from pico2d import *
import game_framework
import second_logo

class Ryan:
    image = None
    def __init__(self, state):
        self.x = 100
        self.y = 20
        self.frame = 0
        self.map_size = 0
        self.jump = 0
        self.strength = 0
        self.collision_time = 0
        self.state = state
        self.state = "Run"

        if Ryan.image == None:
            self.Ryan_run = load_image('images\\Character\\ryan_run.png')
            self.Ryan_slide = load_image('images\\Character\\ryan_slide.png')
            self.Ryan_jump1 = load_image('images\\Character\\ryan_jump.png')
            self.Ryan_jump2 = load_image('images\\Character\\ryan_jump2.png')
            self.Ryan_collide = load_image('images\\Character\\ryan_collid.png')

    def bump(self, state):
        self.state = state
        if self.collision_time < 3:
            self.collision_time += 1
            self.map_size += 0

        else:
            self.state = "Run"
            self.collision_time = 0

    def update(self):

        if self.map_size > 2000:
            self.map_size = 0

        self.strength()
        if self.state == "Run":
            self.map_size += 1
            self.frame = (self.frame + 1) % 6
        elif self.state == "Jump" and self.y <= 210:
            self.state = "Run"
        elif self.state == "Slide" or self.state == "Jump":
            self.map_size += 1
        elif self.state == "Collide":
            self.bump("Collide")

        if self.state == "Jump" and (self.map_size >= 1440 and self.map_size <= 1550):
            if (self.y - 40 - self.strength) > 210:
                self.strength += 2
                self.y -= self.strength / 2
            else:
                self.y = 250
                self.strength = 0
        print("size : ", self.map_size)

    def gravity(self):
        if (self.y - 40 - self.strength) > 160:
            self.jump_gravity += 2
            self.y -= self.strength / 2
        else:
            self.y = 200
            self.strength = 0

    def draw(self):
        if self.state == "Run":
            self.Ryan_run.draw(self.x, self.y)
        elif self.state == "Slide":
            self.Ryan_slide.draw(self.x, self.y - 30)
        elif self.state == "Collide":
            self.Ryan_collide.draw(self.x, self.y)
        elif self.state == "Jump":
            if self.jump % 2 == 1:
                self.Ryan_jump1.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.Ryan_jump2.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 30, self.x + 15, self.y + 10
        elif self.state == "Slide":
            return self.x - 5 , self. y - 50, self.x + 25, self.y - 20
        elif self.state == "Jump":
            return self.x - 15, self. y - 10, self.x + 25, self.y + 10
        elif self.state == "Collide":
            return self.x - 0, self. y - 0, self.x + 0, self.y + 0

    def handle_events(self, event):
        events = get_events()

        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                self.state = "Slide"

            elif event.key == SDLK_UP:
                self.state = "Jump"
                self.jump += 1
                if (self.y - 40) == 160:
                    self.jump_gravity = -30

                if (self.map_size >= 1440 and self.map_size <= 2000) and (self.y - 40) == 210:
                    self.jump_gravity = -30


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                self.state = "Run"


