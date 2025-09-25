from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running
    global x, y
    global direction

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                direction = 'up'
            elif event.key == SDLK_DOWN:
                direction = 'down'
            elif event.key == SDLK_LEFT:
                direction = 'left'
            elif event.key == SDLK_RIGHT:
                direction = 'right'
        elif event.type == SDL_KEYUP:
            direction = 'idle'



x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

def update():
    pass

def render():
    pass

while True:
    handle_events()
    update()
    render()
    pass





close_canvas()