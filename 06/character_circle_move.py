import math
from pico2d import *

def draw_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

theta=0
r = (600-90)//2
while True:
    x = 400 + r * math.sin(theta/360*2*math.pi)
    y = (90+r) + r * math.cos(theta/360*2*math.pi)

    draw_all(x,y)
    
    if theta==359:
        theta = 0
    else:
        theta += 1
    

    

delay(5)

close_canvas()
