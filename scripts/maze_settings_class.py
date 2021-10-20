import os
class MazeSettings:
    def __init__(self):
        self.ROOT_DIR=os.path.dirname(os.path.abspath(__file__)) 
        self.offsets = {
            "right": (1, 0),
            "left": (-1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }
        self.MAZE_FILE=os.path.join(self.ROOT_DIR, "gui_code/gui_mazes/test_maze.txt")
        self.PLAYER="P"
        self.OPPONENT="O"
        self.OBSTACLE="*"
        self.GAME_SPEED=100
        self.TARGET_SCORE=3
        self.WIDTH=800
        self.HEIGHT=740
        self.BUTTON_FONT=('Arial', 12, 'normal')
        self.SCORE_FONT=("Courier", 24, "bold")
        self.GAME_OVER_FONT=("Courier", 18, "normal")
        self.SOUND=False
        self.BOX_SIZE=25


if __name__ == "__main__":
    ms = MazeSettings()
    print(ms.ROOT_DIR)
    print(ms.MAZE_FILE)