################# 1.3 ##############
# === Import the Pygame Zero framework ===
import pgzrun  # Allows you to create games with a simplified interface
####################################

# === Game Board Dimensions ===
GRID_WIDTH = 25     # Number of columns (tiles) horizontally
GRID_HEIGHT = 15    # Number of rows (tiles) vertically
GRID_SIZE = 50      # Size (in pixels) of each tile: 50x50

# === Game Window Size (in pixels) ===
WIDTH = GRID_WIDTH * GRID_SIZE    # 1250 pixels wide
HEIGHT = GRID_HEIGHT * GRID_SIZE  # 750 pixels tall

# === Global Game State ===
gameOver = False  #  Declare globally

# === Dungeon Map Layout ===
# W = wall, P = player start, G = gold, K = key, D = door, ' ' = floor
MAP = [
    "WWWWWWWWWWWWWWWWWWWWWWWWW",
    "W P   W     W     W     W",
    "W WWW W WWWWW WWWWW WWW W",
    "W W G     W   K   W G W W",
    "W W WWWWW W WWWWW W W W W",
    "W K W     W     W W W K W",
    "WWW W WWWWW WWW W WWW WWW",
    "W     W   W K W W     W W",
    "W WWWWW W W WWW WWWWW W W",
    "W W   W W   W   W   K   W",
    "W W W WWWWW WWWWW W WWWWW",
    "W   W     K     W W     W",
    "WWWWWWWWWWWWWWWWWWWWWWW W",
    "W G     K     K     G   D",
    "WWWWWWWWWWWWWWWWWWWWWWWWW"
]

# === Converts grid coordinates to screen coordinates ===
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

# === Draw background floor tiles ===
def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))

# === Get the player's position on the grid ===
def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))

# === Set up game objects and initial state ===
def SetupGame():
    global player
    global keysToCollect
    global gameOver  #  Must declare this to modify global variable
    gameOver = False

    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)

# === Draw static walls and door ===
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

# === Draw player and uncollected keys ===
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()

# === Main draw loop ===
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        screen.draw.text("YOU WIN!", center=(WIDTH // 2, HEIGHT // 2), fontsize=80, color="yellow")

# === Move the player on the grid ===
def MovePlayer(dx, dy):
    global gameOver
    if gameOver:
        return

    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy

    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) == 0:
            gameOver = True  #  Only win if all keys collected
        return

    # Move player
    player.pos = GetScreenCoords(x, y)

    # Check for key pickup
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)
        if x == keyX and y == keyY:
            keysToCollect.remove(key)
            break  #  Stop after removing the key

# === Handle keyboard input ===
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

# === Start the game ===
SetupGame()
pgzrun.go()
