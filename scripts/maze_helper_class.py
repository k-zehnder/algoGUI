from scripts.maze_settings_class import MazeSettings

class MazeHelpers(MazeSettings):
    def __init__(self):
        super().__init__()
             
    def read_maze_from_file(self):
        """
        Reads a maze stored in a text file and returns a 2d list containing the maze representation.
        """
        try:
            with open(self.MAZE_FILE) as fh:
                # Convert string maze to 2d list
                maze = [[char for char in line.strip("\n")] for line in fh]

                # Get maze dimensions
                num_cols_top_row = len(maze[0])
                num_rows = len(maze)

                # Check maze is rectangular
                for row in maze:
                    if len(row) != num_cols_top_row:
                        print("The maze is not rectangular.")
                        raise SystemExit
                # Find obstacles and initial positions for player and opponent
                maze_obstacles = []
                for i in range(num_rows):
                    for j in range(num_cols_top_row):
                        if maze[i][j] == self.OBSTACLE:
                            maze_obstacles.append((i, j))
                        elif maze[i][j] == self.PLAYER:
                            player_start_pos = (i, j)
                        elif maze[i][j] == self.OPPONENT:
                            opponent_start_pos = (i, j)

                # return maze, (num_rows, num_cols_top_row), maze_obstacles, player_start_pos, opponent_start_pos
                return {
                        "maze" : maze,
                        "dims" : (num_rows, num_cols_top_row),
                        "maze_obstacles" : maze_obstacles,
                        "player_start_pos" : player_start_pos,
                        "opponent_start_pos" : opponent_start_pos
                    }

        except UnboundLocalError:
            print("The maze needs a player and an opponent.")
            raise SystemExit
        except OSError:
            print("There is a problem with the file you have selected.")
            raise SystemExit

mh = MazeHelpers()
dict1 = mh.read_maze_from_file()
print(dict1)