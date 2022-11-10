import pygame
from pygame import *
import time
import sys

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


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        #self.rect.topleft = (x, y)
        #self.clicked = False

    def draw(self, surface):
        #action = False
        # get mouse position
        #pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        #if self.rect.collidepoint(pos):
            # print("hover")
            #pass
        surface.blit(self.image, (400, 250))

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('assets/image/cg.png')


#create button instances
start_button = Button(100, 200, start_img, 0.1)


#game loop
run = True
while run:
    screen.fill((255, 255, 255))
    pos = pygame.mouse.get_pos()
    mx,my = pygame.mouse.get_pos()

    if start_button.draw(screen):
        print('START')



    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if start_button.rect.collidepoint(pos):
                start_button.rect.center = (mx, my)
                screen.blit(start_button.image, (start_button.rect.x, start_button.rect.y))
                pygame.display.flip()
                time.sleep(0.01)
                menu()
                display.flip()
        elif event.type == MOUSEMOTION:
            x, y = event.pos
            #print(x + " " + y)
    pygame.display.update()

pygame.quit()
