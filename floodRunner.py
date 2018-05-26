import pygame, sys
from pygame.locals import *
from constants import *
from cell import *
from button import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize + HUDsize))

def winCondition(grid):
    for i in range(boardSize):
        for j in range(boardSize):
            cell = grid[i][j]
            if cell.color != colorpicked:
                return False
    return True

while True:
    # Generates all squares with a random color each
    grid = []
    for i in range(boardSize):
        grid.append([])
        for j in range(boardSize):
            clr = color[randint(0, numberOfColors - 1)]
            grid[i].append(Cell(i, j, clr))

    # Creates the pick color buttons
    PickColorButtons = []
    for x in range(numberOfColors):
        buttonWidth = HUDsize * .66
        PickColorButtons.append(PickColor((x * buttonWidth) + (buttonWidth // 2) +
                (x * 10), HUDsize // 2 - buttonWidth // 2, buttonWidth, color[x]))

    # Starts the game off in the top left corner
    topleft = grid[0][0]
    topleft.flooded = True
    topleft.flood(topleft.color, grid)

    # Game control variables
    moves = 0
    leftClicked = False
    colorpicked = None

    Gameover = False
    setup = False

    while not setup:
        # Game loop
        while not Gameover:
            screen.fill(gray(200))
            mousePos = pygame.mouse.get_pos()

            # Draws board
            for i in range(boardSize):
                for j in range(boardSize):
                    cell = grid[i][j]

                    # cell.setEdges(grid)

                    # Updates resepective squares whenever a color is picked
                    if cell.flooded and colorpicked != None:
                        cell.flood(colorpicked, grid)

                    # Debug tool
                    if cell.has(mousePos) and leftClicked:
                        print(cell.edges)

                    cell.draw(screen, grid)

            # HUD

            # A good part of the way though writing the game I realized the
            # "HUD" wasn't really a HUD it's really like a GUI but I'm too lazy
            # to refactor everything from HUD to GUI

            for button in PickColorButtons:
                button.draw(screen)

                # Sets 'colorpicked' to the color of the button clicked, sets to None if no button is clicked
                if button.has(mousePos) and leftClicked and colorpicked != button.color:
                    colorpicked = button.color
                    moves += 1
                elif not leftClicked:
                    colorpicked = None

            # Writes number of moves, auto formats (that's why this is really long)
            writeText(screen, "Moves: " + str(moves), black, PickColorButtons[numberOfColors - 1].x +
            PickColorButtons[numberOfColors - 1].w + ((screenSize - (PickColorButtons[numberOfColors - 1].x +
            PickColorButtons[numberOfColors - 1].w)) // 2), HUDsize // 2, HUDsize * .66)

            if winCondition(grid):
                Gameover = True

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

        # Gameover loop
        screen.fill(gray(200))
        for i in range(boardSize):
            for j in range(boardSize):
                grid[i][j].draw(screen, grid)

        # Draws message banner
        pygame.draw.rect(screen, white, (0, ((screenSize // 2) + HUDsize) - HUDsize * .5, screenSize, HUDsize))

        writeText(screen, "You Won! Press 'ENTER' to play again", black,
                screenSize // 2, screenSize // 2 + HUDsize, HUDsize * .5)

        # Control of constants in game within HUD to be added

        writeText(screen, "Moves: " + str(moves), black, PickColorButtons[numberOfColors - 1].x +
        PickColorButtons[numberOfColors - 1].w + ((screenSize - (PickColorButtons[numberOfColors - 1].x +
        PickColorButtons[numberOfColors - 1].w)) // 2), HUDsize // 2, HUDsize * .66)

        pygame.display.update()

        # Input loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                setup = True

            # Left-clicked
            if event.type == MOUSEBUTTONDOWN and mouseStates[0] == 1:
                leftClicked = True
            else:
                leftClicked = False
