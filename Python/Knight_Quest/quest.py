import pgzrun

# Constants
GRID_WIDTH = 25
GRID_HEIGHT = 15
GRID_SIZE = 50
GUARDMOVEINTERVAL = 0.25
PLAYER_MOVE_INTERVAL = 0.1
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

# Game state variables
player = None
guards = []
keysToCollect = []
gameOver = False
level = 0
lives = 10
boss_mode = False
waiting_for_input = False
show_intro_message = ""
intro_timer = 0.0

# Maps (original and strategic levels, boss included)
MAPS = [
    [  # Map 1 - Original
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W P   W     W G   W     W",
        "W WWW W WWWWW WWWWW WWW W",
        "W W       W   K   W G W W",
        "W W WWWWW W WWWWW W W W W",
        "W K W     W     W W W K W",
        "WWW W WWWWW WWW W WWW WWW",
        "W     W   W K W W     W W",
        "W WWWWW W W WWW WWWWW W W",
        "W W   W W   W   W   K   W",
        "W W W WWWWW WWWWW W WWWWW",
        "W  GW     K     W W     W",
        "WWWWWWWWWWWWWWWWWWWWWWW W",
        "W       K     K         D",
        "WWWWWWWWWWWWWWWWWWWWWWWWW"
    ],
    [  # round 2
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W P   W   G W     G     W",
        "W WWW W WWWWW WWWWW WWW W",
        "W   W     W   K   W     W",
        "W W WWWWW W WWWWW W W W W",
        "W K   W   W     W W W K W",
        "WWW W WWWWW WWW W WWW WWW",
        "W     W   W K W W     W W",
        "W WWWWW W W WWW WWWWW W W",
        "W W   W W   W   W   K   W",
        "W W W WWWWW WWWWW W WWWWW",
        "W   G     K     W W     W",
        "WWWWWWWWWWWWWWWWWWWWWWW W",
        "W  K          K         D",
        "WWWWWWWWWWWWWWWWWWWWWWWWW"
    ],
    [  # Map 3
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W P   W     W     W     W",
        "W W W WWWWW WWWWW WWWWW W",
        "W W K  G  W   K   W  G  W",
        "W WWWWWWW W WWWWW W WWW W",
        "W   K   W W  G  W W   K W",
        "WWW W WWWWW WWW W WWWWW W",
        "W     W   W   W W     W W",
        "W WWWWW W W WWW WWWWW W W",
        "W  G  W W   W     W   K W",
        "W W W WWWWW WWWWW WWWWW W",
        "W W K     G     K     W W",
        "W WWWWWWWWWWWWWWWWWWWW W",
        "W  G    K   G   K   G  DW",
        "WWWWWWWWWWWWWWWWWWWWWWWWW"
    ],
    [  # round 4
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W     G     W     G      ",
        "W WWWWWWWWWWWWWWWWWWW WW ",
        "W K     K     K     K WW ",
        "W WWWWWWW W WWWWWWWWW WW ",
        "W   K   W     K W   K  W ",
        "WWW W WWWWW WWW W WWWWWW ",
        "W P   W   W   W W     WW ",
        "W WWWWW W WWWWW WWWWW WW ",
        "W W   W W   W   W   K  W ",
        "W W W WWWWW WWWWW W WWWW ",
        "W     G  G     G     G W ",
        "WWWWWWWWWWWWWWWWWWWWWWW  ",
        "D  K          K          ",
        "WWWWWWWWWWWWWWWWWWWWWWWWW"
    ],
    [  # fake last round
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W P     W   G     W     W",
        "W WWWWW W WWW WWWWW WWW W",
        "W   K   W   W   K   W  DW",
        "W WWWWW WWW W WWWWW WWW W",
        "W   W     W W     W     W",
        "WWW W WWWWW W WWW W WWWWW",
        "W     W   W     W W     W",
        "W WWWWW W WWWWW W WWWWW W",
        "W     W W     W W     K W",
        "W WWW W WWWWW W WWWWW WWW",
        "W   W     K   W       GW",
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W       K       K       D",
        "WWWWWWWWWWWWWWWWWWWWWWWWW"
    ],
    [  # boss round
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W P    G   G   G   G    W",
        "W WWWWWWWWWWWWWWWWWWWWW W",
        "W   K   W     K     K   W",
        "W WWWWW W WWWWW WWWWWWW W",
        "W   W   W   W     W     W",
        "WWW W WWW W WWWWW WWWWW W",
        "W     W   W     W W     W",
        "W WWWWW WWWWWWW W W WWW W",
        "W     W     G   W W   K W",
        "W WWWWW WWWWWWW WWWWWWWW ",
        "W   G     K       G     W",
        "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "W        K        K    D ",
        "WWWWWWWWWWWWWWWWWWWWWWWWW"
    ]
]

# --- Utility Functions ---
def GetScreenCoords(x, y): return (x * GRID_SIZE, y * GRID_SIZE)
def GetActorGridPos(actor): return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))

