# modules
import time, sys, pygame
from pygame.locals import *

# initialisation
pygame.init()

# stats
drinko = {'bl': ' ', 'ml': ' ', 'tl': ' '}  # drink order: bottom layer (bl), middle layer (ml), top layer (tp)
color = {'00': 'bb', '10': 'mb', '20': 'tb', '01': 'bg', '11': 'mg', '21': 'tg', '02': 'br', '12': 'mr', '22': 'tr',
         '03': 'by', '13': 'my', '23': 'ty'}
money = 0

# screen/scaling
w = pygame.display.Info()
pygame.display.set_caption("Toad Tavern")
screen = pygame.display.set_mode((w.current_w, int(w.current_h - (w.current_h*0.08))))

# images (shortened variable names as they are used commonly)
cgi = pygame.image.load('assets/image/cg.png')  # cgi = cocktail glass image
bdi = pygame.image.load('assets/image/0.png')  # bdi = blue drink image
gdi = pygame.image.load('assets/image/1.PNG')  # gdi = blue drink image
rdi = pygame.image.load('assets/image/2.png')  # rdi = blue drink image
ydi = pygame.image.load('assets/image/3.png')  # ydi = blue drink image

# poured drink images
bb = pygame.image.load('assets/image/00.png')  # bb = bottom blue
mb = pygame.image.load('assets/image/10.png')  # mb = middle blue
tb = pygame.image.load('assets/image/20.png')  # tb = top blue
bg = pygame.image.load('assets/image/01.png')  # bg = bottom green
mg = pygame.image.load('assets/image/11.png')  # mg = middle green
tg = pygame.image.load('assets/image/21.png')  # tg = top green
br = pygame.image.load('assets/image/02.png')  # br = bottom red
mr = pygame.image.load('assets/image/12.png')  # mr = middle red
tr = pygame.image.load('assets/image/22.png')  # tr = top red
by = pygame.image.load('assets/image/03.png')  # by = bottom yellow
my = pygame.image.load('assets/image/13.png')  # my = middle yellow
ty = pygame.image.load('assets/image/23.png')  # ty = top yellow
# buttons

class Click():
    def __init__(self, x, y, img, sf):
        # gets image/scale
        self.img = pygame.transform.scale(img, (int(img.get_width() * sf), int(img.get_height() * sf)))
        self.rect = self.img.get_rect()
        # position images
        self.rect.topleft = (x, y)
        self.drag = False

    def draw(self):
        do = False
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0] == 1 and self.drag == False:
                self.drag = True
                do = True

            # working drag (implement fully if time allows)
            #if self.drag == True:
            #    mx, my = pygame.mouse.get_pos()
            #    self.rect.center = (mx, my)
            #    #screen.blit(self.img, (mx, my))
            #    pygame.display.flip()
            if pygame.mouse.get_pressed()[0] == 0:
                self.drag = False
        # positioning
        screen.blit(self.img, (self.rect.x, self.rect.y))

        return do

# menu
# menu background
def menu():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (173, 143, 24), pygame.Rect(0, int(w.current_h - (w.current_h * 0.12) - 67), w.current_w, int(w.current_h - (w.current_h * 0.99))))
    pygame.draw.rect(screen, (224, 209, 146), pygame.Rect(0, int(w.current_h - (w.current_h * 0.12) - 60), w.current_w, int(w.current_h - (w.current_h * 0.88))))
    pygame.draw.rect(screen, (153, 102, 0), pygame.Rect(int(w.current_w / 2) - (w.current_w * 0.46),
                                                        int(w.current_h / 2) + (w.current_h * 0.015), int(w.current_w / 2) - (w.current_w * 0.15), 10))
    pygame.draw.rect(screen, (153, 102, 0), pygame.Rect(int(w.current_w / 2) + (w.current_w * 0.11),
                                                        int(w.current_h / 2) + (w.current_h * 0.015), int(w.current_w / 2) - (w.current_w * 0.15), 10))
    pygame.display.flip()


menu()

# menu clickables (buttons)
cocktail_glass = Click(int(w.current_w/2) - (w.current_w * 0.10), int(w.current_h/2) - (w.current_h * 0.17), cgi, 0.6)
blue_drink = Click(int(w.current_w/2) - (w.current_w * 0.55), int(w.current_h/2) - (w.current_h * 0.30), bdi, 0.6)
green_drink = Click(int(w.current_w/2) - (w.current_w * 0.30), int(w.current_h/2) - (w.current_h * 0.30), gdi, 0.6)
red_drink = Click(int(w.current_w/2) + (w.current_w * 0.03), int(w.current_h/2) - (w.current_h * 0.30), rdi, 0.6)
yellow_drink = Click(int(w.current_w/2) + (w.current_w * 0.27), int(w.current_h/2) - (w.current_h * 0.30), ydi, 0.6)

# game loop
while 1:
    if cocktail_glass.draw():
        pass
    if blue_drink.draw():
        if drinko['bl'] == ' ':
            drinko['bl'] = '00'
            bbi = Click(int(w.current_w/2) - (w.current_w * 0.10), int(w.current_h/2) - (w.current_h * 0.17), bb, 0.6)
            bbi.draw()
        elif drinko['ml'] == ' ':
            drinko['ml'] = '10'
        elif drinko['tl'] == ' ':
            drinko['tl'] = '20'
        else:
            print("full")
            print(drinko)
    if green_drink.draw():
        print("green")
    if red_drink.draw():
        print("red")
    if yellow_drink.draw():
        print("yellow")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if drinko['bl'] != ' ':
        if color[drinko['bl']] == 'bb':
            bl = bb
        elif color[drinko['bl']] == 'bg':
            bl = bg
        elif color[drinko['bl']] == 'br':
            bl = br
        elif color[drinko['bl']] == 'by':
            bl = by

        screen.blit(bl, (int(w.current_w/2) - (w.current_w * 0.17), int(w.current_h/2) - (w.current_h * 0.29)))
    if drinko['ml'] != ' ':
        pass
    if drinko['tl'] != ' ':
        pass
    pygame.display.flip()

