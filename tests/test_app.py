from scripts.maze_helper_class import Maze, MazeHelpers


class Test:
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

    def test_helpers_init(self):
        assert type(self.params_dict) == type(dict())
        assert {k:v for k,v in self.params_dict.items()} == {k:v for k,v in self.expected_output.items()}