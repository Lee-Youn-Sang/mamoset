from pico2d import *
import json

running = None

data_file1 = open('Data\\OB1.txt', 'r')
data1 = json.load(data_file1)
data_file1.close()

data_file2 = open('Data\\OB2.txt', 'r')
data2 = json.load(data_file2)
data_file2.close()

data_file3 = open('Data\\OB3.txt', 'r')
data3 = json.load(data_file3)
data_file3.close()

data_file4 = open('Data\\OB4.txt', 'r')
data4 = json.load(data_file4)
data_file4.close()



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
            self.Obsta = load_image('images\\Obstacle\\ob1.png')

    def create(self):
        obstacle_state_table = {
            "Obsta" : self.Obsta
        }
        obstacle = []
        for name in data1:
            ob = OB1()
            ob.name = name
            ob.x = data1[name]['x']
            ob.y = data1[name]['y']
            ob.state = obstacle_state_table[data1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Obsta.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300


class OB2:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = "None"
        self.collision_time = 0
        if OB2.image == None:
            self.Obsta2 = load_image('images\\Obstacle\\ob2.png')

    def create(self):
        obstacle_state_table = {
            "Obsta2": self.Obsta2
        }

        obstacle = []
        for name in data2:
            ob = OB2()
            ob.name = name
            ob.x = data2[name]['x']
            ob.y = data2[name]['y']
            ob.state = obstacle_state_table[data2[name]['state']]
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
        self.Obsta2.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 50

class OB3:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if OB3.image == None:
            self.Obsta3 = load_image('images\\Obstacle\\ob3.png')

    def create(self):
        obstacle_state_table = {
            "Obsta3": self.Obsta3
        }

        obstacle = []
        for name in data3:
            ob = OB3()
            ob.name = name
            ob.x = data3[name]['x']
            ob.y = data3[name]['y']
            ob.state = obstacle_state_table[data3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Obsta3.draw(self.x, self.y + 10)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class OB4:
    image = None
    state = "None"

    def __init__(self):
        self.x = 0
        self.y = 0
        if OB4.image == None:
            self.Obsta4 = load_image('images\\Obstacle\\ob4.png')

    def create(self):
        obstacle_state_table = {
            "Obsta4" : self.Obsta4
        }
        obstacle = []
        for name in data4:
            ob = OB4()
            ob.name = name
            ob.x = data4[name]['x']
            ob.y = data4[name]['y']
            ob.state = obstacle_state_table[data4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Obsta4.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 20, self.x + 15, self.y + 30

