import pygame, sys


def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center= (300, 300))
    return rotated_surface, rotated_rect

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode([1600,1600])
car=pygame.image.load("Cool Car.png")
#car=pygame.transform.scale(400, 400)
car_rect=car.get_rect(center= (800,800))
angle=0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    angle += 1
    screen.fill((255,255,255))
    car_rotated, car_rotated_rect = rotate(car, angle)
    
    screen.blit(car_rotated, car_rotated_rect)
    pygame.display.flip()
    clock.tick(30)