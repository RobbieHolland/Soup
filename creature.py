""" Creature class """

import pygame
import pygame.gfxdraw
import random as rd
import numpy as np
import math

class Creature:
    # All creatures move at a constant speed
    velocity = 1
    max_turn = 0.1

    def __init__(self, x, y, radius, colour, inputs, hidden, output):
        """
        @param colour
        """

        # Characteristics
        self.life = 10000
        self.x = x
        self.y = y 
        self.radius = radius
        self.colour = colour
        self.angle = rd.rand()
        

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

    def get_angle(self, inputs):
        # Apply weights to inputs to get (output == angle)
        res = inputs
        for weight in weights:
            res = np.mat(weight)* np.mat(inputs)
        return res

    def step(self, width, height):self
        alpha = self.get_angle()
        self.x += Creature.velocity * math.cos(alpha) * max_turn
        self.y += Creature.velocity * math.sin(alpha) * max_turn
        
        
    

if __name__ == '__main__':
    print("Test Compilation")
    c = Creature(1,1,1,1,3,1,1)
    print(c.weights)
