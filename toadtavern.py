# modules
import time, sys, pygame, random
from pygame.locals import *

# initialisation
pygame.init()

# drinks
drinko = {'bl': ' ', 'ml': ' ', 'tl': ' '}  # drink order: bottom layer (bl), middle layer (ml), top layer (tp)
color = {'00': 'bb', '10': 'mb', '20': 'tb', '01': 'bg', '11': 'mg', '21': 'tg', '02': 'br', '12': 'mr', '22': 'tr',
         '03': 'by', '13': 'my', '23': 'ty'}
colorconverter = {'bb': 'blue', 'mb': 'blue', 'tb': 'blue', 'bg': 'green', 'mg': 'green',  'tg': 'green',
                  'br': 'red', 'mr': 'red', 'tr': 'red', 'by': 'yellow', 'my': 'yellow', 'ty': 'yellow'}

# ordering
order = {'bl': ' ', 'ml': ' ', 'tl': ' '}
def getorders():
    order['bl'] = random.choice(['bb', 'bg', 'br', 'by'])
    order['ml'] = random.choice(['mb', 'mg', 'mr', 'my'])
    order['tl'] = random.choice(['tb', 'tg', 'tr', 'ty'])
    print(order)

getorders()
orderValue = [order['bl'], order['ml'], order['tl']]

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
upgrade = pygame.image.load('assets/image/upgrade.PNG')
serve = pygame.image.load('assets/image/button.png')
back = pygame.image.load('assets/image/back.PNG')

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

            # working drag (implement fully if time allows) (did not allow)
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
upgradeimage = Click(int(w.current_w/2) - (w.current_w * 0.057), int(w.current_h/2) + (w.current_h * 0.3), upgrade, 0.8)
backimage = Click(int(w.current_w/2) - (w.current_w * 0.057), int(w.current_h/2) + (w.current_h * 0.3), back, 0.8)

# menu background
def shelves():
    pygame.draw.rect(screen, (153, 102, 0), pygame.Rect(int(w.current_w / 2) - (w.current_w * 0.46),
                                                        int(w.current_h / 2) + (w.current_h * 0.015), int(w.current_w / 2) - (w.current_w * 0.15), 10))
    pygame.draw.rect(screen, (153, 102, 0), pygame.Rect(int(w.current_w / 2) + (w.current_w * 0.11),
                                                        int(w.current_h / 2) + (w.current_h * 0.015), int(w.current_w / 2) - (w.current_w * 0.15), 10))
def menu():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (173, 143, 24), pygame.Rect(0, int(w.current_h - (w.current_h * 0.12) - 67), w.current_w, int(w.current_h - (w.current_h * 0.99))))
    pygame.draw.rect(screen, (224, 209, 146), pygame.Rect(0, int(w.current_h - (w.current_h * 0.12) - 60), w.current_w, int(w.current_h - (w.current_h * 0.88))))
    #pygame.draw.rect(screen, (153, 102, 0), pygame.Rect(int(w.current_w / 2) - (w.current_w * 0.46),
    #                                                    int(w.current_h / 2) + (w.current_h * 0.015), int(w.current_w / 2) - (w.current_w * 0.15), 10))
    #pygame.draw.rect(screen, (153, 102, 0), pygame.Rect(int(w.current_w / 2) + (w.current_w * 0.11),
    #                                                    int(w.current_h / 2) + (w.current_h * 0.015), int(w.current_w / 2) - (w.current_w * 0.15), 10))
    pygame.display.flip()


menu()
shelves()

# money and order display
moneyValue = 0
moneyFont = pygame.font.SysFont("monospace", 30)
textX = 10
textY = 10

# orderValue = [order['bl'], order['ml'], order['tl']]
orderFont = pygame.font.SysFont("monospace", 30)
orderX = 300
orderY = 10

def displayOrder(x, y):
    orderText = orderFont.render("{} ({}, {} and {})".format(random.choice(['Parsley Mojito', 'Pond Water', 'Sparkling Snake Venom', 'Croak & Vodka', ' Hops On The Beach']), colorconverter[orderValue[0]], colorconverter[orderValue[1]], colorconverter[orderValue[2]]), True, (0, 0, 0))
    time.sleep(1)
    screen.blit(orderText, (x, y))
    pygame.display.flip()

def displayMoney(x, y):
    moneyText = moneyFont.render("Money: ${}".format(str(moneyValue)), True, (0, 0, 0))
    time.sleep(1)
    menu()
    shelves()
    displayOrder(orderX, orderY)
    screen.blit(moneyText, (x, y))
    pygame.display.flip()


