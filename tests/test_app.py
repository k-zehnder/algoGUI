from scripts.maze_helper_class import Maze, MazeHelpers


class Test:
    test_cases = []
    testable_functions = []
    expected_output = {
        "maze_grid" : [
                ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
                ['*', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], 
                ['*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', '*'], 
                ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], 
                ['*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', '*'], 
                ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], 
                ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', '*'], 
                ['*', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', '*'], 
                ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], 
                ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        ],
        "maze_dimensions" :  (10, 10),
        "maze_obstacles": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 9), (2, 0), (2, 6), (2, 9), (3, 0), (3, 9), (4, 0), (4, 4), (4, 9), (5, 0), (5, 9), (6, 0), (6, 2), (6, 6), (6, 9), (7, 0), (7, 9), (8, 0), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)], 
        "player_start_pos": (1, 1),
        "opponent_start_pos" : (7, 7)
    }

    helpers_class = MazeHelpers()
    params_dict = helpers_class.read_maze_from_file()       
    #gui_class = Maze(**params_dict)


    def test_helpers_init(self):
        assert type(self.params_dict) == type(dict())
        assert {k:v for k,v in self.params_dict.items()} == {k:v for k,v in self.expected_output.items()}

    def test_gui_init(self):
        pass
        
        #NOTE: these given to constructor in guiClassv0.py version
        # self.maze_grid = maze_grid
        # self.maze_dimensions = maze_dimensions
        # self.maze_obstacles = maze_obstacles
        # self.opponent_start_pos = self.opponent_pos = opponent_start_pos
        # self.player_start_pos = player_start_pos
        # self.goal_xy = (7, 7)
        # self.current_algo = "dfs"
        # self.layout, self.window = maze_helpers.get_layout_and_window()
        # self.g = self.window['-GRAPH-']

    def test_dfs_search(self):
        pass

    def test_bfs_search(self):
        pass

    def test_astar_search(self):
        pass