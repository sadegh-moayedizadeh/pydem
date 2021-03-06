"""module that contains tools to illustrate simulations
"""


import sys
import os
import pygame
from geometry import two_dimensional_entities as shapes
from geometry import two_dimensional_operations as operations
from generation.container import Container
from generation.particles import Sand, Clay
import numpy as np
from typing import Type, Union, Tuple, List, Set, Dict, Any
import pathlib
from matplotlib.patches import Rectangle, Circle
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D


class IllustrationPG(object):
    """class to illustrate the DEM simulation using the "pygame"
    libarary package
    """
    
    clay_color = (161, 93, 93)
    sand_color = (75, 204, 112)
    container_color = (163, 250, 255)
    wall_color = (28, 30, 31)
    background_color = (86, 96, 97)
    
    def __init__(self, container):
        """initializes the illustration instace
        """
        
        self.container = container
    
    def _convert_x(self, x: float) -> float:
        """converts the given x coordinate to a value that fits into
        the illustrated container
        """

        return (0.025) * (self.container.length) + (x) * (0.1)
    
    def _convert_y(self, y: float) -> float:
        """converts the given y coordinate to a value that fits into
        the illustrated container
        """

        return ((0.025) * (self.container.width)) + ((0.15) * (self.container.width) - (y) * (0.1))
    
    def set_shapes(self, screen):
        """sets up the shapes to be displayed
        """
        
        for wall in self.container.walls:
            pygame.draw.line(
                screen,
                self.wall_color,
                (self._convert_x(wall.shape.end1.x), self._convert_y(wall.shape.end1.y)),
                (self._convert_x(wall.shape.end2.x), self._convert_y(wall.shape.end2.y)),
                width = 5,
            )
        for particle in self.container.particles:
            if isinstance(particle, Clay):
                pygame.draw.line(
                    screen,
                    self.clay_color,
                    (self._convert_x(particle.midline.end1.x), self._convert_y(particle.midline.end1.y)),
                    (self._convert_x(particle.midline.end2.x), self._convert_y(particle.midline.end2.y)),
                    particle.thickness,
                    )
            elif isinstance(particle, Sand):
                pygame.draw.circle(
                    screen,
                    self.sand_color,
                    (self._convert_x(particle.center.x), self._convert_y(particle.center.y)),
                    paritcle.radius * 0.1
                )
    
    def display(self):
        """displays the illustraion
        """
        
        pygame.init()
        screen = pygame.display.set_mode((int(0.15*self.container.length), int(0.15*self.container.width))) #fix sizes
        screen.fill(self.background_color)
        container_surface = pygame.Surface([self.container.length//10, self.container.width//10])
        container_surface.fill(self.container_color)
        screen.blit(container_surface, (int(0.025*self.container.length), int(0.025*self.container.width)))
        
        pygame.display.set_caption('2D DEM simulation of tiaxial test on sand-clay mixtures')
        # font = pygame.font.Font('CrimsonText-Regular.ttf', 32)
        # text = font.render('GeeksForGeeks', True, self.sand_color, self.sand_color)
        # textRect = text.get_rect()
        # textRect.center = (750, 100)
        # image = pygame.image.load('ut_logo.png')
        
        self.set_shapes(screen)
        done = False
        while done is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


class IllustrationMPL(object):
    """class to illustrate the DEM simulation using the "matplotlib"
    libarary package
    """
    
    def __init__(self, container, title=None):
        """initialize the illustration instance
        """
        
        self.container = container
        self.scale = self.container.length / 1000
        if title is None:
            self.title = '2D DEM simulation of tiaxial test on sand-clay mixtures'
        else:
            self.title = title
    
    def _convert_x(self, x):
        """converts the x coordinate of the given entity in a way that
        fits into the container illustration created by this class
        """

        return (x/self.scale + 250)

    def _convert_y(self, y):
        """converts the x coordinate of the given entity in a way that
        fits into the container illustration created by this class
        """
        
        return (y/self.scale + 250)
    
    def set_shapes(self):
        """sets up the shapes of the all the particles and boundaries
        in the model
        """
        
        for particle in self.container.particles:
            if isinstance(particle, Sand):
                shape = Circle(
                    (self._convert_x(particle.shape.center.x), self._convert_y(particle.shape.center.y)),
                    particle.shape.radius / 100,
                    color = 'green',
                    )
                plt.gca().add_patch(shape)
            if isinstance(particle, Clay):
                x0 = self._convert_x(particle.midline.end1.x)
                y0 = self._convert_y(particle.midline.end1.y)
                x1 = self._convert_x(particle.midline.end2.x)
                x = np.arange(x0, x1, .01)
                m = particle.midline.slope
                plt.plot(x, m*(x-x0)+y0, color='red')
    
    def display(self):
        """displays the illustration of the DEM model
        """

        plt.title(self.title)
        
        #set the size of display window
        x = np.arange(0, 1500, 1)
        y = 0.01*x
        plt.plot(x, y, color = 'white')
        x = np.arange(0, 1500, 1)
        y = 0.01*x + 1485
        plt.plot(x, y, color = 'white')

        #draw the container rectangle
        rect = Rectangle((250, 250), 1000, 1000, fill = False)
        plt.gca().add_patch(rect)
        
        self.set_shapes()
        
        plt.show()
