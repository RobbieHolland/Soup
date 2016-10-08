import pygame
import sys
import pygame.gfxdraw
import time

#import tensorflow as tf

pygame.init()
screen = pygame.display.set_mode((1120,630))
creatures = TABLE OF CREATURE OBJECTS
number_of_steps_per_episode = 100

"""
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
"""

print('Evolution starting')
step = 0
while True:
  step += 1
  #get observations
  #propagate observation through network and find creature velocities
  #do physics (moving and bouncing)
  #calculate new fitness
  if step % number_of_steps_per_episode == 0:
    #Pass creatures to function that does crossover, culling and then returns a new set of creatures

