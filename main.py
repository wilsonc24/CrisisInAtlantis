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
GREEN = (0, 255, 0)
PINK = (255,20,147)
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
OIL = pygame.transform.scale(OIL, (OIL.get_width() / 20, OIL.get_height() / 20))
OCEAN = pygame.image.load('./assets/ocean.jpg')
BOX = pygame.USEREVENT + 1
OIL_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(BOX, 500)
print(type(OIL_EVENT))

INTRO_SONG = MYSTERY
GAME_SONG = SUSPENSE

BUTTON = pygame.image.load('./assets/button.png')
BUTTON = pygame.transform.scale(BUTTON, (400, 50))
LARGER_BUTTON = pygame.transform.scale(BUTTON, (420, 50))
TITLE = pygame.image.load('./assets/title.png')

SPARK = pygame.image.load('./assets/spark.png')
BOSS_SONG = pygame.mixer.Sound('./assets/boss.wav')

BOSS_FRAME_0 = pygame.image.load('./assets/boss2frame0.png')
BOSS_FRAME_1 = pygame.image.load('./assets/boss2frame1.png')
BOSS_FRAME_2 = pygame.image.load('./assets/boss2frame2.png')
BOSS_FRAME_3 = pygame.image.load('./assets/boss2frame3.png')
BOSS_HEIGHT = BOSS_FRAME_0.get_height() / 4
BOSS_WIDTH = BOSS_FRAME_0.get_width() / 4
BOSS_FRAME_0 = pygame.transform.scale(BOSS_FRAME_0, (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_FRAME_1 = pygame.transform.scale(BOSS_FRAME_1, (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_FRAME_2 = pygame.transform.scale(BOSS_FRAME_2, (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_FRAME_3 = pygame.transform.scale(BOSS_FRAME_3, (BOSS_WIDTH, BOSS_HEIGHT))

CAVE2 = pygame.image.load('./assets/cave2.png')
CAVE2 = pygame.transform.scale(CAVE2, (WIDTH, HEIGHT))

DRAGONFIRE = pygame.mixer.Sound('./assets/dragonfire.mp3')

global text
global line_numi
line_num = 0
text_list = []

PLAYER_HIT = pygame.USEREVENT + 5

def print_text():
    global text_len
    # TYPE.play()
    space = 580
    for text in text_list:
        text_len += 1
        WIN.blit(WORD_FONT.render(text[:text_len], True, BLUE), (135, space))
        space += 30
    # TYPE.stop()


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


# TYPEWRITER = pygame.USEREVENT+2
# pygame.time.set_timer(TYPEWRITER, 100)


def print_intro_window():
    WIN.blit(OCEAN, (0, 0))
    WIN.blit(BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 250))
    WIN.blit(BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 320))
    WIN.blit(pygame.transform.scale(BUTTON, (190, 50)), (WIDTH / 2 - BUTTON.get_width() / 2, 450))
    thing = pygame.transform.flip(pygame.transform.scale(BUTTON, (190, 50)), True, False)
    WIN.blit(thing, (510, 450))
    WIN.blit(TITLE, (WIDTH / 2 - TITLE.get_width() / 2, 70))
    subtext = WORD_FONT.render("Singleplayer", True, BLUE)
    WIN.blit(subtext, (WIDTH / 2 - subtext.get_width() / 2, 260))
    WIN.blit(WORD_FONT.render("Multiplayer", True, BLUE), (WIDTH / 2 - subtext.get_width() / 2, 330))
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
        WIN.blit(OCEAN, (0, 0))
        WIN.blit(TITLE, (WIDTH / 2 - TITLE.get_width() / 2, 70))
        # WIN.blit(SPARK, (0,0))

        WIN.blit(BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 250))  # singleplayer
        WIN.blit(BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 320))  # quit
        smaller_button = pygame.transform.scale(BUTTON, (190, 50))
        WIN.blit(smaller_button, (WIDTH / 2 - BUTTON.get_width() / 2, 450))  # left small button
        thing = pygame.transform.flip(pygame.transform.scale(BUTTON, (190, 50)), True, False)
        WIN.blit(thing, (510, 450))  # right small button
        WIN.blit(subtext, (WIDTH / 2 - subtext.get_width() / 2, 260))

        # WIN.blit(WORD_FONT.render("Multiplayer", True, BLUE), (WIDTH/2 - subtext.get_width()/2, 330))
        WIN.blit(subtext2, (WIDTH / 2 - subtext2.get_width() / 2, 330))
        WIN.blit(WORD_FONT.render("Mute", True, BLUE), (575, 460))
        WIN.blit(WORD_FONT.render("Options", True, BLUE), (350, 460))

        play_button = pygame.Rect(WIDTH / 2 - BUTTON.get_width() / 2, 250, 400, 50)
        quit_button = pygame.Rect(WIDTH / 2 - BUTTON.get_width() / 2, 320, 400, 50)
        # pygame.draw.rect(WIN, WHITE, 190, 50)
        if play_button.collidepoint(pos):
            WIN.blit(LARGER_BUTTON, (WIDTH / 2 - LARGER_BUTTON.get_width() / 2, 250))
            WIN.blit(subtext, (WIDTH / 2 - subtext.get_width() / 2, 260))
        elif quit_button.collidepoint(pos):
            WIN.blit(LARGER_BUTTON, (WIDTH / 2 - LARGER_BUTTON.get_width() / 2, 320))
            WIN.blit(subtext2, (WIDTH / 2 - subtext2.get_width() / 2, 330))
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
    WIN.blit(SEA, (0, 0))
    # WIN.blit(ORB, (WIDTH/2 - ORB.get_width()/2, 200))
    # name = WORD_FONT.render("NOVA", True, BLUE)
    # WIN.blit(name, (WIDTH/2 - name.get_width()/2, 175))

    WIN.blit(box, (WIDTH / 2 - box.get_width() / 2, 560))
    print_text()
    WIN.blit(ORB, (50, 500))
    # WIN.blit(OIL, (WIDTH/2 - OIL.get_width(), HEIGHT/2 - OIL.get_height()))
    pygame.display.update()


def oil_dropping(drop):
    WIN.blit(SEA, (0, 0))
    WIN.blit(OIL, (drop.x, drop.y))
    # time.sleep(1)
    pygame.display.update()




BULLET_VEL = 10

def fight():
    player_health = 5
    vel = 5
    max_drops = 5
    oil_drops = []
    BULLET_VEL = 10
    color = ""
    max_bullets = 999999
    frames = [BOSS_FRAME_0, BOSS_FRAME_1, BOSS_FRAME_2, BOSS_FRAME_3]
    GAME_SONG.stop()
    BOSS_SONG.set_volume(0.3)
    BOSS_SONG.play(-1)
    clock = pygame.time.Clock()
    active = True
    i = 0
    piece = pygame.Rect(400, 300, BOSS_WIDTH, BOSS_HEIGHT)
    bullets = []
    while active:
        clock.tick(FPS)
        if i == 4:
            i = 0
        boss = frames[i]
        WIN.blit(SEA, (0, 0))
        WIN.blit(WORD_FONT.render("Ammo : " + str(max_bullets), True, GREEN), (0, 0))
        WIN.blit(WORD_FONT.render("Health : " + str(player_health), True, RED), (0, 30))
        WIN.blit(boss, (piece.x, piece.y))
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = pygame.Rect(piece.x + piece.width // 2 - 2, piece.y - 7, 5, 10)
                color = PINK
                bullets.append(bullet)
                max_bullets -= 1
            if event.type == PLAYER_HIT:
                player_health -= 1
                #BULLET_HIT_SOUND.play()


        if keys_pressed[pygame.K_SPACE]:
            bullet = pygame.Rect(piece.x + piece.width // 2 - 4, piece.y - 5, 10, 3)
            color = PINK
            bullets.append(bullet)
            bullet1 = pygame.Rect(piece.x + piece.width * 0.25, piece.y - 5, 3, 5)
            bullet2 = pygame.Rect(piece.x + piece.width * 0.75, piece.y - 5, 3, 5)
            bullets.append(bullet1)
            bullets.append(bullet2)
            max_bullets -= 3
        if keys_pressed[pygame.K_LSHIFT]:
            vel = 10
        if keys_pressed[pygame.K_LSHIFT] is False:
            vel = 5


        chance = random.randint(0, 20)
        if chance == 5:
        #if keys_pressed[pygame.K_y]:
            x_pos = random.randint(0, 900)
            drop = pygame.Rect(x_pos, 0, 10, 10)
            oil_drops.append(drop)


        #handle_obstacles(oil_drops, piece)
        #handle_bullets(bullets)
        handle_everything(bullets, oil_drops, piece)



        handle_movement(keys_pressed, piece, vel)
        for bullet in bullets:
            pygame.draw.rect(WIN, GREEN, bullet)
        for drop in oil_drops:
            #pygame.draw.rect(WIN, BLACK, drop)
            WIN.blit(OIL, (drop.x, drop.y))



        pygame.display.update()
        i += 1

    BOSS_SONG.stop()
    GAME_SONG.play(-1)
    return


def handle_obstacles(oil_drops, piece):
    for drop in oil_drops:
        drop.y += 5
        if drop.y > HEIGHT:
            oil_drops.remove(drop)
        elif drop.colliderect(piece):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            oil_drops.remove(drop)

def handle_trash(trash_list, piece):
    for drop in trash_list:
        drop.y += 5
        if drop.y > HEIGHT:
            trash_list.remove(drop)
        elif drop.colliderect(piece):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            trash_list.remove(drop)


def handle_bullets(bullets):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        # if red.colliderect(bullet):
        # pygame.event.post(pygame.event.Event(RED_HIT))
        # yellow_bullets.remove(bullet)
        if bullet.x < 0:
            bullets.remove(bullet)

def handle_everything(bullets, oil_drops, piece):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        for drop in oil_drops:
            if drop.colliderect(bullet):
                oil_drops.remove(drop)
                bullets.remove(bullet)

    # if red.colliderect(bullet):
    # pygame.event.post(pygame.event.Event(RED_HIT))
    # yellow_bullets.remove(bullet)
        if bullet.x < 0:
            bullets.remove(bullet)

    for drop in oil_drops:
        drop.y += 5
        if drop.y > HEIGHT:
            oil_drops.remove(drop)
        elif drop.colliderect(piece):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            oil_drops.remove(drop)
        #for bullet in bullets:
           # if bullet.colliderect(drop):
              #  oil_drops.remove(drop)









def handle_movement(keys_pressed, piece, vel):
    if keys_pressed[pygame.K_a] and piece.x - vel > 0:  # LEFT
        piece.x -= vel
    if keys_pressed[pygame.K_d] and piece.x + vel + piece.width < WIDTH:  # RIGHT
        piece.x += vel
    if keys_pressed[pygame.K_w] and piece.y - vel > 0:  # UP
        piece.y -= vel
    if keys_pressed[pygame.K_s] and piece.y + vel + piece.height < HEIGHT:  # DOWN
        piece.y += vel


def main():
    intro()
    global text
    global box
    box = TEXTBOX
    clock = pygame.time.Clock()
    run = True
    update_text()
    GAME_SONG.set_volume(0.3)
    DRAGONFIRE.play(-1)
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
                # drop = pygame.Rect(451, 50, SIZE, SIZE)
                for i in range(10):
                    x_pos = random.randint(0, 900)
                    drop = pygame.Rect(x_pos, 0, SIZE, SIZE)
                    oil_drops.append(drop)
                    # WIN.blit(OIL, (drop.x, drop.y))
                for drop in oil_drops:
                    while drop.y < HEIGHT:
                        # time.sleep(0.01)
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
                if event.key == pygame.K_v:
                    fight()
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
