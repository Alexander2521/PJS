import pygame

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

magic_width = 123
magic_height = 178
clock = pygame.time.Clock()


home = 150
crashed = False
magicImg = pygame.image.load('magic-johnson.png')

def magic(x,y):
    gameDisplay.blit(magicImg, (x,y))

def text_objects(text, font) :
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def text(txt, textX, textY) :
    alextxt = pygame.font.Font("freesansbold.ttf", 50)
    textsurf, textrect = text_objects(txt, alextxt)
    textrect.center = ( textX, textY)
    gameDisplay.blit(textsurf, textrect)

magicX = (display_width * 0.45)
magicY = (display_height * 0.376)
HomeX = (display_width/2)
HomeY = (display_height/2 + home)
x_change = 0
y_change = 0
car_speed = 0

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = - 5
        elif event.key == pygame.K_RIGHT:
            x_change = 5
        elif event.key == pygame.K_DOWN:
            y_change = 5
        elif event.key == pygame.K_UP:
            y_change = -5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            y_change = 0

    magicX += x_change
    magicY += y_change

    # HomeX += x_change
    # HomeY += y_change

    gameDisplay.fill(white)
    magic(magicX,magicY)
    text("Hi I'm magic Johnson", magicX, magicY + magic_height)
        # print(event)

    if magicX < 0:
        magicX = 0
    if magicX > display_width - magic_width:
        magicX= display_width - magic_width

    if magicY < 0 :
        magicY = 0
    if magicY > display_height - magic_height:
        magicY = display_height - magic_height




    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
