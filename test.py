import pygame
import sys
import pygame.gfxdraw
import time

pygame.init()

white = (255,255,255)

screen = pygame.display.set_mode((640,480))
colour = (10, 180, 30)
x = 300
y = 250
width = 20
height = 30
thickness = 5
radius = 10
#pygame.gfxdraw.rect(screen, colour, (x,y,width,height), thickness)
pygame.display.update()
#pygame.draw.arc(screen, colour, (x,y,width,height), 0, 2, 0.5)
#pygame.display.update()

i = 0
t0 = time.clock()
while True:
  i += 1
  if time.clock() - t0 > 5:
    break;
  #print time.clock() - t0
  #colour = (3*i % 255, 5*i % 255, 7*i % 255)  
  screen.fill(colour)
  pygame.gfxdraw.filled_circle(screen, x, y, radius, colour)
  pygame.gfxdraw.aacircle(screen, x, y, radius, colour)
  #pygame.display.update()

print(i)
