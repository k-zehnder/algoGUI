import time
from sys import path
import PySimpleGUI as sg
import random
import string
from gui_code import search

from maze_settings_class import MazeSettings

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
                        "maze_grid" : maze,
                        "maze_dimensions" : (num_rows, num_cols_top_row),
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

class Maze(MazeSettings):
    def __init__(self, maze_grid, maze_dimensions, maze_obstacles, player_start_pos, opponent_start_pos, *args, **kwargs):
        super().__init__()
        self.maze_grid = maze_grid
        self.maze_dimensions = maze_dimensions
        self.maze_obstacles = maze_obstacles
        self.opponent_start_pos = self.opponent_pos = opponent_start_pos
        self.player_start_pos = player_start_pos
        self.goal_xy = (7, 7)
        self.current_algo = "dfs"
        self.layout, self.window = self.get_layout_and_window()
        self.g = self.window['-GRAPH-']

        # 'game loop'
        self.animation_loop()

    @property
    def update_algo_state(self):
        return(f"current algo: {self.current_algo}")

    @update_algo_state.setter
    def update_algo_state(self, algo):
        self.current_algo = algo

    def find_path_to_goal(self, algo):
        # find path to goal using algorithm specified from input argument
        algo_dict = {
                "dfs" : search.dfs,
                "bfs" : search.bfs
        }
        return algo_dict[self.current_algo](self.maze_grid, self.player_start_pos, self.goal_xy)

    def draw_path_to_goal(self, algo):
        # find path to goal
        path_to_goal = self.find_path_to_goal(algo)
        print(f"path to goal: {path_to_goal}")

        # draw it
        self.draw_treasure(path_to_goal, self.player_start_pos, self.window, self.g)

    def draw_maze(self, g, maze_grid, maze_dimensions):
        for row in range(maze_dimensions[0]):
            for col in range(maze_dimensions[1]):
                if maze_grid[row][col] == "*":
                    g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='black')        
                elif maze_grid[row][col] == "P":
                    g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='orange')             
                elif maze_grid[row][col] == "O":
                    g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='yellow')
                else:
                    g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='white')  
                    
    def draw_treasure(self, path_to_goal, player_start_pos, window, g):
            for i, (x, y) in enumerate(path_to_goal):
                if (x,y) not in [player_start_pos, path_to_goal[-1]]: 
                    g.draw_rectangle((x * self.BOX_SIZE + 5, y * self.BOX_SIZE + 3), (x * self.BOX_SIZE + self.BOX_SIZE + 5, y * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='green')
                    letter_location = (x * self.BOX_SIZE + 18, y * self.BOX_SIZE + 17)
                    g.draw_text('{}'.format(i),
                                letter_location, font='Courier 25')
                else:
                    g.draw_rectangle((x * self.BOX_SIZE + 5, y * self.BOX_SIZE + 3), (x * self.BOX_SIZE + self.BOX_SIZE + 5, y * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='orange')
                    letter_location = (x * self.BOX_SIZE + 18, y * self.BOX_SIZE + 17)
                    g.draw_text('{}'.format(i),
                            letter_location, font='Courier 25')
                window.refresh()
                time.sleep(0.5)

    def get_layout_and_window(self):
        layout = [
        [sg.Text('Maze Solver Using PySimpleGUI'), sg.Text('', key='-OUTPUT-')],
        [sg.Graph((800, 800), (0, 450), (450, 0), key='-GRAPH-',
                    change_submits=True, drag_submits=False)],
        [sg.Text("", size=(50, 2), key='-TEXT-')],
        [sg.Button('draw path to goal'), sg.Button('reset'),sg.Button('toggle algorithm'), sg.Button('exit')]
        ]

        window = sg.Window('algoGUI', layout, finalize=True)
        return layout, window

    def animation_loop(self):
        self.window['-TEXT-'].update(f"Current search algorithm: {self.current_algo}")

        # draw maze
        self.draw_maze(self.g, self.maze_grid, self.maze_dimensions)

        while True:            
            event, values = self.window.read()
            print(event, values)
            if event in (sg.WIN_CLOSED, 'exit'):
                break

            if event == '-GRAPH-':
                mouse = values['-GRAPH-']
                if mouse == (None, None):
                    continue
                print(mouse[0], mouse[1])
                box_x = mouse[0]//self.BOX_SIZE
                box_y = mouse[1]//self.BOX_SIZE
                print(box_x, box_y)

            elif event == 'toggle algorithm':
                self.update_algo_state = 'bfs' if self.current_algo == 'dfs' else 'dfs'
                print(f"updated algo to: {self.current_algo}")
                self.window['-TEXT-'].update(f"Current search algorithm: {self.current_algo}")

            elif event == 'draw path to goal':
                path_to_goal = self.find_path_to_goal(self.current_algo)
                self.draw_path_to_goal(self.current_algo)

            elif event == 'reset':
                self.draw_maze(self.g, self.maze_grid, self.maze_dimensions)
                
if __name__ == "__main__":
    mh = MazeHelpers()
    params_dict = mh.read_maze_from_file()
    print({k:v for k,v in params_dict.items()})