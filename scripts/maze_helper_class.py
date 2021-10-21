import time
from sys import path
import PySimpleGUI as sg
import random
import string
from collections import deque
from gui_code import search

from maze_settings_class import MazeSettings

class MazeHelpers(MazeSettings):
    def __init__(self):
        super().__init__()
             
    def read_maze_from_file(self) -> list:
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
    def __init__(self, maze_grid: list, maze_dimensions: tuple, maze_obstacles: list, player_start_pos: tuple, opponent_start_pos: tuple, *args, **kwargs):
        super().__init__()
        self.maze_grid = maze_grid
        self.maze_dimensions = maze_dimensions
        self.maze_obstacles = maze_obstacles
        self.player_start_pos = player_start_pos
        self.goal_xy = opponent_start_pos
        self.current_algo = "dfs"
        self.path_found = False
        self.current = 0
        self.layout, self.window = self.get_layout_and_window()
        self.g = self.window['-GRAPH-']

        # 'game loop'
        self.animation_loop()

    def update_algo_state(self, algo: str):
        self.current_algo = algo

    def find_path_to_goal(self) -> list:
        return self.algo_dict[self.current_algo](
                                                self.maze_grid, 
                                                self.player_start_pos, 
                                                self.goal_xy
                                            )

    def draw_path_to_goal(self):
        path_to_goal = self.find_path_to_goal()
        self.draw_treasure(path_to_goal)
        self.path_found = True

    def draw_maze(self):
        for row in range(self.maze_dimensions[0]):
            for col in range(self.maze_dimensions[1]):
                if self.maze_grid[row][col] == "*":
                    self.g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='black')        
                elif self.maze_grid[row][col] == "P":
                    self.g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='orange')
                    letter_location = (col * self.BOX_SIZE + 18, row * self.BOX_SIZE + 17)
                    self.g.draw_text('start',
                                letter_location, font='Courier 15')             
                elif self.maze_grid[row][col] == "O":
                    self.g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='yellow')
                    letter_location = (col * self.BOX_SIZE + 18, row * self.BOX_SIZE + 17)
                    self.g.draw_text('goal',
                                letter_location, font='Courier 15')          
                else:
                    self.g.draw_rectangle((col * self.BOX_SIZE + 5, row * self.BOX_SIZE + 3), (col * self.BOX_SIZE + self.BOX_SIZE + 5, row * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='white')  
                    
    def draw_treasure(self, path_to_goal):
            for i, (x, y) in enumerate(path_to_goal):
                if (x,y) not in [self.player_start_pos, path_to_goal[-1]]: 
                    self.g.draw_rectangle((x * self.BOX_SIZE + 5, y * self.BOX_SIZE + 3), (x * self.BOX_SIZE + self.BOX_SIZE + 5, y * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='green')
                    letter_location = (x * self.BOX_SIZE + 18, y * self.BOX_SIZE + 17)
                    self.g.draw_text('{}'.format(i),
                                letter_location, font='Courier 25')
                else:
                    self.g.draw_rectangle((x * self.BOX_SIZE + 5, y * self.BOX_SIZE + 3), (x * self.BOX_SIZE + self.BOX_SIZE + 5, y * self.BOX_SIZE + self.BOX_SIZE + 3), line_color='red', fill_color='orange')
                    letter_location = (x * self.BOX_SIZE + 18, y * self.BOX_SIZE + 17)
                    self.g.draw_text('{}'.format(i),
                            letter_location, font='Courier 25')
                self.window.refresh()
                time.sleep(self.GAME_SPEED)

    def get_layout_and_window(self):
        layout = [
            [sg.Text('Maze Solver', font="Times 20", justification='center')],
            [sg.Graph((600, 600), (0, 260), (260, 0), key='-GRAPH-',
                        change_submits=True, drag_submits=False)],
            [sg.Text("", size=(35, 2), font="Times 15", key='-TEXT-')],
            [sg.Button('draw path to goal'), sg.Button('reset'), sg.Button('toggle algorithm'), sg.Button('exit')]
        ]

        window = sg.Window(
                    'algoGUI by Kevin Zehnder', 
                    layout, 
                    element_justification='c', 
                    font="Times 15", 
                    resizable=True, 
                    finalize=True
                )
        return layout, window

    def toggle_algo(self):
        if self.current >= 2:
            self.current = 0
        else:
            self.current += 1
        return list(self.algo_dict.keys())[self.current]
        
    def animation_loop(self):
        self.window['-TEXT-'].update(f"Current search algorithm: {self.current_algo}")
        self.draw_maze()

        while True:            
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'exit'):
                break

            elif event == 'toggle algorithm':
                self.current_algo = self.toggle_algo()
                self.window['-TEXT-'].update(f"Current search algorithm: {self.current_algo}")

            elif event == 'draw path to goal':
                if self.path_found:
                    print('[INFO] resetting maze...')
                    self.draw_maze()
                self.draw_path_to_goal()

            elif event == 'reset':
                self.draw_maze()
                
if __name__ == "__main__":
    mh = MazeHelpers()
    params_dict = mh.read_maze_from_file()
    print({k:v for k,v in params_dict.items()})