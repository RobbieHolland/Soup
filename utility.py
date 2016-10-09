""" Group of useful funcitons """
import creature
import ray

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
    discriminant = creature.radius**2 * ray.length**2 - ray.determinant**2
    detection = discriminant >= 0
    return detection