# menu clickables (buttons)
cocktail_glass = Click(int(w.current_w/2) - (w.current_w * 0.10), int(w.current_h/2) - (w.current_h * 0.17), cgi, 0.6)
blue_drink = Click(int(w.current_w/2) - (w.current_w * 0.55), int(w.current_h/2) - (w.current_h * 0.30), bdi, 0.6)
green_drink = Click(int(w.current_w/2) - (w.current_w * 0.30), int(w.current_h/2) - (w.current_h * 0.30), gdi, 0.6)
red_drink = Click(int(w.current_w/2) + (w.current_w * 0.03), int(w.current_h/2) - (w.current_h * 0.30), rdi, 0.6)
yellow_drink = Click(int(w.current_w/2) + (w.current_w * 0.27), int(w.current_h/2) - (w.current_h * 0.30), ydi, 0.6)
serve_button = Click(int(w.current_w / 2) - (w.current_w * 0.073), int(w.current_h / 2) - (w.current_h * 0.43), serve, 0.3)
back_button = Click(int(w.current_w/2) - (w.current_w * 0.057), int(w.current_h/2) + (w.current_h * 0.3), back, 0.8)
serveActive = False
upgrademenu = False
mainmenu = True


displayMoney(textX, textY)


# game loop
while 1:
    while upgrademenu:
        if back_button.draw():
            mainmenu = True
            upgrademenu = False
            menu()
            shelves()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("x")
                    menu()
                    shelves()
        pygame.display.update()
    while mainmenu:
        if cocktail_glass.draw():
            pass
        if blue_drink.draw():
            if drinko['bl'] == ' ':
                drinko['bl'] = '00'
                #bbi = Click(int(w.current_w/2) - (w.current_w * 0.10), int(w.current_h/2) - (w.current_h * 0.17), bb, 0.6)
                #bbi.draw()
            elif drinko['ml'] == ' ':
                drinko['ml'] = '10'
            elif drinko['tl'] == ' ':
                drinko['tl'] = '20'
                serveActive = True
            else:
                print("full")
                print(drinko)
        if green_drink.draw():
            if drinko['bl'] == ' ':
                drinko['bl'] = '01'
                #bgi = Click(int(w.current_w/2) - (w.current_w * 0.10), int(w.current_h/2) - (w.current_h * 0.17), bg, 0.6) unneccacary
                #bgi.draw()
            elif drinko['ml'] == ' ':
                drinko['ml'] = '11'
            elif drinko['tl'] == ' ':
                drinko['tl'] = '21'
                serveActive = True
            else:
                print("full")
                print(drinko)
        if red_drink.draw():
            if drinko['bl'] == ' ':
                drinko['bl'] = '02'
                #bri = Click(int(w.current_w/2) - (w.current_w * 0.10), int(w.current_h/2) - (w.current_h * 0.17), br, 0.6)
            elif drinko['ml'] == ' ':
                drinko['ml'] = '12'
            elif drinko['tl'] == ' ':
                drinko['tl'] = '22'
                serveActive = True
            else:
                print("full")
                print(drinko)
        if yellow_drink.draw():
            if drinko['bl'] == ' ':
                drinko['bl'] = '03'
                #byi = Click(int(w.current_w / 2) - (w.current_w * 0.10), int(w.current_h / 2) - (w.current_h * 0.17), by,
                #            0.6)
                #byi.draw()
            elif drinko['ml'] == ' ':
                drinko['ml'] = '13'
            elif drinko['tl'] == ' ':
                drinko['tl'] = '23'
                serveActive = True
            else:
                print("full")
                print(drinko)
        if upgradeimage.draw():
            mainmenu = False
            upgrademenu = True
            menu()
        if serveActive:
            if serve_button.draw():
                if order['tl'] == color[drinko['tl']] and order['ml'] == color[drinko['ml']] and order['bl'] == color[drinko['bl']]:
                    moneyValue += 10
                    getorders()
                    orderValue = [order['bl'], order['ml'], order['tl']]
                    displayOrder(orderX, orderY)
                    displayMoney(textX, textY)
                    drinko = {'bl': ' ', 'ml': ' ', 'tl': ' '}
                    serveActive = False

                else:
                    moneyValue -= 10
                    getorders()
                    orderValue = [order['bl'], order['ml'], order['tl']]
                    displayOrder(orderX, orderY)
                    displayMoney(textX, textY)
                    drinko = {'bl': ' ', 'ml': ' ', 'tl': ' '}
                    serveActive = False
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
            if color[drinko['ml']] == 'mb':
                ml = mb
            elif color[drinko['ml']] == 'mg':
                ml = mg
            elif color[drinko['ml']] == 'mr':
                ml = mr
            elif color[drinko['ml']] == 'my':
                ml = my
            screen.blit(ml, (int(w.current_w/2) - (w.current_w * 0.17), int(w.current_h/2) - (w.current_h * 0.29)))

        if drinko['tl'] != ' ':
            if drinko['tl'] != ' ':
                if color[drinko['tl']] == 'tb':
                    tl = tb
                elif color[drinko['tl']] == 'tg':
                    tl = tg
                elif color[drinko['tl']] == 'tr':
                    tl = tr
                elif color[drinko['tl']] == 'ty':
                    tl = ty
                screen.blit(tl, (int(w.current_w / 2) - (w.current_w * 0.17), int(w.current_h / 2) - (w.current_h * 0.29)))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("w")
                    menu()
        pygame.display.update()

