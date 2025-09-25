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
    if direction == 'up':
        global y, frame
        y = min(TUK_HEIGHT, y + 10)
        frame = (frame + 1) % 8
    elif direction == 'down':
        global y, frame
        y = max(0, y - 10)
        frame = (frame + 1) % 8
    elif direction == 'left':
        global x, frame
        x = max(0, x - 10)
        frame = (frame + 1) % 8
    elif direction == 'right':
        global x, frame
        x = min(TUK_WIDTH, x + 10)
        frame = (frame + 1) % 8
    elif direction == 'idle':
        global frame
        frame = 0
    pass

def render():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if direction == 'idle':
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    pass

while True:
    handle_events()
    update()
    render()
    pass





close_canvas()