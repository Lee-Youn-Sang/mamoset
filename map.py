from pico2d import *

class Block:
    def __init__(self):
        self.Block = load_image('image\\block.png')

    def draw(self):
        self.Block.draw(400, 30)



class Background:
    def __init__(self):
        self.image = load_image('image\\background.png')

    def draw(self):
        self.image.draw(400, 330)





