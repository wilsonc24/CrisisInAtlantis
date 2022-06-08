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
TITLE_FONT = pygame.font.SysFont('garamond', 90)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SAND = (194, 178, 128)
FPS = 60
SIZE = 75


SUSPENSE = pygame.mixer.Sound('./assets/suspense.ogg')
MYSTERY = pygame.mixer.Sound('./assets/mystery.mp3')
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
OCEAN = pygame.image.load('./assets/ocean.jpg')
BOX = pygame.USEREVENT + 1
OIL_EVENT = pygame.USEREVENT +2
pygame.time.set_timer(BOX, 500)
print(type(OIL_EVENT))

INTRO_SONG = MYSTERY
GAME_SONG = SUSPENSE

BUTTON = pygame.image.load('./assets/button.png')
BUTTON = pygame.transform.scale(BUTTON, (400, 50))
LARGER_BUTTON = pygame.transform.scale(BUTTON, (420, 50))
TITLE = pygame.image.load('./assets/title.png')

SPARK = pygame.image.load('./assets/spark.png')

global text
global line_numi
line_num = 0
text_list = []

def print_text():
    global text_len
    #TYPE.play()
    space = 580
    for text in text_list:
        text_len += 1
        WIN.blit(WORD_FONT.render(text[:text_len], True, BLUE), (135, space))
        space += 30
    #TYPE.stop()

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


def print_intro_window():

    WIN.blit(OCEAN, (0,0))
    WIN.blit(BUTTON,  (WIDTH/2 - BUTTON.get_width()/2, 250))
    WIN.blit(BUTTON,  (WIDTH/2 - BUTTON.get_width()/2, 320))
    WIN.blit(pygame.transform.scale(BUTTON, (190, 50)),  (WIDTH/2 - BUTTON.get_width()/2, 450))
    thing = pygame.transform.flip(pygame.transform.scale(BUTTON, (190, 50)), True, False)
    WIN.blit(thing,  (510, 450))
    WIN.blit(TITLE, (WIDTH/2 - TITLE.get_width()/2, 70))
    subtext = WORD_FONT.render("Singleplayer", True, BLUE)
    WIN.blit(subtext, (WIDTH/2 - subtext.get_width()/2, 260))
    WIN.blit(WORD_FONT.render("Multiplayer", True, BLUE), (WIDTH/2 - subtext.get_width()/2, 330))
    WIN.blit(WORD_FONT.render("Quit", True, BLUE), (575, 460))
    WIN.blit(WORD_FONT.render("Options", True, BLUE), (350, 460))

def intro():
    active = True
    INTRO_SONG.set_volume(0.7)
    INTRO_SONG.play(-1)
    subtext = WORD_FONT.render("Singleplayer", True, BLUE)
    subtext2 = WORD_FONT.render("Exit", True, BLUE)
    while active:
        pos = pygame.mouse.get_pos()
        WIN.blit(OCEAN, (0,0))
        WIN.blit(TITLE, (WIDTH/2 - TITLE.get_width()/2, 70))
        #WIN.blit(SPARK, (0,0))


        WIN.blit(BUTTON,  (WIDTH/2 - BUTTON.get_width()/2, 250)) #singleplayer
        WIN.blit(BUTTON,  (WIDTH/2 - BUTTON.get_width()/2, 320)) #quit
        smaller_button = pygame.transform.scale(BUTTON, (190, 50))
        WIN.blit(smaller_button,  (WIDTH/2 - BUTTON.get_width()/2, 450)) #left small button
        thing = pygame.transform.flip(pygame.transform.scale(BUTTON, (190, 50)), True, False)
        WIN.blit(thing,  (510, 450)) #right small button
        WIN.blit(subtext, (WIDTH/2 - subtext.get_width()/2, 260))

        #WIN.blit(WORD_FONT.render("Multiplayer", True, BLUE), (WIDTH/2 - subtext.get_width()/2, 330))
        WIN.blit(subtext2, (WIDTH/2 - subtext2.get_width()/2, 330))
        WIN.blit(WORD_FONT.render("Mute", True, BLUE), (575, 460))
        WIN.blit(WORD_FONT.render("Options", True, BLUE), (350, 460))

        play_button = pygame.Rect(WIDTH/2 - BUTTON.get_width()/2, 250, 400, 50)
        quit_button = pygame.Rect(WIDTH/2 - BUTTON.get_width()/2, 320, 400, 50)
        #pygame.draw.rect(WIN, WHITE, 190, 50)
        if play_button.collidepoint(pos):
            WIN.blit(LARGER_BUTTON,  (WIDTH/2 - LARGER_BUTTON.get_width()/2, 250))
            WIN.blit(subtext, (WIDTH/2 - subtext.get_width()/2, 260))
        elif quit_button.collidepoint(pos):
            WIN.blit(LARGER_BUTTON,  (WIDTH/2 - LARGER_BUTTON.get_width()/2, 320))
            WIN.blit(subtext2, (WIDTH/2 - subtext2.get_width()/2, 330))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if play_button.collidepoint(pos):
                        active = False
                        INTRO_SONG.stop()
                        return
                    elif quit_button.collidepoint(pos):
                        pygame.quit()
                        sys.exit()
        WIN.blit(SPARK, (0, 0))
        pygame.display.update()




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
    intro()
    global text
    global box
    box = TEXTBOX
    clock = pygame.time.Clock()
    run = True
    update_text()
    GAME_SONG.set_volume(0.3)
    GAME_SONG.play(-1)
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
                if (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                    update_text()
                if event.key == pygame.K_b:
                    print(type(OIL_EVENT))
                    pygame.event.post(pygame.event.Event(OIL_EVENT))
            elif (event.type == pygame.MOUSEBUTTONUP):
                if event.button == 1:
                    update_text()
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

