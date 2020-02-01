import pygame

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Boralstar')

white = (255,255,255)

bull_width = 70
bull_height = 78
x_change = 0
y_change = 0
bull_speed = 0
clock = pygame.time.Clock()

crashed= False
backImg=pygame.image.load('Feast_or_Famine-Map.png')
bullImg=pygame.image.load('CORONA.png')
bullImg = pygame.transform.scale(bullImg, (65, 80))
backImg = pygame.transform.scale(backImg, (2400, 1800))

def bull(x,y):
    gameDisplay.blit(bullImg, (x,y))

def back(x,y):
    gameDisplay.blit(backImg, (x,y))

bullX = (display_width * 0.45)
bullY = (display_height * 0.376)
backX = (display_width * -0.5)
backY = (display_height * -0.5)
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = + 5
        elif event.key == pygame.K_RIGHT:
            x_change = - 5
        elif event.key == pygame.K_DOWN:
            y_change = - 5
        elif event.key == pygame.K_UP:
            y_change = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            y_change = 0

    backX += x_change
    backY += y_change

    gameDisplay.fill(white)
    back(backX,backY)
    bull(bullX,bullY)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
