from gui_code import config 
import PySimpleGUI as sg
import time

# def read_maze_from_file(file_name):
#     """
#     Reads a maze stored in a text file and returns a 2d list containing the maze representation.
#     """
#     try:
#         with open(file_name) as fh:
#             # Convert string maze to 2d list
#             maze = [[char for char in line.strip("\n")] for line in fh]

#             # Get maze dimensions
#             num_cols_top_row = len(maze[0])
#             num_rows = len(maze)

#             # Check maze is rectangular
#             for row in maze:
#                 if len(row) != num_cols_top_row:
#                     print("The maze is not rectangular.")
#                     raise SystemExit
#             # Find obstacles and initial positions for player and opponent
#             maze_obstacles = []
#             for i in range(num_rows):
#                 for j in range(num_cols_top_row):
#                     if maze[i][j] == config.OBSTACLE:
#                         maze_obstacles.append((i, j))
#                     elif maze[i][j] == config.PLAYER:
#                         player_start_pos = (i, j)
#                     elif maze[i][j] == config.OPPONENT:
#                         opponent_start_pos = (i, j)

#             return maze, (num_rows, num_cols_top_row), maze_obstacles, player_start_pos, opponent_start_pos
#     except UnboundLocalError:
#         print("The maze needs a player and an opponent.")
#         raise SystemExit
#     except OSError:
#         print("There is a problem with the file you have selected.")
#         raise SystemExit

def get_layout_and_window():
    layout = [
    [sg.Text('Maze Solver Using PySimpleGUI'), sg.Text('', key='-OUTPUT-')],
    [sg.Graph((800, 800), (0, 450), (450, 0), key='-GRAPH-',
                change_submits=True, drag_submits=False)],
    [sg.Text("", size=(50, 2), key='-TEXT-')],
    [sg.Button('draw path to goal'), sg.Button('reset'),sg.Button('text'), sg.Button('exit')]
    ]

    window = sg.Window('Window Title', layout, finalize=True)
    return layout, window


def draw_maze(g, maze_grid, maze_dimensions):
    for row in range(maze_dimensions[0]):
        for col in range(maze_dimensions[1]):
            if maze_grid[row][col] == "*":
                g.draw_rectangle((col * config.BOX_SIZE + 5, row * config.BOX_SIZE + 3), (col * config.BOX_SIZE + config.BOX_SIZE + 5, row * config.BOX_SIZE + config.BOX_SIZE + 3), line_color='red', fill_color='black')        
            elif maze_grid[row][col] == "P":
                g.draw_rectangle((col * config.BOX_SIZE + 5, row * config.BOX_SIZE + 3), (col * config.BOX_SIZE + config.BOX_SIZE + 5, row * config.BOX_SIZE + config.BOX_SIZE + 3), line_color='red', fill_color='orange')             
            elif maze_grid[row][col] == "O":
                g.draw_rectangle((col * config.BOX_SIZE + 5, row * config.BOX_SIZE + 3), (col * config.BOX_SIZE + config.BOX_SIZE + 5, row * config.BOX_SIZE + config.BOX_SIZE + 3), line_color='red', fill_color='yellow')
            else:
                g.draw_rectangle((col * config.BOX_SIZE + 5, row * config.BOX_SIZE + 3), (col * config.BOX_SIZE + config.BOX_SIZE + 5, row * config.BOX_SIZE + config.BOX_SIZE + 3), line_color='red', fill_color='white')  

def draw_treasure(path_to_goal, player_start_pos, window, g):
        for i, (x, y) in enumerate(path_to_goal):
            if (x,y) not in [player_start_pos, path_to_goal[-1]]: 
                g.draw_rectangle((x * config.BOX_SIZE + 5, y * config.BOX_SIZE + 3), (x * config.BOX_SIZE + config.BOX_SIZE + 5, y * config.BOX_SIZE + config.BOX_SIZE + 3), line_color='red', fill_color='green')
                letter_location = (x * config.BOX_SIZE + 18, y * config.BOX_SIZE + 17)
                g.draw_text('{}'.format(i),
                            letter_location, font='Courier 25')
            else:
                g.draw_rectangle((x * config.BOX_SIZE + 5, y * config.BOX_SIZE + 3), (x * config.BOX_SIZE + config.BOX_SIZE + 5, y * config.BOX_SIZE + config.BOX_SIZE + 3), line_color='red', fill_color='orange')
                letter_location = (x * config.BOX_SIZE + 18, y * config.BOX_SIZE + 17)
                g.draw_text('{}'.format(i),
                        letter_location, font='Courier 25')
            window.refresh()
            time.sleep(0.5)