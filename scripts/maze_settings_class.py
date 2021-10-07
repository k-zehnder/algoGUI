import PySimpleGUI as sg


class MazeSettings:
    def __init__(self):
        self.offsets = {
            "right": (1, 0),
            "left": (-1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }
        self.MAZE_FILE= "/Users/peppermint/Desktop/codes/python/algoGUI/scripts/gui_code/gui_mazes/test_maze.txt"
        self.PLAYER="P"
        self.OPPONENT="O"
        self.OBSTACLE="*"
        self.GAME_SPEED=100
        self.TARGET_SCORE=3
        self.WIDTH=1200
        self.HEIGHT=740
        self.BUTTON_FONT=('Arial', 12, 'normal')
        self.SCORE_FONT=("Courier", 24, "bold")
        self.GAME_OVER_FONT=("Courier", 18, "normal")
        self.SOUND=False
        self.BOX_SIZE=25
        self.layout=[
            [sg.Text('Maze Solver Using PySimpleGUI'), sg.Text('', key='-OUTPUT-')],
            [sg.Graph((800, 800), (0, 450), (450, 0), key='-GRAPH-',
                        change_submits=True, drag_submits=False)],
            [sg.Text("", size=(50, 2), key='-TEXT-')],
            [sg.Button('draw path to goal'), sg.Button('reset'),sg.Button('text'), sg.Button('exit')]
            ]
        self.window=sg.Window('Window Title', self.layout, finalize=True)


