from random import randint
from pico2d import *

open_canvas()
BG = load_image('KPU_GROUND.png')
character = load_image('run_animation.png')
hand = load_image('hand_arrow.png')

def setHandLocation():
    global hand_x
    global hand_y
    hand_x = randint(0, 800)
    hand_y = randint(0, 600)

def setCharDirection():
    global char_direction
    if char_x < hand_x :
        char_direction = 1
    elif hand_x < char_x :
        char_direction = -1
    else:
        char_direction = 0

def moveChar(direction):
    global char_x
    global char_y

    if direction > 0 :
        slope = (hand_y - char_y) // (hand_x - char_x)
        if hand_x - char_x>=5:
            char_x += 5
            char_y += slope*5
        else:
            char_x += 1
            char_y += slope * 1
    elif direction < 0:
        slope = (hand_y - char_y) // (char_x - hand_x)
        if char_x - hand_x >= 5:
            char_x -= 5
            char_y += slope * 5
        else:
            char_x -= 1
            char_y += slope * 5
    else:
        slope = (hand_y - char_y)
        if slope > 5:
            char_y += 5
        elif slope > 0:
            char_y += 1
        elif slope < -5:
            char_y -= 5
        else:
            char_y -= 1


hand_x = 1
hand_y = 1
setHandLocation()
char_x = 0
char_y = 0
char_direction = 1
setCharDirection()

frame = 0

while True:
    clear_canvas()
    BG.draw(400, 300)
    hand.draw(hand_x, hand_y)
    character.clip_draw(frame*100, 0, 100, 100, char_x, char_y)
    update_canvas()
    frame = (frame + 1) % 8

    if hand_x == char_x and hand_y == char_y:
        setHandLocation()

    setCharDirection()
    moveChar(char_direction)

    delay(0.05)
    get_events()

close_canvas()