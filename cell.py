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
        # [left, top, bottom, right]
        # self.edges = []

    # Sets self.edges to represent which neighboring cells are not flooded
    # def setEdges(self, grid):
    #     self.edges = []
    #     for i in range(-1, 2):
    #         for j in range(-1, 2):
    #             a = self.i + i
    #             b = self.j + j
    #             if abs(i) + abs(j) == 1:
    #                 if not(a >= 0 and a < boardSize and b >= 0 and b < boardSize):
    #                     self.edges.append(False)
    #                 else:
    #                     if not grid[a][b].flooded:
    #                         self.edges.append(False)
    #                     else:
    #                         self.edges.append(True)

    # Draws cell
    def draw(self, window, grid):
        rect(window, self.color, (self.x, self.y, self.w, self.w))

        if not self.flooded:
            rect(window, black, (self.x, self.y, self.w, self.w), 1)

        # # Left edge
        # if self.edges[0]:
        #     line(window, black, (self.x, self.y), (self.x, self.y + self.w), 1)
        # # Top edge
        # if self.edges[1]:
        #     line(window, black, (self.x, self.y), (self.x + self.w, self.y), 1)
        # # Bottom edge
        # if self.edges[2]:
        #     line(window, black, (self.x, self.y + self.w), (self.x + self.w, self.y + self.w), 1)
        # # Right edge
        # if self.edges[3]:
        #     line(window, black, (self.x, self.y + self.w), (self.x + self.w, self.y + self.w), 1)

    def has(self, mousePos):
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        return (mouseX > self.x and mouseX < self.x + self.w and
                mouseY > self.y and mouseY < self.y + self.w)

    # Floods correct cells with picked color
    def flood(self, colorpicked, grid):
        self.color = colorpicked
        for i in range(-1, 2):
            for j in range(-1, 2):
                a = self.i + i
                b = self.j + j
                if (abs(i) + abs(j) == 1 and a >= 0 and a < boardSize
                                         and b >= 0 and b < boardSize):
                    cell = grid[a][b]
                    if cell.color == colorpicked and not cell.flooded:
                        cell.flooded = True
                        cell.flood(colorpicked, grid)
