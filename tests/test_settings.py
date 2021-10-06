from scripts.settings import MazeSettings

class Test:
    settings_object = MazeSettings()

    def test_offsets(self):
        assert self.settings_object.offsets == {
                                            "right": (1, 0),
                                            "left": (-1, 0),
                                            "up": (0, -1),
                                            "down": (0, 1)
                                            }

    def test_maze_file(self):
        assert self.settings_object.MAZE_FILE == "/Users/peppermint/Desktop/codes/python/algoGUI/scripts/gui_code/gui_mazes/test_maze.txt"

    def test_constants(self):
        assert self.settings_object.PLAYER == "P"
        assert self.settings_object.OPPONENT== "O"
        assert self.settings_object.OBSTACLE == "*"
        assert self.settings_object.GAME_SPEED == 100
        assert self.settings_object.TARGET_SCORE == 3
        assert self.settings_object.WIDTH == 1200
        assert self.settings_object.HEIGHT == 740
        assert self.settings_object.BUTTON_FONT == ('Arial', 12, 'normal')
        assert self.settings_object.SCORE_FONT == ("Courier", 24, "bold")
        assert self.settings_object.GAME_OVER_FONT == ("Courier", 18, "normal")
        assert self.settings_object.SOUND == False
        assert self.settings_object.BOX_SIZE == 25

    