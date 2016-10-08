""" Creature class """

import pygame
import pygame.gfxdraw
import random as rd
import numpy as np

class Creature:
    def __init__(self, x, y, radius, colour, inputs, hidden, output):
        """
        @param colour
        """

        # Characteristics
        self.life = 10000
        self.positive_life = 0
        self.x = x
        self.y = y 
        self.radius = radius
        self.colour = colour
        self.scale = 0

        # Genome
        self.weights = self.create_weights(inputs, hidden, output)

    def create_weights(self, inputs, hidden, output):
        mat_list = [np.random.rand(inputs, inputs) for _ in range(hidden)]
        mat_list.append(np.random.rand(output, inputs))
        return np.array(mat_list)
        
    def draw(self, screen):
        pygame.gfxdraw.filled_circle(screen, self.x, self.y, self.radius, self.colour)
        pygame.gfxdraw.aacircle(screen, self.x, self.y, self.radius, self.colour)

    def get_count(self):
        return Creature.creature_count
    

if __name__ == '__main__':
    print("Test Compilation")
    c = Creature(1,1,1,1,3,1,1)
    print(c.weights)
