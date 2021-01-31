import pygame
pygame.init()

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("John Wick")


width = 50
height = 50
x=100
y=700
vel=5
screen_width = 800
screen_height = 800
isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(10)

    #Handles quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    #Fundamental player movement
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel

    if not (isJump):
        #if keys[pygame.K_UP] and y > vel:
            #y -= vel
        #if keys[pygame.K_DOWN] and y < screen_height - height - vel:
            #y += vel
        if keys[pygame.K_SPACE]:
            isJump = True

    #The jumping math using quadratics
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount-=1 

        else:
            isJump = False
            jumpCount = 10

    #Draws character
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    

pygame.quit()