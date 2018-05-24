import pygame
from pygame.draw import *
from constants import *


class Button:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def has(self, mousePos):
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        return (mouseX > self.x and mouseX < self.x + self.w and
                mouseY > self.y and mouseY < self.y + self.w)


class PickColor(Button):
    def __init__(self, x, y, w, color):
        Button.__init__(self, x, y, w)
        self.color = color

    def draw(self, window):
        rect(window, self.color, (self.x, self.y, self.w, self.w))
