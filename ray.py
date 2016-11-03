import utility
import pygame
import numpy as np
import math

class ray:
    """
    def __init__(self, point1, point2, colour):
        self.colour = colour
        self.point1 = point1
        self.point2 = point2
        self.length = utility.dist(point1, point2)
        self.dr = point2 - point1
        self.determinant = point1[0]*point2[1] - point1[1]*point2[0]
    """

    def set_point2(self, angle):
        self.point2 = self.point1 + np.array([self.length * math.cos(angle), self.length * math.sin(angle)])
        self.dr = self.point2 - self.point1

    def __init__(self, point1, length, angle, colour):
        self.colour = colour
        self.length = length
        self.angle = angle
        self.point1 = point1
        self.set_point2(self.angle)
        self.detecting = False
        self.detecting_colour = [255, 0, 0]

    def draw(self, screen):
        colour = self.colour;
        if self.detecting:
            colour = self.detecting_colour
        pygame.draw.line(screen, colour, (int(self.point1[0]), int(self.point1[1])), (int(self.point2[0]), int(self.point2[1])))
