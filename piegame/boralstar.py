import pygame

display_width = 800
display_height = 600
white = (255,255,255)

x_change = 0
y_change = 0

x_middle = 0.5
y_middle = 0.5

x_spawn_change = 0.1109
y_spawn_change = -0.169

bull_speed = 0
bull_width = 70
bull_height = 78
bullX = (display_width * 0.45)
bullY = (display_height * 0.376)

back_width = 2400
back_height = 1800
backX = (display_width * x_middle - back_width * (x_middle + x_spawn_change))
backY = (display_height * y_middle - back_height * (y_middle + y_spawn_change))

crashed= False


# starts pygame
pygame.init()

# sets display & basic settings
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Boralstar')
clock = pygame.time.Clock()

# images : load & resize
backImg=pygame.image.load('Feast_or_Famine-Map.png')
backImg = pygame.transform.scale(backImg, (back_width, back_height))
bullImg=pygame.image.load('CORONA.png')
bullImg = pygame.transform.scale(bullImg, (65, 80))

def move(x,y,sprite):
    gameDisplay.blit(sprite, (x,y))


# game code
while not crashed:

    # exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    # arrow key movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] :
        x_change = + 5
    elif keys[pygame.K_RIGHT] :
        x_change = - 5
    else :
        x_change = 0

    if keys[pygame.K_UP] :
        y_change = + 5
    elif keys[pygame.K_DOWN] :
        y_change = -5
    else :
        y_change = 0

    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_LEFT:
    #         x_change = + 5
    #     elif event.key == pygame.K_RIGHT:
    #         x_change = - 5
    #     elif event.key == pygame.K_DOWN:
    #         y_change = - 5
    #     elif event.key == pygame.K_UP:
    #         y_change = 5
    # if event.type == pygame.KEYUP:
    #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #         x_change = 0
    #     if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
    #         y_change = 0

    if (backX + back_width <= display_width) and x_change < 0 and bullX < display_width - bull_width  :
        bullX -= x_change
        x_change = 0
    elif x_change > 0 and (backX + back_width <= display_width) and bullX > display_width * x_middle  :
        bullX -= x_change
        x_change = 0
    elif (bullX >= display_width - bull_width):
        x_change = 0

    if (backY + back_height <= display_height) and y_change < 0 and bullY < display_height - bull_height  :
        bullY -= y_change
        y_change = 0
    elif y_change > 0 and (backY + back_height <= display_height) and bullY > display_height * y_middle  :
        bullY -= y_change
        y_change = 0
    elif (bullY >= display_height - bull_height):
        y_change = 0



    # if ((backY + 1800 <= 600)) and bullY <= 500:
    #     y_change = 0
    #     bullY -= y_change
    #
    # if ((backY >= 0)) and bullY >= 0:
    #     y_change = 0
    #     bullY -= y_change
    #
    # if ((backX + 2400 <= 800)) and x_change < 0 :
    #     bullX -= x_change
    #
    # if ((backX >= 0)) and x_change > 0:
    #     bullX -= x_change

    # if ((backX < 0) and x_change > 0 ) or ((backX + 2400 > 800) and (x_change < 0)):
    #     backX += x_change
    #
    #
    # if ((backY < 0) and y_change > 0) or ((backY + 1800 > 600) and (y_change < 0)) :
    #     backY += y_change


    backX += x_change
    backY += y_change


    gameDisplay.fill(white)
    move(backX, backY, backImg)
    move(bullX, bullY, bullImg)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
