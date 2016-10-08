import pygame
import sys
import pygame.gfxdraw
import time
import creature
import genetics
import numpy as np

pygame.init()
width = 1120
height = 630
screen = pygame.display.set_mode((width,height))
creatures = [creature.Creature(10, 10, 10, (250, 250, 10), 5, 1, 1), creature.Creature(10, 10, 10, (250, 250, 10), 5, 1, 1)]
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

print('Evolution starting')
step = 0
start = time.clock()
while True:
  step += 1
  if time.clock() - start > 5:
      break;
  #time.sleep(0.5)
  #get observations
  #propagate observation through network and find creature velocities
  #do physics (moving and bouncing)
  #calculate new fitness
  for creature in creatures:
      creature.step(np.random.rand(5, 1), width, height)

  if step % number_of_steps_per_episode == 0:
    creatures = genetics.crossover_mutate(creatures, 0.05)
    screen.fill([0, 0, 0])
  for creature in creatures:
    creature.draw(screen)
  #pygame.display.update()
    #Pass creatures to function that does crossover, culling and then returns a new set of creatures

print(step)
