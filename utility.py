""" Group of useful funcitons """
import creature.py
import ray.py
import intersection.py

def reduce_life(creatures):
    for i in range(len(creatures)):
        for j in range(i+1, len(creatures)):
            a, b = creatures[i], creatures[j]
            if dist(a, b) < (a.radius + b.radius):
                head.life -= 1
                t.life -= 1

def dist(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def ray_creature_intersect(ray, creature):
    intersection = creature.radius**2 * ray.length**2 - ray.point1[0]