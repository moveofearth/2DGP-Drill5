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
                running = True
            elif event.key == SDLK_DOWN:
                direction = 'down'
                running = True
            elif event.key == SDLK_LEFT:
                direction = 'left'
                running = True
            elif event.key == SDLK_RIGHT:
                direction = 'right'
                running = True
        elif event.type == SDL_KEYUP:
            running = False



x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
direction = 'left'
running = False

def update():
    global x, y, frame, direction

    if running == True:
        if direction == 'up':
            y = min(TUK_HEIGHT, y + 10)
            frame = (frame + 1) % 8
        elif direction == 'down':
            y = max(0, y - 10)
            frame = (frame + 1) % 8
        elif direction == 'left':
            x = max(0, x - 10)
            frame = (frame + 1) % 8
        elif direction == 'right':
            x = min(TUK_WIDTH, x + 10)
            frame = (frame + 1) % 8
    else:
        frame = (frame + 1) % 8

    pass

def render():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if running == True:
        if direction == 'up' or direction == 'right':
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif direction == 'down' or direction == 'left':
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        if direction == 'up' or direction == 'right':
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
        elif direction == 'down' or direction == 'left':
            character.clip_draw(frame * 100, 200, 100, 100, x, y)
    update_canvas()
    pass


while True:
    handle_events()
    update()
    render()
    delay(0.05)
    pass


close_canvas()