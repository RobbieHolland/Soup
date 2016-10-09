import pygame
import sys
import pygame.gfxdraw
import time
import creature
import genetics
import numpy as np
import utility
import ray

pygame.init()
width = 1120
height = 630
screen = pygame.display.set_mode((width,height))
number_of_creatures = 10
creatures = []
for i in range(number_of_creatures):
  creatures.append(creature.Creature(10, 10, 10, (250, 250, 10), 5, 1, 1))
number_of_steps_per_episode = 10000

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


ray1 = ray.ray([0, 0], [100, 100], [0, 0, 0])

print('Evolution starting')
step = 0
start = time.clock()
skip = 10
while True:
  step += 1
  if time.clock() - start > 10:
      break;
  #time.sleep(0.5)
  #get observations
  #propagate observation through network and find creature velocities
  #do physics (moving and bouncing)
  #calculate new fitness
  for creature in creatures:
      creature.step(np.random.rand(5, 1), width, height)

  
#  if step % number_of_steps_per_episode == 0:
#    creatures = genetics.crossover_mutate(creatures, 0.05)

  screen.fill([180, 180, 180])
  for creature in creatures:
    creature.draw(screen)
  ray1.draw(screen)

  pygame.display.update()
    #Pass creatures to function that does crossover, culling and then returns a new set of creatures

print(step)
