class MazeSettings:
    def __init__(self):
        self.offsets = {
        "right": (1, 0),
        "left": (-1, 0),
        "up": (0, -1),
        "down": (0, 1)
    }
