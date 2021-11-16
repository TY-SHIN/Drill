import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30cm


TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    image = None;

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image("bird100x100x14.png")
        self.x, self.y = random.randint(0, 1600-1), random.randint(0, 600-1)
        self.dir = random.randrange(-1,2,2)
        self.velocity = random.randint(5,10)   # Km / Hour
        self.frame = 0
        self.size = random.randint(50,100)
        time_per_action = 0.1 * self.velocity
        self.action_per_timer = 1.0 / time_per_action


    def draw(self):
        self.image.clip_draw(100*int(self.frame), 0, 100, 100, self.x, self.y,self.size,self.size)

    def update(self):
        fly_speed_MPM = (self.velocity * 1000.0 / 60.0)  # KM/1hour -> 1000M/60min
        fly_speed_MPS = (fly_speed_MPM / 60.0)  # M/min -> M/60sec
        fly_speed_PPS = (fly_speed_MPS * PIXEL_PER_METER)  # M/sec -> Pixel/sec

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * (self.velocity/10.0)) % 14

        self.x += self.dir * self.velocity * fly_speed_PPS * game_framework.frame_time
        half_size = self.size/2
        self.x = clamp( half_size, self.x, 1600 -  half_size)
        if self.x == half_size or self.x== 1600- half_size : self.dir = -self.dir