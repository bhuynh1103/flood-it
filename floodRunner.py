import pygame, sys
from pygame.locals import *
from constants import *
from cell import *
from button import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize + HUDsize))

grid = []
for i in range(boardSize):
    grid.append([])
    for j in range(boardSize):
        clr = color[randint(0, numberOfColors - 1)]
        grid[i].append(Cell(i, j, clr))


PickColorButtons = []
for x in range(numberOfColors):
    buttonWidth = 50
    PickColorButtons.append(PickColor((x * buttonWidth) + (buttonWidth // 2) + (x * 10), HUDsize // 2 - buttonWidth // 2, buttonWidth, color[x]))

grid[0][0].flooded = True

leftClicked = False
colorpicked = None

while True:
    screen.fill(gray(200))

    mousePos = pygame.mouse.get_pos()

    for i in range(boardSize):
        for j in range(boardSize):
            cell = grid[i][j]

            # if cell.has(mousePos) and leftClicked:
            #     cell.flood()
            #     print(cell.i, cell.j, "clicked")

            if cell.flooded and colorpicked != None:
                cell.flood(colorpicked, grid)

            if cell.has(mousePos) and leftClicked:
                print(cell.flooded)

            cell.draw(screen)

            # if cell.has(mousePos) and leftClicked:
            #     print(cell.flooded)


    for button in PickColorButtons:
        button.draw(screen)

        if button.has(mousePos) and leftClicked:
            colorpicked = button.color
        elif not leftClicked:
            colorpicked = None

        # print(colorpicked)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        mouseStates = pygame.mouse.get_pressed()

        # Left-clicked
        if event.type == MOUSEBUTTONDOWN and mouseStates[0] == 1:
            leftClicked = True
        else:
            leftClicked = False
