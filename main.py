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
# from pylab import *

width = 300
height = 300
number_of_steps_per_episode = 1000
number_of_episodes = 20
total_learning_steps = number_of_episodes * number_of_steps_per_episode
show_display = True
screen = pygame.display.set_mode((width,height))
number_of_creatures = 10
creatures = []
number_sensors_per_creature = 2 * number_of_creatures
current_angle = 0
sensor_length = 100


delta_angle = 2*math.pi / number_sensors_per_creature
for i in range(number_of_creatures):
    current_angle = 0
    sensors = []
    for j in range(number_sensors_per_creature):
        current_angle += delta_angle
        sensors.append(ray.ray(np.array([0.0, 0.0]), sensor_length, current_angle, [100, 100, 100]))
    creatures.append(creature.Creature(np.array([500.0, 500.0]), 10, (250, 250, 10), (0, 0, 0), [number_sensors_per_creature, 2, 3, 1],
                     sensors))
    creatures[i].random_relocate(width, height)


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

if show_display:
    pygame.init()

print('Evolution starting')
step = 0
start = time.clock()
skip = 10
average_scores = []

while True:
  step += 1
  if step > total_learning_steps:
      break;

  utility.step_creatures(creatures, width, height);

  #for creature in creatures:
    #  creature.step(np.array([[1],[1],[1]]), width, height)

  if step % number_of_steps_per_episode == 0:
    print("epoch")
    creatures = genetics.crossover_mutate(creatures, 0.005)
    print("Best fitness: " + str(creatures[number_of_creatures - 1].life))
    median_fitness = creatures[int(number_of_creatures / 2)].life
    average_fitness = 0;
    for c in creatures:
      average_fitness += c.life
      print(c.life)
      c.random_relocate(width, height)
      c.life = 0
    creatures[0].position[1] = 100
    average_fitness /= number_of_creatures
    average_scores.append(average_fitness)

    print("Average fitness: " + str(average_fitness))
    print("Median fitness: " + str(median_fitness))

  if show_display:
      screen.fill([180, 180, 180])
      for creature in creatures:
        creature.draw(screen)
      pygame.display.update()

print(step)
for c in creatures:
  print(c.weights)

print(average_scores)
