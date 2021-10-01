import time
from sys import path
import PySimpleGUI as sg
import random
import string
from gui_code import helper_functions as helpers
from gui_code import config
from gui_code import search

def draw_maze(g, maze_grid, maze_dimensions):
    for row in range(maze_dimensions[0]):
        for col in range(maze_dimensions[1]):
            if maze_grid[row][col] == "*":
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='red', fill_color='black')        
            elif maze_grid[row][col] == "P":
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='red', fill_color='orange')             
            elif maze_grid[row][col] == "O":
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='red', fill_color='yellow')
            else:
                g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='red', fill_color='white')  


def draw_path_to_treasure():
    global window, path_to_goal, player_start_pos, opponent_start_pos
    for i, (x, y) in enumerate(path_to_goal):
        if (x,y) not in [player_start_pos, path_to_goal[-1]]: 
            g.draw_rectangle((x * BOX_SIZE + 5, y * BOX_SIZE + 3), (x * BOX_SIZE + BOX_SIZE + 5, y * BOX_SIZE + BOX_SIZE + 3), line_color='red', fill_color='green')
            letter_location = (x * BOX_SIZE + 18, y * BOX_SIZE + 17)
            g.draw_text('{}'.format(i),
                        letter_location, font='Courier 25')
        else:
            g.draw_rectangle((x * BOX_SIZE + 5, y * BOX_SIZE + 3), (x * BOX_SIZE + BOX_SIZE + 5, y * BOX_SIZE + BOX_SIZE + 3), line_color='red', fill_color='orange')
            letter_location = (x * BOX_SIZE + 18, y * BOX_SIZE + 17)
            g.draw_text('{}'.format(i),
                    letter_location, font='Courier 25')
        window.refresh()
        time.sleep(0.5)

# read from file
maze_grid, maze_dimensions, maze_obstacles, player_start_pos, opponent_start_pos = helpers.read_maze_from_file(
    config.MAZE_FILE)
print(f"params: {maze_grid, maze_dimensions, maze_obstacles, player_start_pos, opponent_start_pos}")

# find path to goal
path_to_goal = search.dfs(maze_grid, (1, 1), (7,7))
print(f"path to goal: {path_to_goal}")

# path_to_goal = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (5, 3), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (3, 8), (2, 8), (2, 7), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (2, 3), (2, 4), (1, 8), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (7, 7)]

BOX_SIZE = 25
layout = [
    [sg.Text('Maze Solver Using PySimpleGUI'), sg.Text('', key='-OUTPUT-')],
    [sg.Graph((800, 800), (0, 450), (450, 0), key='-GRAPH-',
              change_submits=True, drag_submits=False)],
    [sg.Text("", size=(18, 1), key='-TEXT-')],
    [sg.Button('draw path to goal'), sg.Button('reset'),sg.Button('text'), sg.Button('exit')]
]

window = sg.Window('Window Title', layout, finalize=True)
g = window['-GRAPH-']

# draw map
draw_maze(g, maze_grid, maze_dimensions)

# Event Loop
while True:            
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'exit'):
        break

    if event == '-GRAPH-':
        mouse = values['-GRAPH-']
        if mouse == (None, None):
            continue
        box_x = mouse[0]//BOX_SIZE
        box_y = mouse[1]//BOX_SIZE
        letter_location = (box_x * BOX_SIZE + 18, box_y * BOX_SIZE + 17)
        print(box_x, box_y)
        g.draw_text('{}'.format(random.choice(string.ascii_uppercase)),
                    letter_location, font='Courier 25')

    elif event == 'text':
        window['-TEXT-'].update("hello!")

    elif event == 'draw path to goal':
        draw_path_to_treasure()
    
    elif event == 'reset':
        draw_maze(g, maze_grid, maze_dimensions)

window.close()

# NOTE: Driver code
# if __name__ == "__main__":

# NOTE: read from file
# maze_grid, maze_dimensions, maze_obstacles, player_start_pos, opponent_start_pos = helpers.read_maze_from_file(
#     config.MAZE_FILE)