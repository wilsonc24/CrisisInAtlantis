import pygame
import time
import sys
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = int(WIDTH * .7)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CRISIS IN ATLANTIS")
programIcon = pygame.image.load('./assets/orb2.png')
pygame.display.set_icon(programIcon)
WORD_FONT = pygame.font.SysFont('garamond', 30)
NAME_FONT = pygame.font.SysFont('garamond', 40)
SCORE_FONT = pygame.font.SysFont('Verdana', 40)
FINAL_SCORE_FONT = pygame.font.SysFont('Verdana', 60)
WIN_FONT = pygame.font.SysFont('garamond', 70)
TITLE_FONT = pygame.font.SysFont('garamond', 90)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SAND = (194, 178, 128)
GREEN = (0, 255, 0)
PINK = (255, 20, 147)
MARINE = (50, 100, 83)
PURPLE = (102, 51, 153)
FPS = 60
SIZE = 75
BULLET_VEL = 15

# ASSETS
SUSPENSE = pygame.mixer.Sound('./assets/suspense.ogg')
MYSTERY = pygame.mixer.Sound('./assets/mystery.mp3')
SEA = pygame.image.load('./assets/sea.jpg')
SEA = pygame.transform.scale(SEA, (WIDTH, HEIGHT))
TEXTBOX = pygame.image.load('./assets/textbox.png')
TEXTBOX2 = pygame.image.load('./assets/textbox2.png')
TEXTBOX = pygame.transform.scale(TEXTBOX, (800, 130))
TEXTBOX2 = pygame.transform.scale(TEXTBOX2, (800, 130))
ORB = pygame.image.load('./assets/orb.png')
ORB = pygame.transform.scale(ORB, (100, 100))
UNPAUSED_BLUE = pygame.image.load('./assets/UNPAUSE_blue.png')
UNPAUSED_WHITE = pygame.image.load('./assets/UNPAUSE_white.png')
SCORE_IMG = pygame.image.load('./assets/SCORE.png')
HIGHSCORE_IMG = pygame.image.load('./assets/HIGHSCORE.png')
OIL = pygame.image.load('./assets/oil.png')
OIL = pygame.transform.scale(OIL, (OIL.get_width() / 15, OIL.get_height() / 15))
OCEAN = pygame.image.load('./assets/ocean.jpg')
INTRO_SONG = MYSTERY
GAME_SONG = SUSPENSE
BUTTON = pygame.image.load('./assets/button.png')
BUTTON = pygame.transform.scale(BUTTON, (400, 50))
WHITE_BUTTON = pygame.image.load('./assets/whitebutton.png')
WHITE_BUTTON = pygame.transform.scale(WHITE_BUTTON, (400, 50))
SMALLER_BUTTON = pygame.transform.scale(BUTTON, (190, 50))
SMALLER_WHITE_BUTTON = pygame.transform.scale(WHITE_BUTTON, (190, 50))
GAME_OVER = pygame.image.load('./assets/GAME-OVER.png')
REPLAY_ICON = pygame.image.load('./assets/rep.png')
HOME_ICON = pygame.image.load('./assets/home.png')
PAUSE_BLUE = pygame.image.load('./assets/pause.png')
PAUSE_YELLOW = pygame.image.load('./assets/pause2.png')
CLICK_SOUND = pygame.mixer.Sound('./assets/button_click_sound.wav')
WHITE_REPLAY_ICON = pygame.image.load('./assets/rep_white.png')
WHITE_HOME_ICON = pygame.image.load('./assets/home_white.png')
LARGER_BUTTON = pygame.transform.scale(WHITE_BUTTON, (420, 50))
TITLE = pygame.image.load('./assets/title.png')
BOSS_SONG = pygame.mixer.Sound('./assets/boss.wav')
LASER_SOUND = pygame.mixer.Sound('./assets/laser_sound.wav')
LASER_SOUND.set_volume(0.2)
HEAL_SOUND = pygame.mixer.Sound('./assets/heal_sound.mp3')
HEAL_SOUND.set_volume(0.4)
RELOAD_SOUND = pygame.mixer.Sound('./assets/reload.wav')
RELOAD_SOUND.set_volume(0.3)
HIT_SOUND = pygame.mixer.Sound('./assets/hit_sound.wav')
HIT_SOUND.set_volume(0.5)
BOSS_FRAME_0 = pygame.image.load('./assets/boss2frame0.png')
BOSS_FRAME_1 = pygame.image.load('./assets/boss2frame1.png')
BOSS_FRAME_2 = pygame.image.load('./assets/boss2frame2.png')
BOSS_FRAME_3 = pygame.image.load('./assets/boss2frame3.png')
BOSS_HEIGHT = BOSS_FRAME_0.get_height() / 5
BOSS_WIDTH = BOSS_FRAME_0.get_width() / 5
BOSS_FRAME_0 = pygame.transform.scale(BOSS_FRAME_0, (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_FRAME_1 = pygame.transform.scale(BOSS_FRAME_1, (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_FRAME_2 = pygame.transform.scale(BOSS_FRAME_2, (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_FRAME_3 = pygame.transform.scale(BOSS_FRAME_3, (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_FRAME_DMG = pygame.image.load('./assets/boss2Damage.png')
BOSS_FRAME_DMG = pygame.transform.scale(BOSS_FRAME_DMG, (BOSS_WIDTH, BOSS_HEIGHT))
HEART = pygame.image.load('./assets/heart_2.gif')
HEART = pygame.transform.scale(HEART, (HEART.get_width() * 2, HEART.get_height() * 2))
TRASH = pygame.image.load('./assets/garbage.png')
TRASH = pygame.transform.scale(TRASH, (TRASH.get_width() / 5, TRASH.get_height() / 5))
MISSILE = pygame.image.load('./assets/missile1.png')
MISSILE_ICON = pygame.image.load('./assets/missileicon.png')
GAME_OVER_SONG = pygame.mixer.Sound('./assets/gameoveraudio.mp3')
MISSILE_CRATE = pygame.image.load('./assets/missilecrate.png')
MISSILE_CRATE = pygame.transform.scale(MISSILE_CRATE, (MISSILE_CRATE.get_width() / 4, MISSILE_CRATE.get_height() / 4))
PICTURE_FRAME = pygame.image.load('./assets/picture_frame.png')


global text
global line_num
global text_len
global high_score
text_list = []
line_num = 0
high_score = 0
text_len = 0


# EVENTS
BOX = pygame.USEREVENT + 1
OIL_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(BOX, 500)
PLAYER_HIT = pygame.USEREVENT + 5
PLAYER_DIED = pygame.USEREVENT + 6
PLAYER_ADD_HEART = pygame.USEREVENT + 7
PLAYER_ADD_MISSILE = pygame.USEREVENT + 8
UNPAUSING = pygame.USEREVENT + 9


def print_text():
    global text_len
    space = 580
    for text in text_list:
        text_len += 1
        WIN.blit(WORD_FONT.render(text[:text_len], True, BLUE), (135, space))
        space += 30


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
        if t == "!fight_event":
            pygame.event.post(pygame.event.Event(UNPAUSING))
            fight()
        texts = t.split(" ")
        #n = 1
        for i in texts:
            sen += i + " "
            l = WORD_FONT.render(sen, True, WHITE)
            if l.get_width() >= 700:
                text_list.append(sen)
                sen = ""
            #if n % 10 == 0:
              #  text_list.append(sen)
               # sen = ""
               # n = 1
            #n += 1
        text_list.append(sen)
        line_num += 1
    except IndexError:
        pass


def game_over(score):
    global high_score
    BOSS_SONG.stop()
    GAME_OVER_SONG.play(-1)
    if score > high_score:
        high_score = score
    active = True
    home_icon_piece = pygame.Rect(410, 550, HOME_ICON.get_width(), HOME_ICON.get_height())
    replay_icon_piece = pygame.Rect(530, 550, REPLAY_ICON.get_width(), REPLAY_ICON.get_height())
    high_score_text = FINAL_SCORE_FONT.render(str(high_score),  True, WHITE)
    score_points = FINAL_SCORE_FONT.render(str(score),  True, WHITE)
    while active:
        pos = pygame.mouse.get_pos()
        replay_icon = REPLAY_ICON
        home_icon = HOME_ICON

        if replay_icon_piece.collidepoint(pos):
            replay_icon = WHITE_REPLAY_ICON
        elif home_icon_piece.collidepoint(pos):
            home_icon = WHITE_HOME_ICON

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if replay_icon_piece.collidepoint(pos):
                    GAME_OVER_SONG.stop()
                    pygame.event.post(pygame.event.Event(UNPAUSING))
                    fight()
                elif home_icon_piece.collidepoint(pos):
                    GAME_OVER_SONG.stop()
                    intro()

        WIN.blit(OCEAN, (-900, 0))
        WIN.blit(GAME_OVER, (WIDTH/ 2 - GAME_OVER.get_width()/2, 80))
        WIN.blit(HIGHSCORE_IMG, (WIDTH/ 2 - HIGHSCORE_IMG.get_width()/2, 150 + HIGHSCORE_IMG.get_height()))
        WIN.blit(high_score_text, (WIDTH/ 2 - high_score_text.get_width()/2, 150 + HIGHSCORE_IMG.get_height() +
                                   HIGHSCORE_IMG.get_height()))
        WIN.blit(SCORE_IMG, (WIDTH/ 2 - SCORE_IMG.get_width()/2, 150 + HIGHSCORE_IMG.get_height() +
                             HIGHSCORE_IMG.get_height() + high_score_text.get_height()))
        WIN.blit(score_points, (WIDTH/ 2 - score_points.get_width()/2, 150 + HIGHSCORE_IMG.get_height() +
                                HIGHSCORE_IMG.get_height() + high_score_text.get_height() + SCORE_IMG.get_height()))
        WIN.blit(home_icon, (420, 560))
        WIN.blit(replay_icon, (540, 565))
        pygame.display.update()


def controls():
    active = True
    home_icon_piece = pygame.Rect(0, 0, HOME_ICON.get_width(), HOME_ICON.get_height())

    controls_text_string = ["-CONTROLS-", " ", "[WASD] to move", "[SPACE] to fire laser gun",
                            "(hold to spam fire, can't destory oil)","[CLICK] to fire laser missile",
                            "(blasts away everything)", "(limited ammo, obtained from missile crates)",
                            "[HOLD SHIFT] for speed boost", " ", "-Destorying junk gives +1 score-",
                            "-Blasting away oil gives +10 score-", "(Only laser missiles can blast away oil)",
                            "-Pick up hearts to heal-"]

    while active:
        pos = pygame.mouse.get_pos()
        home_icon = HOME_ICON


        if home_icon_piece.collidepoint(pos):
            home_icon = WHITE_HOME_ICON


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if home_icon_piece.collidepoint(pos):
                    return


        WIN.blit(OCEAN, (-600, 0))
        WIN.blit(home_icon, (5, 0))
        ypos = 0
        for sentence in controls_text_string:
            controls_text = SCORE_FONT.render(sentence, True, BLACK)
            WIN.blit(controls_text, (WIDTH/2 - controls_text.get_width()/2, ypos))
            ypos += controls_text.get_height()
        pygame.display.update()


def extra():
    active = True
    home_icon_piece = pygame.Rect(0, 0, HOME_ICON.get_width(), HOME_ICON.get_height())

    facts_text_string = ["Octopus have 3 hearts", "The tongue of a blue whale is heavier than an elephant",
                         "Crabs have taste buds on their feet",
                         "The shockwave from a mantis shrimp punch vaporizes water upon contact",
                         "After octopi mate they get dementia",
                         "There are more than 3 million shipwrecks on the ocean floor",
                         "The ancient sponge was the first animal",
                         "Lobsters urinate in each other's faces as a way of communicating",
                         "Seahorses are the only animal where the male gives birth"]

    while active:
        pos = pygame.mouse.get_pos()
        home_icon = HOME_ICON

        if home_icon_piece.collidepoint(pos):
            home_icon = WHITE_HOME_ICON

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if home_icon_piece.collidepoint(pos):
                    return

        WIN.blit(OCEAN, (-600, 0))
        WIN.blit(home_icon, (5, 0))
        WIN.blit(PICTURE_FRAME, (WIDTH/2 - PICTURE_FRAME.get_width()/2, 30))

        y_pos = 50 + PICTURE_FRAME.get_height()
        for sentence in facts_text_string:
            controls_text = WORD_FONT.render(sentence + "...", True, WHITE)
            WIN.blit(controls_text, (WIDTH/2 - controls_text.get_width()/2, y_pos))
            y_pos += controls_text.get_height()
        pygame.display.update()


def intro():
    active = True
    INTRO_SONG.set_volume(0.7)
    INTRO_SONG.play(-1)
    subtext = WORD_FONT.render("Singleplayer", True, BLUE)
    subtext2 = WORD_FONT.render("Exit", True, BLUE)
    frame = 0
    while active:
        pos = pygame.mouse.get_pos()
        WIN.blit(OCEAN, (frame, 0))
        WIN.blit(TITLE, (WIDTH / 2 - TITLE.get_width() / 2, 70))

        WIN.blit(BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 250))  # singleplayer
        WIN.blit(BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 320))  # quit
        WIN.blit(SMALLER_BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 450))  # left small button
        thing = pygame.transform.flip(pygame.transform.scale(BUTTON, (190, 50)), True, False)
        WIN.blit(thing, (510, 450))  # right small button
        WIN.blit(subtext, (WIDTH / 2 - subtext.get_width() / 2, 260))

        WIN.blit(subtext2, (WIDTH / 2 - subtext2.get_width() / 2, 330))

        WIN.blit(WORD_FONT.render("Extra", True, BLUE), (570, 460))
        WIN.blit(WORD_FONT.render("Controls", True, BLUE), (347, 460))
        WIN.blit(WORD_FONT.render("Beta 1.0", True, WHITE), (10, HEIGHT - WORD_FONT.get_height()))

        play_button = pygame.Rect(WIDTH / 2 - BUTTON.get_width() / 2, 250, 400, 50)
        quit_button = pygame.Rect(WIDTH / 2 - BUTTON.get_width() / 2, 320, 400, 50)

        button_1 = pygame.Rect(WIDTH / 2 - BUTTON.get_width() / 2, 450, 190, 50)
        button_2 = pygame.Rect(510, 450, 190, 50)

        if play_button.collidepoint(pos):
            WIN.blit(LARGER_BUTTON, (WIDTH / 2 - LARGER_BUTTON.get_width() / 2, 250))
            WIN.blit(subtext, (WIDTH / 2 - subtext.get_width() / 2, 260))
        elif quit_button.collidepoint(pos):
            WIN.blit(LARGER_BUTTON, (WIDTH / 2 - LARGER_BUTTON.get_width() / 2, 320))
            WIN.blit(subtext2, (WIDTH / 2 - subtext2.get_width() / 2, 330))
        elif button_1.collidepoint(pos):
            WIN.blit(SMALLER_WHITE_BUTTON, (WIDTH / 2 - BUTTON.get_width() / 2, 450))
            WIN.blit(WORD_FONT.render("Controls", True, BLUE), (347, 460))
        elif button_2.collidepoint(pos):
            WIN.blit(pygame.transform.flip(SMALLER_WHITE_BUTTON, True, False), (510, 450))
            WIN.blit(WORD_FONT.render("Extra", True, BLUE), (570, 460))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if play_button.collidepoint(pos):
                        CLICK_SOUND.play()
                        time.sleep(CLICK_SOUND.get_length())
                        active = False
                        INTRO_SONG.stop()
                        return
                    elif quit_button.collidepoint(pos):
                        CLICK_SOUND.play()
                        time.sleep(CLICK_SOUND.get_length())
                        pygame.quit()
                        sys.exit()
                    elif button_1.collidepoint(pos):
                        CLICK_SOUND.play()
                        time.sleep(CLICK_SOUND.get_length())
                        controls()
                    elif button_2.collidepoint(pos):
                        CLICK_SOUND.play()
                        time.sleep(CLICK_SOUND.get_length())
                        extra()
        pygame.display.update()


def draw_window():
    global box
    global text
    WIN.blit(SEA, (0, 0))
    WIN.blit(box, (WIDTH / 2 - box.get_width() / 2, 560))
    print_text()
    WIN.blit(ORB, (50, 500))
    #name = SCORE_FONT.render("NOVA", True, WHITE)
    #WIN.blit(name, (760, 515))
    pygame.display.update()


def oil_dropping(drop):
    WIN.blit(SEA, (0, 0))
    WIN.blit(OIL, (drop.x, drop.y))
    pygame.display.update()


def fight():
    global score
    score = 0
    player_health = 6
    vel = 5
    oil_drops = []
    trash_list = []
    dropped_hearts = []
    dropped_missiles = []
    max_bullets = 999999
    max_missiles = 10
    frames = [BOSS_FRAME_0, BOSS_FRAME_1, BOSS_FRAME_2, BOSS_FRAME_3]
    GAME_SONG.stop()
    BOSS_SONG.set_volume(0.3)
    BOSS_SONG.play(-1)
    clock = pygame.time.Clock()
    active = True
    i = 0
    pause_icon_piece = pygame.Rect(WIDTH - PAUSE_BLUE.get_width(), HEIGHT - PAUSE_BLUE.get_height()
                                   ,PAUSE_BLUE.get_width(), PAUSE_BLUE.get_height())
    piece = pygame.Rect((WIDTH//2 - frames[0].get_width()//2), 600, BOSS_WIDTH, BOSS_HEIGHT)
    bullets = []
    missiles = []
    while active:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        if i == 4:
            i = 0
        boss = frames[i]
        WIN.blit(SEA, (0, 0))
        pause_icon = PAUSE_BLUE
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and pause_icon_piece.collidepoint(pos):
                    pause_game()
                elif event.button == 1 and max_missiles > 0:
                    LASER_SOUND.play()
                    missile = pygame.Rect(piece.x + piece.width // 2 - MISSILE.get_width() // 2, piece.y -
                                          MISSILE.get_height() + 25, MISSILE.get_width(), MISSILE.get_height())
                    missiles.append(missile)
                    max_missiles -= 1
            if event.type == PLAYER_ADD_HEART and player_health < 6:
                player_health += 1
                HEAL_SOUND.play()
            if event.type == PLAYER_ADD_MISSILE and max_missiles < 10:
                RELOAD_SOUND.play()
                max_missiles = 10
            if event.type == PLAYER_DIED:
                game_over(score)
            if event.type == PLAYER_HIT:
                HIT_SOUND.play()
                boss = BOSS_FRAME_DMG
                player_health -= 1
                if player_health <= 0:
                    pygame.event.post(pygame.event.Event(PLAYER_DIED))
            if event.type == UNPAUSING:
                num = 3
                while num > 0:
                    unpausing_text = SCORE_FONT.render(str(num), True, WHITE)
                    WIN.blit(SEA, (0, 0))
                    WIN.blit(unpausing_text, (WIDTH/2 - unpausing_text.get_width()/2, HEIGHT/2 -
                                              unpausing_text.get_height()/2))
                    pygame.display.update()
                    time.sleep(1)
                    num -= 1
        if keys_pressed[pygame.K_SPACE]:
            bullet = pygame.Rect(piece.x + piece.width // 2 - 4, piece.y - 5, 10, 3)
            bullets.append(bullet)
            bullet1 = pygame.Rect(piece.x + piece.width * 0.25, piece.y - 5, 3, 5)
            bullet2 = pygame.Rect(piece.x + piece.width * 0.75, piece.y - 5, 3, 5)
            bullets.append(bullet1)
            bullets.append(bullet2)
            max_bullets -= 3
        if keys_pressed[pygame.K_LSHIFT]:
            vel = 20
        if keys_pressed[pygame.K_LSHIFT] is False:
            vel = 10

        chance = random.randint(0, 17)
        drop_chance = random.randint(0, 500)
        if chance == 5:
            x_pos = random.randint(0, 900)
            drop = pygame.Rect(x_pos, 0, OIL.get_width(), OIL.get_height())
            oil_drops.append(drop)
        if chance == 6 or chance == 7:
            x_pos = random.randint(0, 900)
            trash = pygame.Rect(x_pos, 0, TRASH.get_width(), TRASH.get_height())
            trash_list.append(trash)
        if drop_chance == 100:
            x_pos = random.randint(0, 900)
            dropped_heart = pygame.Rect(x_pos, 0, HEART.get_width(), HEART.get_height())
            dropped_hearts.append(dropped_heart)
        if drop_chance < 2:
            x_pos = random.randint(0, 900)
            dropped_missile = pygame.Rect(x_pos, 0, MISSILE_CRATE.get_width(), MISSILE_CRATE.get_height())
            dropped_missiles.append(dropped_missile)

        handle_everything(bullets, missiles, oil_drops, trash_list, piece, dropped_hearts, dropped_missiles)

        handle_movement(keys_pressed, piece, vel)
        for bullet in bullets:
            pygame.draw.rect(WIN, GREEN, bullet)
        for missile in missiles:
            WIN.blit(MISSILE, (missile.x, missile.y))
        for drop in oil_drops:
            WIN.blit(OIL, (drop.x, drop.y))
        for trash in trash_list:
            WIN.blit(TRASH, (trash.x, trash.y))
        for dropped_heart in dropped_hearts:
            WIN.blit(HEART, (dropped_heart.x, dropped_heart.y))
        for dropped_missile in dropped_missiles:
            WIN.blit(MISSILE_CRATE, (dropped_missile.x, dropped_missile.y))

        WIN.blit(boss, (piece.x, piece.y))

        score_points = SCORE_FONT.render(str(score),  True, WHITE)
        WIN.blit(score_points, (WIDTH - score_points.get_width(), 0))
        hx_pos = 0
        for heart in range(player_health):
            WIN.blit(HEART, (hx_pos, 0))
            hx_pos += HEART.get_width()
        hx_pos = 0
        for icon in range(max_missiles):
            WIN.blit(MISSILE_ICON, (hx_pos, 30))
            hx_pos += MISSILE_ICON.get_width()

        if pause_icon_piece.collidepoint(pos):
            pause_icon = PAUSE_YELLOW
        WIN.blit(pause_icon, (pause_icon_piece.x, pause_icon_piece.y))
        pygame.display.update()
        i += 1
    BOSS_SONG.stop()
    GAME_SONG.play(-1)
    return


def handle_everything(bullets, missiles, oil_drops, trash_list, piece, dropped_hearts, dropped_missiles):
    global score
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        for trash in trash_list:
            if trash.colliderect(bullet):
                trash_list.remove(trash)
                bullets.remove(bullet)
                score += 1
        if bullet.x < 0:
            bullets.remove(bullet)

    for missile in missiles:
        missile.y -= 20
        for trash in trash_list:
            if trash.colliderect(missile):
                trash_list.remove(trash)
                score += 1
        for oil in oil_drops:
            if oil.colliderect(missile):
                oil_drops.remove(oil)
                score += 10

    for drop in oil_drops:
        drop.y += 10
        if drop.y > HEIGHT:
            oil_drops.remove(drop)
        elif drop.colliderect(piece):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            oil_drops.remove(drop)
        for bullet in bullets:
            if bullet.colliderect(drop):
                bullets.remove(bullet)

    for trash in trash_list:
        trash.y += 10
        if trash.y > HEIGHT:
            trash_list.remove(trash)
        elif trash.colliderect(piece):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            trash_list.remove(trash)

    for dropped_heart in dropped_hearts:
        dropped_heart.y += 15
        if dropped_heart.y > HEIGHT:
            dropped_hearts.remove(dropped_heart)
        elif dropped_heart.colliderect(piece):
            pygame.event.post(pygame.event.Event(PLAYER_ADD_HEART))
            dropped_hearts.remove(dropped_heart)

    for dropped_missile in dropped_missiles:
        dropped_missile.y += 10
        if dropped_missile.y > HEIGHT:
            dropped_missiles.remove(dropped_missile)
        elif dropped_missile.colliderect(piece):
            pygame.event.post(pygame.event.Event(PLAYER_ADD_MISSILE))
            dropped_missiles.remove(dropped_missile)


def handle_movement(keys_pressed, piece, vel):
    if keys_pressed[pygame.K_a] and piece.x - vel > 0:  # LEFT
        piece.x -= vel
    if keys_pressed[pygame.K_d] and piece.x + vel + piece.width < WIDTH:  # RIGHT
        piece.x += vel
    if keys_pressed[pygame.K_w] and piece.y - vel > 0:  # UP
        piece.y -= vel
    if keys_pressed[pygame.K_s] and piece.y + vel + piece.height < HEIGHT:  # DOWN
        piece.y += vel


def pause_game():
    active = True
    BOSS_SONG.set_volume(0)
    unpause = UNPAUSED_BLUE
    home_icon_piece = pygame.Rect(0, 0, HOME_ICON.get_width(), HOME_ICON.get_height())
    while active:
        pos = pygame.mouse.get_pos()
        WIN.blit(SEA, (0, 0))
        unpause_text = pygame.Rect(WIDTH /2 - unpause.get_width() / 2, HEIGHT / 2 - unpause.get_height() / 2,
                                   unpause.get_width(), unpause.get_height())
        WIN.blit(unpause, (unpause_text.x, unpause_text.y))
        if unpause_text.collidepoint(pos):
            unpause = UNPAUSED_WHITE
        else:
            unpause = UNPAUSED_BLUE

        home_icon = HOME_ICON

        if home_icon_piece.collidepoint(pos):
            home_icon = WHITE_HOME_ICON

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if unpause_text.collidepoint(pos):
                        active = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if home_icon_piece.collidepoint(pos):
                    intro()
        WIN.blit(home_icon, (5, 0))
        pygame.display.update()
    INTRO_SONG.stop()
    BOSS_SONG.set_volume(0.3)
    pygame.event.post(pygame.event.Event(UNPAUSING))
    return


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
                for i in range(10):
                    x_pos = random.randint(0, 900)
                    drop = pygame.Rect(x_pos, 0, SIZE, SIZE)
                    oil_drops.append(drop)
                for drop in oil_drops:
                    while drop.y < HEIGHT:
                        drop.y += 10
                        oil_dropping(drop)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    update_text()
                #if event.key == pygame.K_b:
                    #pygame.event.post(pygame.event.Event(OIL_EVENT))
                #if event.key == pygame.K_v:
                    #fight()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    update_text()
        draw_window()
    pygame.quit()
    sys.exit()


main()
