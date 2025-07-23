################# 1.3 ##############
import pgzrun  # Import the Pygame Zero module so we can use its features, such as game loop and drawing

####################################

# Define the number of grid tiles in width and height, and the size of each tile
GRID_WIDTH = 16   # The game board will be 16 tiles wide
GRID_HEIGHT = 12  # The game board will be 12 tiles tall
GRID_SIZE = 50    # Each tile is 50 pixels by 50 pixels

# Define the size of the game window using the grid dimensions
WIDTH = GRID_WIDTH * GRID_SIZE   # Set the window width to 16 tiles * 50 pixels = 800 pixels
HEIGHT = GRID_HEIGHT * GRID_SIZE # Set the window height to 12 tiles * 50 pixels = 600 pixels

# Define the dungeon map using a list of strings, each character represents an object:
# W = wall, P = player start, G = gold, K = key, D = door, ' ' = empty floor
MAP = ["WWWWWWWWWWWWWWWW",  # Row 0 (top of the screen)
       "W              W",  # Row 1
       "W              W",  # Row 2
       "W  W  KG       W",  # Row 3
       "W  WWWWWWWWWW  W",  # Row 4
       "W              W",  # Row 5
       "W       P      W",  # Row 6 — Player 'P' starts here
       "W  WWWWWWWWWW  W",  # Row 7
       "W      GK   W  W",  # Row 8
       "W              W",  # Row 9
       "W              W",  # Row 10
       "W              D",  # Row 11 — Door 'D' is here
       "WWWWWWWWWWWWWWWW"]  # Row 12 (bottom of the screen)


# Function to convert grid coordinates (tile x,y) into screen coordinates (pixels)
def GetScreenCords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)  # Multiply by tile size to get pixel position


# Function to draw the background floor image on each tile
def DrawBackground():
    for y in range(GRID_HEIGHT):  # Loop over each row
        for x in range(GRID_WIDTH):  # Loop over each column
            # Draw the floor tile image ("floor1") at the screen coordinates for each grid tile
            screen.blit("floor1", GetScreenCords(x, y))

##########################

############# 1.7 ###########

# Function to set up the initial game state, including placing the player
def SetupGame():
    global player  # Declare the player variable as global so it can be used in other functions
    player = Actor("player", anchor=("left", "top"))  # Create an Actor using the "player" image
    for y in range(GRID_HEIGHT):  # Loop through rows
        for x in range(GRID_WIDTH):  # Loop through columns
            square = MAP[y][x]  # Get the character in the MAP at this grid position
            if square == "P":  # If this square contains a player marker
                player.pos = GetScreenCords(x, y)  # Place the player actor at this position
############################


############ 1.6 ###############
# Function to draw walls and door from the MAP
def DrawScenery():
    for y in range(GRID_HEIGHT):  # Loop through each row
        for x in range(GRID_WIDTH):  # Loop through each column
            square = MAP[y][x]  # Get the character in the MAP at this grid tile
            if square == "W":  # If the tile is a wall
                screen.blit("wall", GetScreenCords(x, y))  # Draw wall image
            elif square == "D":  # If the tile is a door
                screen.blit("door", GetScreenCords(x, y))  # Draw door image


# The draw() function is called automatically by Pygame Zero each frame
def draw():
    DrawBackground()  # Draw floor tiles
    DrawScenery()     # Draw walls and doors on top of floor
    player.draw()     # Draw the player sprite

#####################################

SetupGame()   # Initialize the player and setup the game state before the game loop starts
pgzrun.go()   # Start the Pygame Zero game loop (this keeps the game running and displaying)
