import random
import json
from pico2d import *

hp_heart_data = open('Data\\Hp_Heart.txt', 'r')
hp_heart = json.load(hp_heart_data)
hp_heart_data.close()

class Spring_Map_SPEED:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Sky_Map_SPEED:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 40.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Hp_Heart:

    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = "None"
        self.collision_time = 0

        if Hp_Heart.image == None:
            self.Hp_Heart = load_image('Resource\\Item\\hp_heart.png')

    def create(self):
        hp_state_table = {
            "Hp" : self.Hp_Heart
        }

        hp = []

        for name in hp_heart:
            item = Hp_Heart()
            item.name = name
            item.x = hp_heart[name]['x']
            item.y = hp_heart[name]['y']
            item.state = hp_state_table[hp_heart[name]['state']]
            hp.append(item)

        return hp

    def update(self, frame_time):
        if Spring_Map_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = frame_time * Spring_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance
            self.collision_time = 0

        elif self.state == "Smashing":
            if self.collision_time < 30:
                self.collision_time += 10
                for i in range(2):
                   if self.x > 150:
                      self.x += 20
                   else:
                     self.x -= 20

        elif self.state != "Smashing":
            self.distance = frame_time * Spring_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance
            self.collision_time = 0

    def draw(self):
        self.Hp_Heart.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

