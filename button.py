import pygame
from pygame.draw import *
import constants


# Button class holds standard methods all buttons should have so that the methods are inherited
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

# Button for picking colors
class PickColor(Button):
    def __init__(self, x, y, w, color):
        Button.__init__(self, x, y, w)
        self.color = color

    def draw(self, window):
        rect(window, self.color, (self.x, self.y, self.w, self.w))


# Ended up not using this class but its has potential, doesn't work yet
'''
class Scroller:
    def __init__(self, leftX, rightX, y, w, name):
        self.leftX = leftX
        self.rightX = rightX
        self.x = leftX + (rightX - leftX) // 2
        self.y = y
        self.w = w
        self.show = False
        self.name = name

    def draw(self, window):
        if self.show:
            line(window, black, (self.leftX, self.y), (self.rightX, self.y))
            ellipse(window, gray(50), (self.x - self.w // 2, self.y - self.w // 2, self.w, self.w))
            writeText(window, self.name, black, self.leftX + (self.rightX - self.leftX) // 2, self.y - self.w, self.w)

    def has(self, mousePos):
        if self.show:
            mouseX = mousePos[0]
            mouseY = mousePos[1]
            return (mouseX > self.x - self.w // 2 and mouseX < self.x - self.w // 2 + self.w and
                    mouseY > self.y - self.w // 2 and mouseY < self.y + self.w - self.w // 2)

    def scroll(self, mousePos, clicked):
        if self.has(mousePos):
            if mousePos[0] < self.leftX:
                self.x = self.leftX
            elif mousePos[0] > self.rightX:
                self.x = self.rightX
            else:
                self.x = mousePos[0]

            print(self.x, mousePos[0])
'''
