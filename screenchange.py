import time
from pygame import *
from sys import *
from pygame.locals import *
init()
inf = display.Info()
screen = display.set_mode((inf.current_w, inf.current_h-(int(inf.current_h * 0.08))))
while 1:
    for x in event.get():
        if x.type == QUIT:
            exit()
    screen.fill((0, 0, 0))
    display.update()
    time.wait(100)
    screen.fill((255, 255, 255))
    display.update()
    time.wait(100)
