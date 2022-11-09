import time
from pygame import *
import pygame
from sys import *

#FPS = 30
pygame.init()

# images
#bg = pygame.image.load("assets/image/bg2.jpeg")
cg = pygame.image.load('assets/image/cg.png')
cg = pygame.transform.scale(cg, (100, 100))


# screen scaling
w = pygame.display.Info()
pygame.display.set_caption("Toad Tavern")
screen = pygame.display.set_mode((w.current_w, int(w.current_h - (w.current_h*0.08))))
# screen = pygame.display.set_mode((1280, 697))
screen.blit(cg, (100, 100))

# menu
def menu():
    screen.fill((255, 255, 255))
    # screen.blit(bg, (0, 0))
    # screen.blit(cg, (0, 0))
    # pygame.display.update()
    pygame.draw.rect(screen, (173, 143, 24), pygame.Rect(0, int(w.current_h - (w.current_h*0.12) - 67), w.current_w,
                                                          int(w.current_h - (w.current_h * 0.99))))
    pygame.display.flip()
    pygame.draw.rect(screen, (224, 209, 146),
    pygame.Rect(0, int(w.current_h - (w.current_h*0.12) - 60), w.current_w, int(w.current_h - (w.current_h*0.88))))
    #pygame.draw.rect(screen, (173, 143, 24), pygame.Rect(0, int(w.current_h - w.current_h * 0.12 - 70), w.current_w, int(w.current_h - (w.current_h*0.88))))
    #pygame.display.flip()


# draggable drinks
rectangle_draging = False
#clock = time.Clock()


while 1:
    # mouse pos
    mx, my = pygame.mouse.get_pos()

    # game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        elif event.type == MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
    #screen.fill((255, 255, 255))
    #draw.rect(screen, (255, 0 ,0), rectangle)
    #center of glass
    cog = cg.get_rect()
    cog.center = (mx, my)
    screen.blit(cg, (cog.x, cog.y))
    display.flip()
    time.wait(10)
    menu()
    display.flip()
