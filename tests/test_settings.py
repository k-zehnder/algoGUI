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

    def test_