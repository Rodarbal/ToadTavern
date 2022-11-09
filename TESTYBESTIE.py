import time
from pygame import *
import pygame
from sys import *

FPS = 30
pygame.init()

# screen scaling
w = pygame.display.Info()
pygame.display.set_caption("Toad Tavern")
screen = pygame.display.set_mode((w.current_w, int(w.current_h - (w.current_h*0.08))))
# screen = pygame.display.set_mode((1280, 697))


# images
#bg = pygame.image.load("assets/image/bg2.jpeg")
cg = pygame.image.load('assets/image/cg.png')
cg = pygame.transform.scale(cg, (100, 100))
cog = cg.get_rect()



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


menu()
screen.blit(cg, (200, 200))
cog.center = (w.current_w, w.current_h)
display.flip()
# draggable drinks


mx, my = pygame.mouse.get_pos()
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        elif event.type == MOUSEMOTION:
            x, y = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            #if event.button == 1:
            if cog.collidepoint(event.pos):
                print("hi")
        #elif event.type == MOUSEBUTTONUP:
         #   if event.button == 1:


    #cog.center = (mx, my)
    #screen.blit(cg, (mx, my))
    #menu()
    display.flip()
    clock = time.Clock().tick(FPS)
