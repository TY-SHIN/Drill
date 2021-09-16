from pico2d import *

def draw_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
while True:
    while x<800:
        draw_all(x,y)
        x+=2
        delay(0.01)
    while y<600:
        draw_all(x,y)
        y+=2
        delay(0.01)
    while x>0:
        draw_all(x,y)
        x-=2
        delay(0.01)
    while y>90:
        draw_all(x,y)
        y-=2
        delay(0.01)

    

delay(5)

close_canvas()
