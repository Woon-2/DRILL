from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):    # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code


open_canvas()
grass = Grass()

team = [Boy() for i in range(11)]


running = True

# game main loop code


while running:
    handle_events()

    # game logic
    for boy in team:
        boy.update()

    # game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    delay(0.05)

    update_canvas()

# finalization code
