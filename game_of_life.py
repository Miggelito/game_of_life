"""
GAME OF LIFE

Syntax inspired and started from 
http://programarcadegames.com/index.php?chapter=array_backed_grids


"""
import pygame
 
# Define Dead and Alive cells
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
 
# This sets the WIDTH, HEIGHT and MARGIN (thickness of border) of each grid
WIDTH = 10
HEIGHT = 10
MARGIN = 1

# How many ROWs and COLumns and in the world
ROW = 100
COL = 100



 
# Create a 2 dimensional array. A two dimensional
# array is a list of lists.
def generateEmptyGrid(ROW, COL):
    """
    Create a 2 dimensional array. A two dimensional
    array is a list of lists.
    Input:
        - ROWs
        - COLumns
    Returns:
        - Empty grid (only dead cells) of size ROW x COL
    """
    grid = []
    for row in range(ROW):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(COL):
            grid[row].append(0)  # Append a cell
    return grid
            
# Generate Starting grid
grid = generateEmptyGrid(ROW,COL)
 
# Insert some patterns

# Glider
grid[54][60] = 1
grid[55][61] = 1
grid[56][61] = 1
grid[56][60] = 1
grid[56][59] = 1

# Tub
grid[9][4] = 1
grid[10][5] = 1
grid[10][3] = 1
grid[11][4] = 1

# Blinker
grid[24][25] = 1
grid[25][25] = 1
grid[26][25] = 1

def torusConversion(i,j,ROW,COL):
    if i < 1 and j < 1:
        return ROW, COL
    elif i >= 1 and j < 1:
        return i, COL
    elif i < 1 and j >= 1:
        return ROW, j
    elif i > ROW - 1 and j > COL - 1:
        return 0, 0
    elif i > ROW - 1 and j <= COL - 1:
        return 0, j
    elif i <= ROW - 1 and j > COL - 1:
        return i, 0
    else:
        return i, j


def gridUpdate(grid):
    """
    Updates grid, by iterating over all cells in world.
    Uses Conway's rules from the Game Of Life.
    Input:
        - Old Grid
    Returns:
        - Updated Grid
    """
    nROW = len(grid)
    nCOL = len(grid[0])
    nextGrid = generateEmptyGrid(nROW,nCOL)    
    for i in range(1,nROW-1):
        for j in range(1,nCOL-1):
            N = grid[i-1][j]
            NE = grid[i-1][j+1]
            E = grid[i][j+1]
            SE = grid[i+1][j+1]
            S = grid[i+1][j]
            SW = grid[i+1][j-1]
            W = grid[i][j-1]
            NW = grid[i-1][j-1]
            # Sums the number of neighbours
            neighbours = N+NE+E+SE+S+SW+W+NW
            if grid[i][j] == 1 and neighbours < 2:
                nextGrid[i][j] = 0
            elif grid[i][j] == 1 and (neighbours == 2 or neighbours == 3):
                nextGrid[i][j] = 1
            elif grid[i][j] == 1 and neighbours > 3:
                nextGrid[i][j] = 0
            elif grid[i][j] == 0 and neighbours == 3:
                nextGrid[i][j] = 1
    return nextGrid

 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [ROW*(WIDTH + MARGIN) + MARGIN, COL*(HEIGHT + MARGIN) + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Conway's GAME OF LIFE")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    grid = gridUpdate(grid)
    for event in pygame.event.get():  # User Interaction
        if event.type == pygame.QUIT:  # User termination of program
            done = True  # Exit loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Toggle location to one or zero depending on previous status
            if grid[row][column] == 0:
                grid[row][column] = 1
            elif grid[row][column] == 1:
                grid[row][column] = 0
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(ROW):
        for column in range(COL):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(30)
 
    # Update screen
    pygame.display.flip()
        
		
    
 
# Quit program
pygame.quit()