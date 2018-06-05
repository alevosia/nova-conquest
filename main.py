import pygame
import random
import time
pygame.init()
pygame.font.init()
# my modules

# game configuration
game_title = 'Nova Conquest'
display_width = 1280
display_height = 800

# custom rgb colors0
black   = (0, 0, 0)
white   = (255, 255, 255)

# set the configuration
enemy_ship = pygame.image.load('tera_sp1_r.png')
pygame.display.set_caption(game_title) # window title
pygame.display.set_icon(enemy_ship) # window title
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.mixer.music.load('retro_space.mp3')
pygame.mixer.music.play(-1)
laser = pygame.mixer.Sound('lazer.ogg')
expsound = pygame.mixer.Sound('expsound.ogg')
clock = pygame.time.Clock()

# sprites
ship_width = 80
ship_height = 100

shipImg = pygame.image.load('spaceship.png')
shipImg = pygame.transform.scale(shipImg, (ship_width, ship_height))

enemy_ship = pygame.transform.scale(enemy_ship, (ship_width, ship_height))

enemy_ship2 = pygame.image.load('tera_sp2.png')
enemy_ship2 = pygame.transform.scale(enemy_ship2, (ship_width, ship_height))

bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (30, 50))

space_bg1 = pygame.image.load('space_bg.png')
space_bg1 = pygame.transform.scale(space_bg1, (display_width, display_height))
space_bg2 = pygame.image.load('space_bg.png')
space_bg2 = pygame.transform.scale(space_bg2, (display_width, display_height))
space_bg3 = pygame.image.load('space_bg.png')
space_bg3 = pygame.transform.scale(space_bg3, (display_width, display_height))
exp1 = pygame.image.load('exp1.png')
exp2 = pygame.image.load('exp2.png')
exp3 = pygame.image.load('exp3.png')
exp4 = pygame.image.load('exp4.png')
exp5 = pygame.image.load('exp5.png')
exp6 = pygame.image.load('exp6.png')
exp7 = pygame.image.load('exp7.png')
exp8 = pygame.image.load('exp8.png')
exp9 = pygame.image.load('exp9.png')
exp10 = pygame.image.load('exp10.png')

# functions
def drawShip(x, y):
    gameDisplay.blit(shipImg, (x, y))

def drawEnemyShip1(x, y):
    gameDisplay.blit(enemy_ship, (x, y))

def drawEnemyShip2(x, y):
    gameDisplay.blit(enemy_ship2, (x, y))

def drawBG1(bg_y):
    gameDisplay.blit(space_bg1, (0, bg_y))

def drawBG2(bg_y):
    gameDisplay.blit(space_bg2, (0, bg_y - display_height))

def drawBG3(bg_y):
    gameDisplay.blit(space_bg3, (0, bg_y + display_height))

def drawBullet(x, y):
    gameDisplay.blit(bullet, (x, y))


def explosion(x,y):
    gameDisplay.blit(exp1, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp2, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp3, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp4, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp5, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp6, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp7, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp8, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp9, (x,y))
    pygame.display.update()
    gameDisplay.blit(exp10, (x,y))
    pygame.display.update()

# SCOREBOARD ===================================================
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    font = pygame.font.Font('COLONNA.TTF', 100)
    TextSurface, TextRect = text_objects(text, font)
    TextRect.center = ((display_width/2, 30))
    gameDisplay.blit(TextSurface, TextRect)

def displayScore(score):
    message_display(score)

# GAME OVER ===================================================
def text_objects2(text, font):
    textSurface = font.render(text, True, (220,20,60))
    return textSurface, textSurface.get_rect()

def message_display2(text):
    font = pygame.font.Font('COLONNA.TTF', 100)
    TextSurface, TextRect = text_objects2(text, font)
    TextRect.center = ((display_width/2, display_height/2))
    gameDisplay.blit(TextSurface, TextRect)

def displayEnd(text):
    message_display2(text)


