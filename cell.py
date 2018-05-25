import pygame
from pygame.draw import *
from constants import *


class Cell:
    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.w = screenSize // boardSize
        self.x = i * self.w
        self.y = j * self.w + HUDsize
        self.color = color
        self.flooded = False

    def draw(self, window):
        rect(window, self.color, (self.x, self.y, self.w, self.w))

    def has(self, mousePos):
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        return (mouseX > self.x and mouseX < self.x + self.w and
                mouseY > self.y and mouseY < self.y + self.w)

    def flood(self, colorpicked, grid):
        self.color = colorpicked
        for i in range(-1, 2):
            for j in range(-1, 2):
                a = self.i + i
                b = self.j + j
                if abs(i) + abs(j) == 1 and (a >= 0 and a < boardSize and b >= 0 and b < boardSize):
                    cell = grid[a][b]
                    if cell.color == colorpicked and not cell.flooded:
                        cell.flooded = True
                        cell.flood(colorpicked, grid)
                        # print("flood")
