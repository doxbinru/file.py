from pygame import *

mw = display.set_mode((800,600))
display.set_caption('dogonalki')

bg = transform.scale(image.load('background.png'), (800,600))
sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
x1, y1 = 100, 400

sprite2 = transform.scale(image.load('sprite2.png'),(100,100))
x2, y2 = 400, 400

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    mw.blit(bg, (0,0))
    mw.blit(sprite1, (x1,y1))
    mw.blit(sprite2, (x2,y2))
    keys = key.get_pressed()
    if keys[K_RIGHT] and x1 < 700:
        x1 += 3
    if keys[K_LEFT] and x1 > 0:
        x1 -= 3
    if keys[K_DOWN] and y1 < 500:
        y1 += 3
    if keys[K_UP] and y1 > 0:
        y1 -= 3

    if x1 > x2:
        x2 += 1
    if x1 < x2:
        x2 -= 1
    if y1 > y2:
        y2 += 1
    if y1 < y2:
        y2 -= 1

    display.update()
    time.Clock().tick(100)