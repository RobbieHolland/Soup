import utility
import pygame

class ray:
    def __init__(self, point1, point2, colour):
        self.colour = colour
        self.point1 = point1
        self.point2 = point2
        self.length = utility.dist(point1, point2)
        self.determinant = point1[0]*point2[1] - point1[1]*point2[0]

    def draw(self, screen):
        #Using aatrigon for now; can't find aaline
        pygame.gfxdraw.aatrigon(screen, int(self.point1[0]), int(self.point1[1]), int(self.point2[0]), int(self.point2[1]), int(self.point2[0]), int(self.point2[1]), self.colour)
