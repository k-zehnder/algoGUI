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
        self.current_algo = "dfs"
        self.layout, self.window = maze_helpers.get_layout_and_window()
        self.g = self.window['-GRAPH-']

        # 'game loop'
        self.animation_loop()

    def find_path_to_goal(self, algo):
        # find path to goal using algorithm specified as input argument
        algo_dict = {
                "dfs" : search.dfs,
                "bfs" : search.bfs
        }
        # property setter/getter for current_algo?
        print(f"self.current_algo: {self.current_algo}")
        return algo_dict[self.current_algo](self.maze_grid, self.player_start_pos, self.goal_xy)

    def draw_path_to_goal(self, algo):
        # find path to treasure
        path_to_goal = self.find_path_to_goal(algo)

        # draw it
        maze_helpers.draw_treasure(path_to_goal, self.player_start_pos, self.window, self.g)

    def animation_loop(self):
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

        elif event == 'text':
            m.window['-TEXT-'].update("hello!")

        elif event == 'draw path to goal':
            path_to_goal = m.find_path_to_goal('dfs')
            m.draw_path_to_goal('dfs')

        elif event == 'reset':
            maze_helpers.draw_maze(m.g, m.maze_grid, m.maze_dimensions)


""">>> class Switcher(object):
          def indirect(self,i):
                   method_name='number_'+str(i)
                   method=getattr(self,method_name,lambda :'Invalid')
                   return method()
          def number_0(self):
                   return 'zero'
          def number_1(self):
                   return 'one'
          def number_2(self):
                   return 'two'
>>> s=Switcher()
>>> s.indirect(2)"""