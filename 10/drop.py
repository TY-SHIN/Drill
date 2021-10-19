from pico2d import *
from random import randint


class Big_Ball:
    def __init__ (self):
        self.x = randint(0,800+1)
        self.y = 599
        self.speed = randint(1,20+1)
        self.image = load_image('ball41x41.png')

    def drop(self):
        self.y = self.y - self.speed
        if self.y < 30 + 20: self.y = 30 + 20

    def draw(self):
        self.image.draw_now(self.x,self.y)

class Small_Ball:
    def __init__ (self):
        self.x = randint(0,800+1)
        self.y = 599
        self.speed = randint(1,20+1)
        self.image = load_image('ball21x21.png')

    def drop(self):
        self.y = self.y - self.speed
        if self.y < 30 + 10: self.y = 30 + 10

    def draw(self):
        self.image.draw_now(self.x,self.y)


open_canvas()
grass = load_image('grass.png')
big_ball = [Big_Ball() for i in range(1,20+1)]
small_ball = [Small_Ball() for i in range(1,20+1)]

while 1:
    grass.draw_now(400, 30)
    for i in big_ball:
        i.draw()
        i.drop()
    for i in small_ball:
        i.draw()
        i.drop()

    delay(0.1)
    clear_canvas_now()

close_canvas()





delay(5)

close_canvas()