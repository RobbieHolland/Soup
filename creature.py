""" Creature class """

import pygame
import pygame.gfxdraw
import random as rd
import numpy as np
import math

class Creature:
    # All creatures move at a constant speed
    velocity = 1
    max_turn = 0.5

    def __init__(self, position, radius, colour1, colour2, config, sensors):
        """
        @param colour
        """

        # Characteristics
        self.life = 0
        self.positive_life = 0
        self.position = position
        self.radius = radius
        self.colour1 = colour1
        self.colour2 = colour2
        self.angle = rd.uniform(0, 1)
        self.scale = 0
        self.sensors = sensors;

        # Genome
        self.weights = self.create_weights(config)

    def create_weights(self, config):
        mat_list = []
        for i in range(len(config)-1):
            mat_list.append(np.random.rand(config[i+1], config[i]))
        return mat_list

    def draw(self, screen):
        for sensor in self.sensors:
            sensor.draw(screen)

        pygame.gfxdraw.filled_circle(screen, int(self.position[0]), int(self.position[1]), self.radius, self.colour1)
        pygame.gfxdraw.aacircle(screen, int(self.position[0]), int(self.position[1]), self.radius, self.colour2)

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
        self.life -= inputs.sum()

        self.angle += Creature.max_turn * (self.get_angle(inputs)[0][0] - 0.5)
        self.position[0] += Creature.velocity * math.cos(self.angle)
        self.position[0] = max(min(self.position[0], width), 0)
        self.position[1] += Creature.velocity * math.sin(self.angle)
        self.position[1] = max(min(self.position[1], height), 0)
        
        for sensor in self.sensors:
            sensor.point1 = self.position
            sensor.set_point2(sensor.angle + self.angle)

    def random_relocate(self, width, height):
        self.position = np.random.rand(2)
        self.position[0] *= width
        self.position[1] *= height


if __name__ == '__main__':
    print("Test Compilation")
    c = Creature(1,1,1,1,[2,3,2,1])
    print(c.weights)
    print(np.random.rand(2, 1))
    print(c.get_angle(np.random.rand(2,1))[0][0])
