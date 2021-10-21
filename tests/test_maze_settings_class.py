import os
from scripts.gui_code import search
from scripts.maze_settings_class import MazeSettings

class Test:
    settings_object = MazeSettings()
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

    def test_offsets(self):
        assert self.settings_object.offsets == {
            "right": (1, 0),
            "left": (-1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }

    def test_constants(self):
        assert self.settings_object.PLAYER == "P"
        assert self.settings_object.OPPONENT== "O"
        assert self.settings_object.OBSTACLE == "*"
        assert self.settings_object.GAME_SPEED == 0.25
        assert self.settings_object.WIDTH == 800
        assert self.settings_object.HEIGHT == 800
        assert self.settings_object.SOUND == False
        assert self.settings_object.BOX_SIZE == 25
    