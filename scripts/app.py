from maze_helper_class import MazeHelpers, Maze

if __name__ == "__main__":
    # get parameters for game
    helpers_class = MazeHelpers()
    params_dict = helpers_class.read_maze_from_file()

    # run animation loop
    Maze(**params_dict)


