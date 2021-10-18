# www.meet-kevin-z.com

if __name__ == "__main__":
    from gui_code import config
    import PySimpleGUI as sg
    from maze_helper_class import MazeHelpers, Maze

    # instantiate MazeHelper object
    helpers_class = MazeHelpers()
    params_dict = helpers_class.read_maze_from_file()

    # run animation loop
    m = Maze(**params_dict)


