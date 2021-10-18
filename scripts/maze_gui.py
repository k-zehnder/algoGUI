import PySimpleGUI as sg
from maze_helper_class import MazeHelpers, Maze


if __name__ == "__main__":
    from gui_code import config

    # instantiate MazeHelper object
    helpers_class = MazeHelpers()

    # use MazeHelper to read from file
    # returns params_dict
    params_dict = helpers_class.read_maze_from_file()

    m = Maze(**params_dict)
    print(m)


