import pygame
pygame.init()

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("John Wick")


width = 50
height = 50
x=100
y=100
vel=5
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    keys = pygamme.key.get_pressed()
    
    if keys[pygame.K_LEFT]:

    if keys[pygame.K_RIGHT]:

    if keys[pygame.K_UP]:

    if keys[pygame.K_DOWN]:

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    

pygame.quit()