# --- Game Setup ---
def SetupGame():
    global player, keysToCollect, guards, gameOver, boss_mode, waiting_for_input, lives, level
    global show_intro_message, intro_timer

    gameOver = False
    waiting_for_input = False
    boss_mode = (level == len(MAPS) - 1)

    if level == 4:
        show_intro_message = "Last Round"
        intro_timer = 2.0
    elif level == 5:
        show_intro_message = "Boss Round"
        intro_timer = 2.0
    else:
        show_intro_message = ""
        intro_timer = 0.0

    player = Actor("player", anchor=("left", "top"))
    keysToCollect.clear()
    guards.clear()

    current_map = MAPS[level]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if y >= len(current_map) or x >= len(current_map[y]):
                continue
            tile = current_map[y][x]
            if tile == "P":
                player.pos = GetScreenCoords(x, y)
            elif tile == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif tile == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)

    if boss_mode and lives <= 0:
        lives = 10

# --- Drawing Functions ---
def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1" if x % 2 == y % 2 else "floor2", GetScreenCoords(x, y))

def DrawScenery():
    current_map = MAPS[level]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if y >= len(current_map) or x >= len(current_map[y]):
                continue
            tile = current_map[y][x]
            if tile == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif tile == "D":
                screen.blit("door", GetScreenCoords(x, y))

def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()

def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()

    if show_intro_message:
        screen.draw.text(show_intro_message, center=(WIDTH // 2, HEIGHT // 2), fontsize=80, color="orange")

    if gameOver:
        if boss_mode:
            screen.draw.text(f"Lives left: {lives}", (10, 10), fontsize=40, color="red")
            if lives <= 0:
                screen.draw.text("YOU LOST THE BOSS FIGHT!\nPress SPACE to restart level 1.", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="yellow")
            else:
                screen.draw.text("You lost a life! Press SPACE to retry boss.", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="yellow")
        else:
            screen.draw.text("YOU WIN!" if len(keysToCollect) == 0 else "YOU LOSE! Press SPACE to try again.", center=(WIDTH // 2, HEIGHT // 2), fontsize=80, color="yellow")
    elif waiting_for_input:
        screen.draw.text("Oh, you thought you were done?", center=(WIDTH // 2, HEIGHT // 2 - 30), fontsize=60, color="yellow")
        screen.draw.text("Are you ready...? (Press Y to continue, N to quit)", center=(WIDTH // 2, HEIGHT // 2 + 40), fontsize=40, color="yellow")

# --- Player Movement ---
def MovePlayer(dx, dy):
    global gameOver, waiting_for_input, level, lives

    if gameOver or waiting_for_input:
        return

    x, y = GetActorGridPos(player)
    x += dx
    y += dy

    if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
        return

    current_map = MAPS[level]
    if y >= len(current_map) or x >= len(current_map[y]):
        return

    tile = current_map[y][x]
    if tile == "W": return
    elif tile == "D" and len(keysToCollect) == 0:
        if boss_mode:
            gameOver = True
        else:
            level += 1
            if level == len(MAPS) - 1:
                waiting_for_input = True
            else:
                SetupGame()
        return

    player.pos = GetScreenCoords(x, y)

    # Check collision with guards after moving
    for guard in guards:
        gx, gy = GetActorGridPos(guard)
        if gx == x and gy == y:
            if boss_mode:
                lives -= 1
                if lives <= 0:
                    level = 0
                gameOver = True
            else:
                gameOver = True
            return

    for key in keysToCollect:
        kx, ky = GetActorGridPos(key)
        if kx == x and ky == y:
            keysToCollect.remove(key)
            break

# --- Guard AI ---
def MoveGuard(guard):
    global gameOver, level, lives, boss_mode
    if gameOver or waiting_for_input:
        return

    playerX, playerY = GetActorGridPos(player)
    guardX, guardY = GetActorGridPos(guard)
    current_map = MAPS[level]

    def is_walkable(x, y):
        return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT and current_map[y][x] != "W"

    if playerX > guardX and is_walkable(guardX + 1, guardY): guardX += 1
    elif playerX < guardX and is_walkable(guardX - 1, guardY): guardX -= 1
    elif playerY > guardY and is_walkable(guardX, guardY + 1): guardY += 1
    elif playerY < guardY and is_walkable(guardX, guardY - 1): guardY -= 1

    guard.pos = GetScreenCoords(guardX, guardY)

    if guardX == playerX and guardY == playerY:
        if boss_mode:
            lives -= 1
            if lives <= 0:
                level = 0
            gameOver = True
        else:
            gameOver = True

def MoveGuards():
    for guard in guards:
        MoveGuard(guard)

# --- Input Handling ---
def on_key_down(key):
    global waiting_for_input

    if waiting_for_input:
        if key == keys.Y:
            waiting_for_input = False
            SetupGame()
        elif key == keys.N:
            quit()
        return

    if key == keys.LEFT: MovePlayer(-1, 0)
    elif key == keys.RIGHT: MovePlayer(1, 0)
    elif key == keys.UP: MovePlayer(0, -1)
    elif key == keys.DOWN: MovePlayer(0, 1)

def on_key_up(key):
    global gameOver, level, lives
    if gameOver and key == keys.SPACE:
        if boss_mode and lives <= 0:
            level = 0
            lives = 10
        SetupGame()

# --- Timer Update ---
def update(dt):
    global intro_timer, show_intro_message
    if intro_timer > 0:
        intro_timer -= dt
        if intro_timer <= 0:
            show_intro_message = ""

# --- Run Game ---
SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()
