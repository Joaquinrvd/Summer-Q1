################# 1.3 ##############
import pgzrun  # Import the Pygame Zero module so we can use its features, such as the game loop and drawing
####################################

# Define the number of grid tiles in width and height, and the size of each tile
GRID_WIDTH = 25   # The game board will be 25 tiles wide
GRID_HEIGHT = 15  # The game board will be 14 tiles tall (note: 15 rows in MAP, but index 0–14 is 15 total)
GRID_SIZE = 50    # Each tile is 50 pixels by 50 pixels

# Define the size of the game window using the grid dimensions
WIDTH = GRID_WIDTH * GRID_SIZE   # 25 tiles * 50 pixels = 1250 pixels wide
HEIGHT = GRID_HEIGHT * GRID_SIZE # 14 tiles * 50 pixels = 700 pixels tall

# Define the dungeon map using a list of strings, each character represents a tile or object
# Legend:
# W = wall, P = player start, G = gold, K = key, D = door, ' ' = empty floor
MAP = [
    "WWWWWWWWWWWWWWWWWWWWWWWWW",  # Row 0 (top of the screen) - full wall
    "W                       W",  # Row 1 - empty floor bordered by walls
    "W                       W",  # Row 2 - empty floor
    "W  W  KG         KG     W",  # Row 3 - walls and gold/key clusters
    "W  WWWWWWWWWWWWWWWWWWW  W",  # Row 4 - thick center wall
    "W                       W",  # Row 5 - open floor
    "W                       W",  # Row 6
    "W                       W",  # Row 7
    "W       P               W",  # Row 8 - Player starts here
    "W  WWWWWWWWWW           W",  # Row 9 - wall block
    "W      GK   W           W",  # Row 10 - some gold and a key
    "W                       W",  # Row 11 - open floor
    "W                       W",  # Row 12
    "W                       D",  # Row 13 - Door is on far-right
    "WWWWWWWWWWWWWWWWWWWWWWWWW"   # Row 14 (bottom of the screen) - full wall
]


# Function to convert grid coordinates (x, y) to pixel coordinates for screen drawing
def GetScreenCords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)  # Each tile is 50 pixels, so multiply by tile size


# Function to draw the dungeon floor across the entire screen
def DrawBackground():
    for y in range(GRID_HEIGHT):        # Loop over each row of tiles
        for x in range(GRID_WIDTH):     # Loop over each column in the row
            # Draw the "floor1" tile image at the pixel location for this tile
            screen.blit("floor1", GetScreenCords(x, y))

##########################

############# 1.7 ###########

# Function to set up the game by placing the player at the correct location
def SetupGame():
    global player  # Declare player as a global variable so we can access it elsewhere
    player = Actor("player", anchor=("left", "top"))  # Create a player Actor using the image "player.png"
    
    # Loop through the grid to find where the player (P) is in the MAP
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]  # Get the character from the MAP at this grid location
            if square == "P":   # If it's a player start position
                player.pos = GetScreenCords(x, y)  # Set the player's position to that tile's pixel coordinates

############################


############ 1.6 ###############

# Function to draw all walls and doors from the MAP
def DrawScenery():
    for y in range(GRID_HEIGHT):       # Loop through each row
        for x in range(GRID_WIDTH):    # Loop through each tile in the row
            square = MAP[y][x]         # Get the tile type (character)
            
            if square == "W":          # If it's a wall tile
                screen.blit("wall", GetScreenCords(x, y))  # Draw wall image
                
            elif square == "D":        # If it's a door tile
                screen.blit("door", GetScreenCords(x, y))  # Draw door image


# The draw() function is called automatically by Pygame Zero every frame (60 times/sec by default)
def draw():
    DrawBackground()  # First draw the floor tiles
    DrawScenery()     # Then draw the walls and door on top
    player.draw()     # Finally draw the player sprite

#####################################


SetupGame()  # Run the SetupGame function to initialize the player position and game world

from time import time

last_move_time = 0
move_delay = 0.2  # seconds

def update():
    global last_move_time
    current_time = time()

    if current_time - last_move_time > move_delay:
        if keyboard.left:
            player.x -= GRID_SIZE
            last_move_time = current_time
        elif keyboard.right:
            player.x += GRID_SIZE
            last_move_time = current_time
        elif keyboard.up:
            player.y -= GRID_SIZE
            last_move_time = current_time
        elif keyboard.down:
            player.y += GRID_SIZE
            last_move_time = current_time




pgzrun.go()  # Start the Pygame Zero game loop (this keeps the game window open and running)
