import pygame
import sys
import pygame.gfxdraw
import time
import creature
import genetics
import numpy as np
import utility
import ray
import math

pygame.init()
width = 1120
height = 630
screen = pygame.display.set_mode((width,height))
number_of_creatures = 10
creatures = []

number_sensors_per_creature = 10
current_angle = 0
sensor_length = 50
delta_angle = 2*math.pi / number_sensors_per_creature
for i in range(number_of_creatures):
    current_angle = 0
    sensors = []
    for j in range(number_sensors_per_creature):
        current_angle += delta_angle
        sensors.append(ray.ray(np.array([0.0, 0.0]), np.array([sensor_length * math.cos(current_angle), sensor_length * math.sin(current_angle)]), [100, 100, 100]))
    creatures.append(creature.Creature(np.array([500.0, 500.0]), 10, (250, 250, 10), (0, 0, 0), [number_sensors_per_creature, 2, 3, 1],
                     sensors))
number_of_steps_per_episode = 40

"""
x = 300
y = 250
width = 20 height = 30
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
skip = 10

while True:
  step += 1
  if step > 100000:
      break;

  utility.step_creatures(creatures, width, height);

  #for creature in creatures:
    #  creature.step(np.array([[1],[1],[1]]), width, height)

  if step % number_of_steps_per_episode == 0:
    print("epoch")
    creatures = genetics.crossover_mutate(creatures, 0.005)
    for c in creatures:
      print(c.life)
      c.life = 0

  screen.fill([180, 180, 180])
  for creature in creatures:
    creature.draw(screen)

  pygame.display.update()

print(step)
for c in creatures:
  print(c.weights)
