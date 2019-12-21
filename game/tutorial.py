import pygame
pygame.init()

display_width = 800
display_height = 600

Display = pygame.display.set_mode ((display_width,display_height))
pygame.display.set_caption ("Oh")
clock = pygame.time.Clock()

trumpImg = pygame.image.load('trump.png')
trumpImg = pygame.transform.scale(trumpImg, (115, 150))

def trump(x,y):
    Display.blit(trumpImg, (x,y))

crashed = False

trumpX=0

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        else : x_change = 0

        print(event)

    trumpX += x_change
    trump(trumpX,0)

    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()
