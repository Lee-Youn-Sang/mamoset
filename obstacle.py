from pico2d import *
import json

running = None;

# Spring_Map Obstacle Data

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

# Sky_Map Obstacle Data

data_file5 = open('Data\\OB5.txt', 'r')
data5 = json.load(data_file5)
data_file5.close()

data_file6 = open('Data\\OB6.txt', 'r')
data6 = json.load(data_file6)
data_file6.close()

data_file7 = open('Data\\OB7.txt', 'r')
data7 = json.load(data_file7)
data_file7.close()

data_file8 = open('Data\\OB8.txt', 'r')
data8 = json.load(data_file8)
data_file8.close()


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

# Stage1 Obstacles

class OB1:
    image = None;

    def __init__(self):
        self.x = 0
        self.y = 0
        if self.image == None:
            self.Obsta1 = load_image('Resource\\Obstacle\\ob1.png')

    def create(self):
        obstacle_state_table = {
            "Obsta1" : self.Obsta1
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
        if frame_time * Spring_Map_SPEED.RUN_SPEED_PPS < 18:
            self.distance = frame_time * Spring_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance

    def draw(self):
        self.Obsta1.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300

class OB2:
    image = None;

    def __init__(self):
        self.x = 0
        self.y = 0
        if self.image == None:
            self.Obsta2 = load_image('Resource\\Obstacle\\ob2.png')

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

    def smash(self, state):
        self.state = state

        if self.collision_time < 3:
            self.state = "Smashing"
            self.collision_time += 1
            self.distance = 0
        else:
            self.state = "None"
            self.collision_time = 0

    def update(self, frame_time):
        if frame_time * Spring_Map_SPEED.RUN_SPEED_PPS < 18:
            self.distance = frame_time * Spring_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance

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
        if self.image == None:
            self.Obsta3 = load_image('Resource\\Obstacle\\ob3.png')

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
        if frame_time * Spring_Map_SPEED.RUN_SPEED_PPS < 18:
            self.distance = frame_time * Spring_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance


    def draw(self):
        self.Obsta3.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class OB4:
    image = None;

    def __init__(self):
        self.x = 0
        self.y = 0
        if self.image == None:
            self.Obsta4 = load_image('Resource\\Obstacle\\ob4.png')

    def create(self):
        obstacle_state_table = {
            "Obsta4": self.Obsta4
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
        if frame_time * Spring_Map_SPEED.RUN_SPEED_PPS< 18:
            self.distance = frame_time * Spring_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance

    def draw(self):
        self.Obsta4.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 20, self.x + 15, self.y + 30

class OB5:
    image = None;

    def __init__(self):
        self.x = 0
        self.y = 0
        if self.image == None:
            self.Obsta5 = load_image('Resource\\Obstacle\\ob5.png')

    def create(self):
        obstacle_state_table = {
            "Obsta5" : self.Obsta5
        }
        obstacle = []
        for name in data5:
            ob = OB5()
            ob.name = name
            ob.x = data5[name]['x']
            ob.y = data5[name]['y']
            ob.state = obstacle_state_table[data5[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if frame_time * Sky_Map_SPEED.RUN_SPEED_PPS < 21:
            self.distance = frame_time * Sky_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance

    def draw(self):
        self.Obsta5.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300

class OB6:
    image = None;

    def __init__(self):
        self.x = 0
        self.y = 0
        if self.image == None:
            self.Obsta6 = load_image('Resource\\Obstacle\\ob6.png')

    def create(self):
        obstacle_state_table = {
            "Obsta6": self.Obsta6
        }

        obstacle = []
        for name in data6:
            ob = OB6()
            ob.name = name
            ob.x = data6[name]['x']
            ob.y = data6[name]['y']
            ob.state = obstacle_state_table[data6[name]['state']]
            obstacle.append(ob)

        return obstacle

    def smash(self, state):
        self.state = state

        if self.collision_time < 3:
            self.state = "Smashing"
            self.collision_time += 1
            self.distance = 0
        else:
            self.state = "None"
            self.collision_time = 0

    def update(self, frame_time):
        if frame_time * Sky_Map_SPEED.RUN_SPEED_PPS  < 21:
            self.distance = frame_time * Sky_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance

    def draw(self):
        self.Obsta6.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 50


class OB7:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if self.image == None:
            self.Obsta7 = load_image('Resource\\Obstacle\\ob7.png')

    def create(self):
        obstacle_state_table = {
            "Obsta7": self.Obsta7
        }

        obstacle = []
        for name in data7:
            ob = OB7()
            ob.name = name
            ob.x = data7[name]['x']
            ob.y = data7[name]['y']
            ob.state = obstacle_state_table[data7[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if frame_time * Sky_Map_SPEED.RUN_SPEED_PPS< 21:
            self.distance = frame_time * Sky_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance


    def draw(self):
        self.Obsta7.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class OB8:
    image = None;

    def __init__(self):
        self.x = 0
        self.y = 0
        if self.image == None:
            self.Obsta8 = load_image('Resource\\Obstacle\\ob8.png')

    def create(self):
        obstacle_state_table = {
            "Obsta8": self.Obsta8
        }

        obstacle = []
        for name in data8:
            ob = OB8()
            ob.name = name
            ob.x = data8[name]['x']
            ob.y = data8[name]['y']
            ob.state = obstacle_state_table[data8[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if frame_time * Sky_Map_SPEED.RUN_SPEED_PPS < 21:
            self.distance =  frame_time * Sky_Map_SPEED.RUN_SPEED_PPS
            self.x -= self.distance

    def draw(self):
        self.Obsta8.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 20, self.x + 15, self.y + 30




