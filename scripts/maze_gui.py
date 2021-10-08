from maze_helper_class import MazeHelpers

class MazeGUI:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


if __name__ == "__main__":
    # instantiate MazeHelper object
    helpers_class = MazeHelpers()

    # use MazeHelper to read from file
    # returns params_dict
    params_dict = helper_class.read_maze_from_file()

    # instantiate gui with params_dict
    gui = MazeGUI(**params_dict)
    print(gui.dims)