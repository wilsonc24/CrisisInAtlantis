import pygame
import time
import sys
import random
from pygame import mixer

pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = int(WIDTH * .7)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CRISIS IN ATLANTIS")
programIcon = pygame.image.load('./assets/orb.png')
pygame.display.set_icon(programIcon)
WORD_FONT = pygame.font.SysFont('garamond', 30)
WIN_FONT = pygame.font.SysFont('garamond', 70)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SAND = (194, 178, 128)
FPS = 60
SIZE = 75


SUSPENSE = pygame.mixer.Sound('./assets/suspense.ogg')
BEEP = pygame.mixer.Sound('./assets/beep.wav')
TYPE = pygame.mixer.Sound('./assets/type.wav')

SEA = pygame.image.load('./assets/sea.jpg')
SEA = pygame.transform.scale(SEA, (WIDTH, HEIGHT))
TEXTBOX = pygame.image.load('./assets/textbox.png')
TEXTBOX2 = pygame.image.load('./assets/textbox2.png')
TEXTBOX = pygame.transform.scale(TEXTBOX, (800, 130))
TEXTBOX2 = pygame.transform.scale(TEXTBOX2, (800, 130))
ORB = pygame.image.load('./assets/orb.png')
ORB = pygame.transform.scale(ORB, (100, 100))
OIL = pygame.image.load('./assets/oil.png')
OIL = pygame.transform.scale(OIL, (OIL.get_width()/10, OIL.get_height()/10))

BOX = pygame.USEREVENT + 1
OIL_EVENT = pygame.USEREVENT +2
pygame.time.set_timer(BOX, 500)
print(type(OIL_EVENT))

global text
global line_numi
line_num = 0
text_list = []

def print_text():
    global text_len
    TYPE.play()
    space = 580
    for text in text_list:
        text_len += 1
        WIN.blit(WORD_FONT.render(text[:text_len], True, WHITE), (135, space))
        space += 30
    TYPE.stop()

def update_text():
    global line_num
    global text_list
    global text_len
    text_len = 0
    text_list.clear()
    file = open('./assets/script.txt')
    content = file.readlines()
    try:
        sen = ""
        t = content[line_num].replace("\n", "")
        texts = t.split(" ")
        n = 1
        for i in texts:
            sen += i + " "
            if n % 10 == 0:
                text_list.append(sen)
                sen = ""
                n = 1
            n += 1
        text_list.append(sen)
        line_num += 1
    except IndexError:
        pass



global text_len
text_len = 0
#TYPEWRITER = pygame.USEREVENT+2
#pygame.time.set_timer(TYPEWRITER, 100)



def draw_window():
    global box
    global text
    WIN.blit(SEA, (0,0))

    #WIN.blit(ORB, (WIDTH/2 - ORB.get_width()/2, 200))
    #name = WORD_FONT.render("NOVA", True, BLUE)
    #WIN.blit(name, (WIDTH/2 - name.get_width()/2, 175))


    WIN.blit(box,(WIDTH/2 - box.get_width()/2, 560))
    print_text()
    WIN.blit(ORB, (50,500))
    #WIN.blit(OIL, (WIDTH/2 - OIL.get_width(), HEIGHT/2 - OIL.get_height()))
    pygame.display.update()

def oil_dropping(drop):
    WIN.blit(SEA, (0,0))
    WIN.blit(OIL, (drop.x, drop.y))
    #time.sleep(1)
    pygame.display.update()





def main():
    global text
    global box
    box = TEXTBOX
    clock = pygame.time.Clock()
    run = True

    update_text()


    SUSPENSE.set_volume(0.4)
    SUSPENSE.play(-1)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == BOX:
                if box == TEXTBOX:
                    box = TEXTBOX2
                else:
                    box = TEXTBOX
            if event.type == OIL_EVENT:
                max_drops = 5
                oil_drops = []
                #drop = pygame.Rect(451, 50, SIZE, SIZE)
                for i in range(10):
                    x_pos = random.randint(0, 900)
                    drop = pygame.Rect(x_pos, 0, SIZE, SIZE)
                    oil_drops.append(drop)
                    #WIN.blit(OIL, (drop.x, drop.y))
                for drop in oil_drops:
                    while drop.y < HEIGHT:
                        #time.sleep(0.01)
                        drop.y += 1
                        oil_dropping(drop)


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONUP):
                    #pos = pygame.mouse.get_pos()
                    update_text()

                if event.key == pygame.K_b:
                    print(type(OIL_EVENT))
                    pygame.event.post(pygame.event.Event(OIL_EVENT))
        draw_window()
    pygame.quit()
    sys.exit()

'''
def oil_event():
    max_drops = 5
    oil_drops = []
    #drop = pygame.Rect(451, 50, SIZE, SIZE)
    for event in pygame.event.get():
    for i in range(10):
        drop = pygame.Rect(451, 50, SIZE, SIZE)
        oil_drops.append(drop)
        WIN.blit(OIL, (drop.x, drop.y))
'''

if __name__ == "__main__":
    main()

