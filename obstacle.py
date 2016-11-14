from pico2d import *
import json

running = None

obstacle_data_file1_1 = open('Stage_Data\\OB1.txt', 'r')
obstacle_data1_1 = json.load(obstacle_data_file1_1)
obstacle_data_file1_1.close()

obstacle_data_file1_2 = open('Stage_Data\\OB3.txt', 'r')
obstacle_data1_2 = json.load(obstacle_data_file1_2)
obstacle_data_file1_2.close()

obstacle_data_file1_4 = open('Stage_Data\\Hurdle.txt', 'r')
obstacle_data1_4 = json.load(obstacle_data_file1_4)
obstacle_data_file1_4.close()

class Stage_SPEED:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class OB1:
    image = None
    state = "None"

    def __init__(self):
        self.x = 0
        self.y = 0
        if OB1.image == None:
            self.Fork = load_image('images\\Map\\map\\ob1.png')

    def create(self):
        obstacle_state_table = {
            "Fork" : self.Fork
        }
        obstacle = []
        for name in obstacle_data1_1:
            ob = OB1()
            ob.name = name
            ob.x = obstacle_data1_1[name]['x']
            ob.y = obstacle_data1_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Fork.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300


class OB3:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if OB3.image == None:
            self.Thorn = load_image('images\\Map\\map\\ob3.png')

    def create(self):
        obstacle_state_table = {
            "Thorn": self.Thorn
        }

        obstacle = []
        for name in obstacle_data1_2:
            ob = OB3()
            ob.name = name
            ob.x = obstacle_data1_2[name]['x']
            ob.y = obstacle_data1_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Hurdle:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = "None"
        self.collision_time = 0
        if Hurdle.image == None:
            self.Thorn = load_image('images\\Map\\map\\Hurdle.png')

    def create(self):
        obstacle_state_table = {
            "Thorn": self.Thorn
        }

        obstacle = []
        for name in obstacle_data1_4:
            ob = Hurdle()
            ob.name = name
            ob.x = obstacle_data1_4[name]['x']
            ob.y = obstacle_data1_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def bump(self, state):
        self.state = state

        if self.collision_time < 3:
            self.state = "Collide"
            self.collision_time += 1
            self.distance = 0
        else:
            self.state = "None"
            self.collision_time = 0

    def update(self, frame_time):
        if Stage_SPEED.RUN_SPEED_PPS * frame_time < 12 and self.state != "Collide":
            self.distance = Stage_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

        elif Stage_SPEED.RUN_SPEED_PPS * frame_time < 12 and self.state == "Collide":
            self.bump("Collide")

    def draw(self):
        self.Thorn.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 50