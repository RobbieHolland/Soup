""" Creature class """

import pygame
import pygame.gfxdraw
import random as rd
import numpy as np

class Creature:
    creature_count = 0

    def __init__(self, width, height, radius, colour, weights):

        # Characteristics
        self.life = 0
        self.x = rd.randint(width-height,height-radius)
        self.y = rd.randint(width-height,height-radius)
        self.radius = radius
        self.colour = colour

        # Genome
        self.weights = np.

        creature_count += 1
        
    def draw(self, creature, screen):
        x = creature.x
        y = creature.y
        radius = creature.radius
        colour = creature.colour
        pygame.gfxdraw.filled_circle(screen, x, y, radius, colour)
        pygame.gfxdraw.aacircle(screen, x, y, radius, colour)

    def get_count(self):
        return Creature.creature_count
    
