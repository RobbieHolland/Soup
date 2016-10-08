""" Creature class """

import pygame
import pygame.gfxdraw
import random as rd
import numpy as np
import math

class Creature:
    # All creatures move at a constant speed
    velocity = 0.5
    max_turn = 0.5

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
        self.angle = rd.uniform(0, 1)
        self.scale = 0
        self.outputs = output

        # Genome
        self.weights = self.create_weights(inputs, hidden, output)

    def create_weights(self, inputs, hidden, output):
        mat_list = [np.random.rand(inputs, inputs) for _ in range(hidden)]
        mat_list.append(np.random.rand(output, inputs))
        return np.array(mat_list)
        
    def draw(self, screen):
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.radius, self.colour)
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.colour)

    def get_count(self):
        return Creature.creature_count

    def get_angle(self, inputs):
        # Apply weights to inputs to get (output == angle)
        res = inputs
        for weight in self.weights:
            res = np.mat(weight)* np.mat(inputs) / len(inputs)
        return res / len(inputs)

    def step(self, inputs, width, height):
        print(self.get_angle(inputs), "angle", self.angle, "adding", Creature.max_turn * (self.get_angle(inputs) - 0.05))
        self.angle += Creature.max_turn * (self.get_angle(inputs) - 0.5 * Creature.max_turn)
        self.x += Creature.velocity * math.cos(self.angle)
        self.x = max(min(self.x, width), 0)
        self.y += Creature.velocity * math.sin(self.angle)
        self.y = max(min(self.y, height), 0)
    

if __name__ == '__main__':
    print("Test Compilation")
    c = Creature(1,1,1,1,3,1,1)
    print(c.weights)
