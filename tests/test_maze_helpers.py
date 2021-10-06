from scripts.maze_helper_class import MazeHelpers


class Test:
    helpers_class = MazeHelpers() # inherits MazeSettings
    expected_output = {
        "maze" : [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], ['*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', '*'], ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], ['*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', '*'], ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', '*'], ['*', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', '*'], ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']],
        "dims" :  (10, 10),
        "maze_obstacles": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 9), (2, 0), (2, 6), (2, 9), (3, 0), (3, 9), (4, 0), (4, 4), (4, 9), (5, 0), (5, 9), (6, 0), (6, 2), (6, 6), (6, 9), (7, 0), (7, 9), (8, 0), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)], 
        "player_start_pos": (1, 1),
        "opponent_start_pos" : (7, 7)
    }
    
    def test_read_maze_from_file(self):
        params_dict = self.helpers_class.read_maze_from_file()
        # assert {k:v for (k, v) in params_dict} == {k:v for (k, v) in self.expected_output}

        assert params_dict == self.expected_output
# {
#     "maze" : maze,
#     "dims" : (num_rows, num_cols_top_row),
#     "maze_obstacles" : maze_obstacles,
#     "player_start_pos" : player_start_pos,
#     "opponent_start_pos" : opponent_start_pos
# }
