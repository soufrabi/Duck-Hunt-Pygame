# Python Arcade Shooting Gallery

import pygame
import math

pygame.init()
fps = 60
timer = pygame.time.Clock()


WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Level wise background, banners, guns
bgs = []
banners = []
guns = []
level = 1


for i in range(1,4):
    bgs.append(pygame.image.load(f'assets/bgs/{i}.png'))
    banners.append(pygame.image.load(f'assets/banners/{i}.png'))
    guns.append(pygame.transform.scale(pygame.image.load(f'assets/guns/{i}.png'),  (100,100)) )



# draw gun to make the application look good
# otherwise the image of the gun will have no impact on gameplay
def draw_gun():
    mouse_pos = pygame.mouse.get_pos()
    gun_point = (WIDTH/2,HEIGHT-200)
    lasers = ['red','purple','green']
    clicks = pygame.mouse.get_pressed()

    # calculate slope but don't divide by zero
    if mouse_pos[0] != gun_point[0] :
        slope = (mouse_pos[1]-gun_point[1])/(mouse_pos[0]-gun_point[0])
    else :
        slope = -100000

    angle = math.atan(slope)
    rotation = math.degrees(angle)

    # left side of the screen
    if mouse_pos[0] < WIDTH/2 :
        gun = pygame.transform.flip(guns[level-1],True,False)

        if mouse_pos[1]<600 :
            screen.blit(pygame.transform.rotate(gun, 90-rotation),  (WIDTH/2 - 90, HEIGHT -250))
            if clicks[0]:
                pygame.draw.circle(screen,lasers[level-1], mouse_pos, 5)
    else:
        gun = guns[level-1]

        if mouse_pos[1]<600:
            screen.blit(pygame.transform.rotate(gun, 270-rotation), (WIDTH/2 -30, HEIGHT-250) )
            if clicks[0]:
                pygame.draw.circle(screen,lasers[level-1],mouse_pos, 5)



run = True

while run:
    timer.tick(fps)

    screen.fill('white')
    screen.blit(bgs[level-1],(0,0))
    screen.blit(banners[level-1],(0,HEIGHT-200))

    # gun
    if level > 0:
        draw_gun()

    # To quit the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.flip()

pygame.quit()









