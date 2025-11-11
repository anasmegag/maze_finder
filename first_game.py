# Importing pygame module
import pygame
from pygame.locals import *
import solution
from random import randint
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Grid Maze Editor")

# Define colors and constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) # Obstacles
START_COLOR = (0, 200, 0) # Green
END_COLOR = (200, 0, 0)   # Red
GRID_SIZE = 30
SQUARE_SIZE = (GRID_SIZE, GRID_SIZE)

     
# Function to snap coordinates to the nearest grid top-left corner
def get_accurate_position(position):
    x = position[0]
    y = position[1]
    # Use floor division // to snap down to the nearest multiple of GRID_SIZE
    return (x // GRID_SIZE * GRID_SIZE, y // GRID_SIZE * GRID_SIZE)

# creating list in which we will store the position of the square's top-left corner
squares_positions = []

def random_maze():
    for i in range(200):
         squares_positions.append(get_accurate_position((randint(3,900),randint(3,600))))
# Define special squares: (x, y) coordinates
starting_position = (0, 0) # Top-left corner
ending_position = (WINDOW_WIDTH - GRID_SIZE, WINDOW_HEIGHT - GRID_SIZE) # Bottom-right corner

# Creating a variable which we will use to run the while loop
run = True
pt =[]
# Creating a while loop
while run:
    # --- 1. EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        # If mouse button is pressed
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos 
            snapped_pos = get_accurate_position(position)
            # Prevent interaction with Start/End squares
            if snapped_pos == starting_position or snapped_pos == ending_position:
                continue
            # Toggle the square (Add or Remove)
            if snapped_pos in squares_positions:
                squares_positions.remove(snapped_pos)
            else:
                squares_positions.append(snapped_pos)
       
            
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_r:
                random_maze()
            elif event.key == pygame.K_f:
                print('hi')
                sol = solution.Solution(squares_positions)
                so= sol.getPath()
                print(so)
                if so is not None:
                        pt = so
                else:
                        pt = []
        



            
    # --- 2. DRAWING (Inside the loop to refresh the screen) ---
    
    # Clear the screen (Erase previous frame)
    window.fill(WHITE) 
    
    # Draw all obstacle squares (black)
    for position in squares_positions:
        # Create the Rect argument: (x, y, width, height)
        rect_to_draw = (position[0], position[1], SQUARE_SIZE[0], SQUARE_SIZE[1])
        pygame.draw.rect(window, BLACK, rect_to_draw)
    for s in pt:
        x = (s % 30) * GRID_SIZE
        y = (s // 30) * GRID_SIZE
        pygame.draw.rect(window, (100, 200, 200), (x, y, GRID_SIZE, GRID_SIZE))
        
    # Draw the Starting Square (Green)
    start_rect = starting_position + SQUARE_SIZE # Concatenates (0,0) with (30,30) -> (0,0,30,30)
    pygame.draw.rect(window, START_COLOR, start_rect)
    
    # Draw the Ending Square (Red)
    end_rect = ending_position + SQUARE_SIZE # Concatenates (870,570) with (30,30) -> (870,570,30,30)
    pygame.draw.rect(window, END_COLOR, end_rect)
    pygame.display.flip()

    # Draws the surface object to the screen.
    pygame.display.update()
    # Dessiner le chemin
    

    
pygame.quit()