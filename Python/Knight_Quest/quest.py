################# 1.3 ##############

# === Import the Pygame Zero framework ===
import pgzrun  # Allows you to create games using the Pygame Zero library (a simpler version of Pygame)

####################################

# === Game Board Dimensions ===
GRID_WIDTH = 25     # Number of tiles horizontally
GRID_HEIGHT = 15    # Number of tiles vertically
GRID_SIZE = 50      # Size (in pixels) of each tile (width and height)
GUARDMOVEINTERVAL = 0.25  # Time in seconds between each guard movement

# === Game Window Size (in pixels) ===
WIDTH = GRID_WIDTH * GRID_SIZE    # Total screen width: 25 tiles × 50 pixels = 1250
HEIGHT = GRID_HEIGHT * GRID_SIZE  # Total screen height: 15 tiles × 50 pixels = 750

# === Global Game State ===
gameOver = False  # Flag to check whether the game has ended

# === Dungeon Map Layout ===
# Characters on the map:
# W = Wall, P = Player start, G = Guard, K = Key, D = Door, space = walkable floor
MAP = [
    "WWWWWWWWWWWWWWWWWWWWWWWWW",  # Top row of walls
    "W P   W     W G   W     W",  # Player starts at P, Guard at G
    "W WWW W WWWWW WWWWW WWW W",  # Walls and pathways
    "W W       W   K   W G W W",  # A key at K, Guard at G
    "W W WWWWW W WWWWW W W W W",  # Maze-like structure
    "W K W     W     W W W K W",  # Multiple keys
    "WWW W WWWWW WWW W WWW WWW",  # Central maze
    "W     W   W K W W     W W",  # More keys
    "W WWWWW W W WWW WWWWW W W",  # Complex walls
    "W W   W W   W   W   K   W",  # Open area with a key
    "W W W WWWWW WWWWW W WWWWW",  # Tight corridors
    "W  GW     K     W W     W",  # Guard and key together
    "WWWWWWWWWWWWWWWWWWWWWWW W",  # Bottom wall with one opening
    "W       K     K         D",  # Keys and the door at D
    "WWWWWWWWWWWWWWWWWWWWWWWWW"   # Bottom-most row of walls
]

# === Converts grid coordinates (x, y) to screen (pixel) coordinates ===
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)  # Convert grid tile to pixel coordinates

# === Draws the floor (background) on every tile ===
def DrawBackground():
    for y in range(GRID_HEIGHT):          # Loop through each row
        for x in range(GRID_WIDTH):       # Loop through each column
            screen.blit("floor1", GetScreenCoords(x, y))  # Draw floor tile at each position

# === Gets grid (tile) position from an actor's screen (pixel) position ===
def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))  # Convert pixel to grid

# === Initializes all game objects based on the MAP ===
def SetupGame():
    global player, keysToCollect, guards, gameOver
    gameOver = False  # Reset game state

    player = Actor("player", anchor=("left", "top"))  # Create player actor
    keysToCollect = []  # List to hold key actors
    guards = []         # List to hold guard actors

    # Loop through each tile on the map
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]  # Get the tile character
            if square == "P":
                player.pos = GetScreenCoords(x, y)  # Set player position
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))  # Create key
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)  # Add key to list
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))  # Create guard
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)  # Add guard to list

# === Draw static map objects like walls and doors ===
def DrawScenery():
    for y in range(GRID_HEIGHT):          # Loop through each row
        for x in range(GRID_WIDTH):       # Loop through each column
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))  # Draw wall
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))  # Draw door

# === Draw player, keys, and guards ===
def DrawActors():
    player.draw()  # Draw the player character
    for key in keysToCollect:
        key.draw()  # Draw each key
    for guard in guards:
        guard.draw()  # Draw each guard

# === Main draw loop called every frame ===
def draw():
    screen.clear()  # Clear the screen
    DrawBackground()  # Draw floor
    DrawScenery()     # Draw walls and door
    DrawActors()      # Draw player, keys, guards

    # If the game has ended, show win or lose message
    if gameOver:
        screen.draw.text(
            "YOU WIN!" if len(keysToCollect) == 0 else "YOU LOSE!",  # Win if no keys left
            center=(WIDTH // 2, HEIGHT // 2),  # Show message in center
            fontsize=80, color="yellow"  # Text styling
        )

# === Attempts to move the player in a direction ===
def MovePlayer(dx, dy):
    global gameOver
    if gameOver:
        return  # Do nothing if game over

    (x, y) = GetActorGridPos(player)  # Get current grid position
    x += dx  # Apply movement delta
    y += dy

    square = MAP[y][x]  # Check the destination tile
    if square == "W":
        return  # Can't move into walls
    elif square == "D":
        if len(keysToCollect) == 0:  # Only allow door if all keys collected
            gameOver = True  # Player wins
        return  # Don't move through door

    player.pos = GetScreenCoords(x, y)  # Move player to new position

    # Check if player landed on a key
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)
        if x == keyX and y == keyY:
            keysToCollect.remove(key)  # Remove collected key
            break  # Only remove one key

# === Handles key press input ===
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)  # Move left
    elif key == keys.UP:
        MovePlayer(0, -1)  # Move up
    elif key == keys.RIGHT:
        MovePlayer(1, 0)   # Move right
    elif key == keys.DOWN:
        MovePlayer(0, 1)   # Move down

# === Moves one guard toward the player ===
def MoveGuard(guard):
    global gameOver
    if gameOver:
        return  # Stop movement if game over

    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)

    # Move guard toward player (prioritize horizontal movement)
    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
        guardX += 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        guardX -= 1
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        guardY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        guardY -= 1

    guard.pos = GetScreenCoords(guardX, guardY)  # Move guard

    # Check if guard caught the player
    if guardX == playerX and guardY == playerY:
        gameOver = True  # Player loses

# === Moves all guards each turn ===
def MoveGuards():
    for guard in guards:
        MoveGuard(guard)  # Move each guard toward player

# === Start the game ===
SetupGame()  # Setup player, keys, and guards from the map
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)  # Move guards on a timer
pgzrun.go()  # Start the Pygame Zero game loop
