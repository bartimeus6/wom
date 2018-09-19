#World of Monsters v2.0

import pygame
import time
import random as r

pygame.init()

#set game window
win= pygame.display.set_mode((500, 500))
pygame.display.set_caption(('experiment'))

#set Clock
clock= pygame.time.Clock()

#some data
x= 100
y= 100
width= 50
height= 50
vel= 5
red= (255, 0, 0)

#text
font= pygame.font.SysFont(None, 50)

def message(msg, color):
    text= font.render(msg, True, color)
    win.blit(text, [150, 225])

#draw the rectangle and fill after it moves
def displayUpdate():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (60, 60, 60), (x, y, width, height))
    pygame.display.update()

#main loop
while True:
#set FPS
    clock.tick(30)

#set quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            message('Quitting...', red)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            quit()

    keys= pygame.key.get_pressed()

#set movements and borders
    if keys[pygame.K_w]:
        y-= vel
        if y<= 0:
            y= 0
    if keys[pygame.K_s]:
        y+= vel
        if y>= 500-height:
            y= 500-height
    if keys[pygame.K_d]:
        x+= vel
        if x>= 500-width:
            x= 500-width
    if keys[pygame.K_a]:
        x-= vel
        if x<= 0:
            x= 0

    displayUpdate()
