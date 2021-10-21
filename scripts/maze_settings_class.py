import os
from gui_code import search

class MazeSettings:
    def __init__(self):
        self.ROOT_DIR=os.path.dirname(os.path.abspath(__file__)) 
        self.MAZE_FILE=os.path.join(self.ROOT_DIR, "gui_code/gui_mazes/test_maze.txt")
        self.offsets = {
            "right": (1, 0),
            "left": (-1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }
        self.algo_dict = {
            "dfs" : search.dfs,
            "bfs" : search.bfs,
            "a_star" : search.a_star
        }
        self.PLAYER="P"
        self.OPPONENT="O"
        self.OBSTACLE="*"
        self.WIDTH=800
        self.HEIGHT=800
        self.SOUND=False
        self.BOX_SIZE=25
        self.GAME_SPEED=0.25

if __name__ == "__main__":
    ms = MazeSettings()
    print(ms.ROOT_DIR)
    print(ms.MAZE_FILE)