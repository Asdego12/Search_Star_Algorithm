from MySearchStar import *

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Grid specs
WIDTH = 80
HEIGHT = 80
MARGIN = 5

# Define grid
grid = [[0 for x in range(7)] for y in range(5)]

# Initializes pygame
pygame.init()

# Sets the HEIGHT, WIDTH, TITLE of the screen
WINDOW_SIZE = [600, 430]
screen = pygame.display.set_mode(WINDOW_SIZE)
# Font size
font = pygame.font.SysFont('Calibri', 20, bold=1)
pygame.display.set_caption("A* Search Algorithm")

# Loop until close button clicked
done = False

# Screen update
clock = pygame.time.Clock()

# Screen background
screen.fill(BLACK)
# Screen range
for row in range(5):
    for column in range(7):
        color = WHITE  # Default
        tile = pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
        grid[row][column] = MySearchStar(tile, 0, position=(row, column))

# Specifies the RED tiles
grid[0][1].colorfill = 1
grid[2][1].colorfill = 1
grid[2][3].colorfill = 1
grid[3][1].colorfill = 1
grid[3][4].colorfill = 1
grid[4][4].colorfill = 1


grid[0][6].colorfill = 1
grid[1][6].colorfill = 1
grid[2][6].colorfill = 1
grid[3][6].colorfill = 1


target_node = grid[4][6]


# Colour WHITE
for row in range(5):
    for column in range(7):
        color = WHITE

        # Colour RED
        if grid[row][column].colorfill == 1:
            color = RED
        pygame.draw.rect(screen, color, grid[row][column].rect)

# Prints Start and End
screen.blit(font.render("START", True, BLACK), (19, 36))
screen.blit(font.render("END", True, BLACK), (452, 380))

# Updates the screen
pygame.display.update()

reRun = False

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not reRun:
                reRun = True
                print(astar(grid, grid[0][0], target_node, screen))

# Quits the program
pygame.quit()
