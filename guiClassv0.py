import time
from sys import path
import PySimpleGUI as sg
import random
import string
from gui_code import maze_helper_functions as maze_helpers
from gui_code import config
from gui_code import search

class Maze:
    def __init__(self, maze_grid, maze_dimensions, maze_obstacles, player_start_pos, opponent_start_pos):
        self.maze_grid = maze_grid
        self.maze_dimensions = maze_dimensions
        self.maze_obstacles = maze_obstacles
        self.opponent_start_pos = self.opponent_pos = opponent_start_pos
        self.player_start_pos = player_start_pos
        self.goal_xy = (7, 7)
        self.layout, self.window = maze_helpers.get_layout_and_window()
        self.g = self.window['-GRAPH-']

        # 'game loop'
        self.animation_loop()

    def find_path_to_goal(self, algo):
        algo_dict = {
                "dfs" : search.dfs,
                "bfs" : search.bfs
        }
        return algo_dict[algo](self.maze_grid, self.player_start_pos, self.goal_xy)

    def draw_path_to_treasure(self):
        maze_helpers.draw_path_to_treasure()

    def animation_loop(self):
        # get layout and window
        layout, window = maze_helpers.get_layout_and_window()

        # draw maze
        maze_helpers.draw_maze(self.g, self.maze_grid, self.maze_dimensions)

if __name__ == "__main__":
    maze_grid, maze_dimensions, maze_obstacles, player_start_pos, opponent_start_pos = maze_helpers.read_maze_from_file_2(
        config.MAZE_FILE)

    m = Maze(maze_grid, maze_dimensions, maze_obstacles, player_start_pos, opponent_start_pos)
    #m.drawMaze()

    # Event Loop
    while True:            
        event, values = m.window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'exit'):
            break

        if event == '-GRAPH-':
            mouse = values['-GRAPH-']
            if mouse == (None, None):
                continue
            box_x = mouse[0]//config.BOX_SIZE
            box_y = mouse[1]//config.BOX_SIZE
            letter_location = (box_x * config.BOX_SIZE + 18, box_y * config.BOX_SIZE + 17)
            print(box_x, box_y)
            g.draw_text('{}'.format(random.choice(string.ascii_uppercase)),
                        letter_location, font='Courier 25')

        elif event == 'text':
            m.window['-TEXT-'].update("hello!")

        elif event == 'draw path to goal':
            path_to_goal = m.find_path_to_goal('dfs')
            maze_helpers.draw_path_to_treasure(m.window,m.g, path_to_goal, m.player_start_pos, m.opponent_start_pos)

        elif event == 'reset':
            maze_helpers.draw_maze(m.g, m.maze_grid, m.maze_dimensions)