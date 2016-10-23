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

    def __init__(self, x, y, radius, colour, config):
        """
        @param colour
        """

        # Characteristics
        self.life = 0
        self.positive_life = 0
        self.x = x
        self.y = y 
        self.radius = radius
        self.colour = colour
        self.angle = rd.uniform(0, 1)
        self.scale = 0

        # Genome
        self.weights = self.create_weights(config)

    def create_weights(self, config):
        mat_list = []
        for i in range(len(config)-1):
            mat_list.append(np.random.rand(config[i+1], config[i]))
        return mat_list
        
    def draw(self, screen):
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.radius, self.colour)
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.colour)

    def get_count(self):
        return Creature.creature_count

    def get_angle(self, inputs):
        # Apply weights to inputs to get (output == angle)
        for weight in self.weights:
            inputs = np.array(np.mat(weight)* np.mat(inputs)) 
            inputs = inputs - len(inputs)/4
            inputs = self.sigmoid(inputs)
        return inputs

    def sigmoid(self, x):
        return 1 / (1 + math.e**(-x))

    def step(self, inputs, width, height):
        # print(self.get_angle(inputs), "angle", self.angle, "adding", Creature.max_turn * (self.get_angle(inputs) - 0.5))
        self.life += self.get_angle(inputs)[0][0] - 0.5
        self.angle += Creature.max_turn * (self.get_angle(inputs)[0][0] - 0.5)
        self.x += Creature.velocity * math.cos(self.angle)
        self.x = max(min(self.x, width), 0)
        self.y += Creature.velocity * math.sin(self.angle)
        self.y = max(min(self.y, height), 0)
    

if __name__ == '__main__':
    print("Test Compilation")
    c = Creature(1,1,1,1,[2,3,2,1])
    print(c.weights)
    print(np.random.rand(2, 1))
    print(c.get_angle(np.random.rand(2,1))[0][0])
    
