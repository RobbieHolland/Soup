""" Group of useful funcitons """
import creature
import ray
import numpy as np
from math import *

def reduce_life(creatures):
    for i in range(len(creatures)):
        for j in range(i+1, len(creatures)):
            a, b = creatures[i], creatures[j]
            if dist(a, b) < (a.radius + b.radius):
                head.life -= 1
                t.life -= 1

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def ray_creature_intersect(ray, creature):
    new_point1 = ray.point1 - creature.position;
    new_point2 = ray.point2 - creature.position;
    determinant = new_point1[0] * new_point2[1] - new_point2[0] * new_point1[1]

    discriminant = creature.radius**2 * ray.length**2 - determinant**2
    detection = discriminant >= 0

    detection &= dist(ray.point1, creature.position) < ray.length
    detection &= dist(ray.point2, creature.position) < ray.length
    return detection

#hack
sensor_len = 50.0
def step_creatures(creatures, width, height):
    for i in range(len(creatures)):
        # Convolutional next
        sensory_input = np.zeros((len(creatures)*2, 1))
        for j in range(len(creatures)):
            if i == j: continue
            sensory_input[j*2][0] = min(1, dist(creatures[i].position, creatures[j].position)) / sensor_len
            rel_vec = creatures[j].position - creatures[i].position
            sensory_input[j*2+1][0] = (np.arctan2(rel_vec[1], rel_vec[0]) + pi) / (2*pi)
        creatures[i].step(sensory_input, width, height);

"""
    for i in range(len(creatures)):
        sensory_input = np.zeros((len(creatures[i].sensors), 1))
        for j in range(len(creatures)):
            if (i != j):
                for k in range(len(creatures[i].sensors)):
                    creatures[i].sensors[k].detecting = False
                    sensory_input[k][0] = int(ray_creature_intersect(creatures[i].sensors[k], creatures[j]))
                    if (sensory_input[k][0]):
                        creatures[i].sensors[k].detecting = True
                # print(sensory_input)
        creatures[i].step(sensory_input, width, height);
"""
