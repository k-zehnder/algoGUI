# MAZE_FILE = "gui_mazes/square_maze_25x25.txt"
# MAZE_FILE = "gui_mazes/pacman_maze.txt"
MAZE_FILE = "/home/batman/Desktop/algoGUI/gui_code/gui_mazes/test_maze.txt"
# MAZE_FILE = "gui_mazes/wide_maze.txt"
# MAZE_FILE = "gui_mazes/diagonal_23x23.txt"
# MAZE_FILE = "gui_mazes/walled_garden_10x10.txt"
# MAZE_FILE = "gui_mazes/walled_garden_20x20.txt"

PLAYER = "P"
OPPONENT = "O"
OBSTACLE = "*"
GAME_SPEED = 100
TARGET_SCORE = 3
WIDTH = 1200
HEIGHT = 740
BUTTON_FONT = ('Arial', 12, 'normal')
SCORE_FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 18, "normal")
SOUND = True
BOX_SIZE = 25
# offsets = {
#     "right": (0, 1),
#     "left": (0, -1),
#     "up": (-1, 0),
#     "down": (1, 0)
# }


offsets = {
    "right": (1, 0),
    "left": (-1, 0),
    "up": (0, -1),
    "down": (0, 1)
}

