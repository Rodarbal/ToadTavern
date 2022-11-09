# modules
import time, sys, pygame
from pygame.locals import *

# initialisation
pygame.init()


# screen/scaling
w = pygame.display.Info()
pygame.display.set_caption("Toad Tavern")
screen = pygame.display.set_mode((w.current_w, int(w.current_h - (w.current_h*0.08))))

# images

# cocktail glass image
cgi = pygame.image.load('assets/image/cg.png')
# cg = pygame.transform.scale(cg, (100, 100))
# screen.blit(cg, (100, 100))

# buttons

class Click():
    def __init__(self, x, y, img, sf):
        # gets image/scale
        self.img = pygame.transform.scale(img, (int(img.get_width() * sf), int(img.get_height() * sf)))
        self.rect = self.img.get_rect()
        # position images
        self.rect.topleft = (x, y)

    def draw(self):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint((mx, my)):
            print("over")
        # positioning
        screen.blit(self.img, (self.rect.x, self.rect.y))


# menu
# menu background
def menu():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (173, 143, 24), pygame.Rect(0, int(w.current_h - (w.current_h * 0.12) - 67), w.current_w, int(w.current_h - (w.current_h * 0.99))))
    pygame.draw.rect(screen, (224, 209, 146), pygame.Rect(0, int(w.current_h - (w.current_h * 0.12) - 60), w.current_w, int(w.current_h - (w.current_h * 0.88))))
    pygame.display.flip()


menu()

# menu clickables (buttons)
cocktail_glass = Click(int(w.current_w/2), int(w.current_h/2), cgi, 0.35)

while 1:
    cocktail_glass.draw()
    # game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