# the game loop ======================================================
def game_loop(ship_width, ship_height, enemy_ship):

    score = 0
    # starting position of car
    x = (display_width * 0.50)
    y = (display_height - ship_height)

    change_x = 0
    change_y = 0

    enemy_ship_startX = random.randrange(0, display_width-ship_width)
    enemy_ship_startY = -ship_height
    enemy_ship_speed = 10

    enemy_ship2_startX = random.randrange(0, display_width-ship_width)
    enemy_ship2_startY = -ship_height
    enemy_ship2_speed = 7

    enemy_ship3_startX = random.randrange(0, display_width-ship_width)
    enemy_ship3_startY = -ship_height
    enemy_ship3_speed = 8

    enemy_ship4_startX = random.randrange(0, display_width-ship_width)
    enemy_ship4_startY = -ship_height
    enemy_ship4_speed = 12

    enemy_ship5_startX = random.randrange(0, display_width-ship_width)
    enemy_ship5_startY = -ship_height
    enemy_ship5_speed = 5

    enemy_ship6_startX = random.randrange(0, display_width-ship_width)
    enemy_ship6_startY = -ship_height
    enemy_ship6_speed = 3

    bg_y = 0
    default_bg_y_change = 1.5
    bg_y_change = default_bg_y_change

    # attributes
    fspeed = 6
    side_speed = 8
    boost_speed = fspeed * 2

    fired = False
    bullet_startY = 0
    bullet_startX = 0
    bullet_speed = 10

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    change_x += -side_speed
                elif event.key == pygame.K_d:
                    change_x += side_speed
                elif event.key == pygame.K_w:
                    bg_y_change += fspeed
                    enemy_ship_speed += fspeed
                    enemy_ship2_speed += fspeed
                    enemy_ship3_speed += fspeed
                    enemy_ship4_speed += fspeed
                    enemy_ship5_speed += fspeed
                    enemy_ship6_speed += fspeed

                elif event.key == pygame.K_LSHIFT:
                    bg_y_change += boost_speed
                    enemy_ship_speed += boost_speed
                    enemy_ship2_speed += boost_speed
                    enemy_ship3_speed += boost_speed
                    enemy_ship4_speed += boost_speed
                    enemy_ship5_speed += boost_speed
                    enemy_ship6_speed += boost_speed

                elif event.key == pygame.K_1:
                    bullet_speed += 1

                if not fired:
                    if event.key == pygame.K_SPACE:
                        laser.play()
                        fired = True
                        bullet_startX = x + 15
                        bullet_startY = y

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    change_x += side_speed
                elif event.key == pygame.K_d:
                    change_x += -side_speed
                elif event.key == pygame.K_w:
                    bg_y_change = default_bg_y_change
                    enemy_ship_speed -= fspeed
                    enemy_ship2_speed -= fspeed
                    enemy_ship3_speed -= fspeed
                    enemy_ship4_speed -= fspeed
                    enemy_ship5_speed -= fspeed
                    enemy_ship6_speed -= fspeed



                elif event.key == pygame.K_LSHIFT:
                    bg_y_change -= boost_speed
                    enemy_ship_speed -= boost_speed
                    enemy_ship2_speed -= boost_speed
                    enemy_ship3_speed -= boost_speed
                    enemy_ship4_speed -= boost_speed
                    enemy_ship5_speed -= boost_speed
                    enemy_ship6_speed -= boost_speed


        if bg_y_change < 0:
            bg_y_change = default_bg_y_change

        x += change_x
        bg_y += bg_y_change
        #print('({}, {})'.format(x,y))

        # border controls
        if x < 0:
            x = 0
        elif x > display_width - ship_width:
            x = display_width - ship_width

        if bg_y > display_height:
            bg_y = 0
        elif bg_y < -display_height:
            bg_y = 0

        drawBG1(bg_y)
        drawBG2(bg_y)
        drawBG3(bg_y)
        displayScore(str(score))
        drawShip(x, y)

        if fired:
            drawBullet(bullet_startX, bullet_startY)
            bullet_startY -= bullet_speed
            if bullet_startY <= enemy_ship_startY+ship_height and (bullet_startX >= enemy_ship_startX and bullet_startX <= enemy_ship_startX+ship_width):
                explosion(enemy_ship_startX, enemy_ship_startY)
                expsound.play()
                score += 1
                fired = False
                enemy_ship_startY = -ship_height
                enemy_ship_startX = random.randrange(0, display_width-ship_width)
            elif bullet_startY <= enemy_ship2_startY+ship_height and (bullet_startX >= enemy_ship2_startX and bullet_startX <= enemy_ship2_startX+ship_width):
                explosion(enemy_ship2_startX, enemy_ship2_startY)
                expsound.play()
                score += 1
                fired = False
                enemy_ship2_startY = -ship_height
                enemy_ship2_startX = random.randrange(0, display_width-ship_width)
            elif bullet_startY <= enemy_ship3_startY+ship_height and (bullet_startX >= enemy_ship3_startX and bullet_startX <= enemy_ship3_startX+ship_width):
                explosion(enemy_ship3_startX, enemy_ship3_startY)
                expsound.play()
                score += 1
                fired = False
                enemy_ship3_startY = -ship_height
                enemy_ship3_startX = random.randrange(0, display_width-ship_width)
            elif bullet_startY <= enemy_ship4_startY+ship_height and (bullet_startX >= enemy_ship4_startX and bullet_startX <= enemy_ship4_startX+ship_width):
                explosion(enemy_ship4_startX, enemy_ship4_startY)
                expsound.play()
                score += 1
                fired = False
                enemy_ship4_startY = -ship_height
                enemy_ship4_startX = random.randrange(0, display_width-ship_width)
            elif bullet_startY <= enemy_ship5_startY+ship_height and (bullet_startX >= enemy_ship5_startX and bullet_startX <= enemy_ship5_startX+ship_width):
                explosion(enemy_ship5_startX, enemy_ship5_startY)
                expsound.play()
                score += 1
                fired = False
                enemy_ship5_startY = -ship_height
                enemy_ship5_startX = random.randrange(0, display_width-ship_width)
            elif bullet_startY <= enemy_ship6_startY+ship_height and (bullet_startX >= enemy_ship6_startX and bullet_startX <= enemy_ship6_startX+ship_width):
                explosion(enemy_ship6_startX, enemy_ship6_startY)
                expsound.play()
                score += 1
                fired = False
                enemy_ship6_startY = -ship_height
                enemy_ship6_startX = random.randrange(0, display_width-ship_width)
            elif bullet_startY < 0:
                fired = False

        drawEnemyShip1(enemy_ship_startX, enemy_ship_startY)
        drawEnemyShip2(enemy_ship2_startX, enemy_ship2_startY)
        drawEnemyShip1(enemy_ship3_startX, enemy_ship3_startY)
        drawEnemyShip2(enemy_ship4_startX, enemy_ship4_startY)
        drawEnemyShip1(enemy_ship5_startX, enemy_ship5_startY)
        drawEnemyShip2(enemy_ship6_startX, enemy_ship6_startY)
        enemy_ship_startY += enemy_ship_speed
        enemy_ship2_startY += enemy_ship2_speed
        enemy_ship3_startY += enemy_ship3_speed
        enemy_ship4_startY += enemy_ship4_speed
        enemy_ship5_startY += enemy_ship5_speed
        enemy_ship6_startY += enemy_ship6_speed


        if (enemy_ship_startY >= y and enemy_ship_startY <= display_height) and (enemy_ship_startX >= x and enemy_ship_startX <= x + ship_width):
            explosion(x, y)
            expsound.play()
            displayEnd('Game Over')
            pygame.display.update()
            time.sleep(3)
            gameExit = True
        elif enemy_ship_startY > display_height:
            enemy_ship_startY = -ship_height
            enemy_ship_startX = random.randrange(0, display_width-ship_width)


        if (enemy_ship2_startY >= y and enemy_ship2_startY <= display_height) and (enemy_ship2_startX >= x and enemy_ship2_startX <= x + ship_width):
            explosion(x, y)
            expsound.play()
            displayEnd('Game Over')
            pygame.display.update()
            time.sleep(3)
            gameExit = True
        elif enemy_ship2_startY > display_height:
            enemy_ship2_startY = -ship_height
            enemy_ship2_startX = random.randrange(0, display_width-ship_width)


        if (enemy_ship3_startY >= y and enemy_ship3_startY <= display_height) and (enemy_ship3_startX >= x and enemy_ship3_startX <= x + ship_width):
            explosion(x, y)
            expsound.play()
            displayEnd('Game Over')
            pygame.display.update()
            time.sleep(3)
            gameExit = True
        elif enemy_ship3_startY > display_height:
            enemy_ship3_startY = -ship_height
            enemy_ship3_startX = random.randrange(0, display_width-ship_width)


        if (enemy_ship4_startY >= y and enemy_ship4_startY <= display_height) and (enemy_ship4_startX >= x and enemy_ship4_startX <= x + ship_width):
            explosion(x, y)
            expsound.play()
            displayEnd('Game Over')
            pygame.display.update()
            time.sleep(3)
            gameExit = True
        elif enemy_ship4_startY > display_height:
            enemy_ship4_startY = -ship_height
            enemy_ship4_startX = random.randrange(0, display_width-ship_width)


        if (enemy_ship5_startY >= y and enemy_ship5_startY <= display_height) and (enemy_ship5_startX >= x and enemy_ship5_startX <= x + ship_width):
            explosion(x, y)
            expsound.play()
            displayEnd('Game Over')
            pygame.display.update()
            time.sleep(3)
            gameExit = True
        elif enemy_ship5_startY > display_height:
            enemy_ship5_startY = -ship_height
            enemy_ship5_startX = random.randrange(0, display_width-ship_width)


        if (enemy_ship6_startY >= y and enemy_ship6_startY <= display_height) and (enemy_ship6_startX >= x and enemy_ship6_startX <= x + ship_width):
            explosion(x, y)
            expsound.play()
            displayEnd('Game Over')
            pygame.display.update()
            time.sleep(3)
            gameExit = True
        elif enemy_ship6_startY > display_height:
            enemy_ship6_startY = -ship_height
            enemy_ship6_startX = random.randrange(0, display_width-ship_width)

        pygame.display.update()
        clock.tick(60) # frames per second

game_loop(ship_width, ship_height, enemy_ship)
pygame.quit()
quit()

# AUTHOR: Alexander Mariñas
