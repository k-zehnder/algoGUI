#import config
from gui_code import config
import heapq
from collections import deque


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def dfs(board, start, goal):
    stack = [start]
    visited = set()
    full_path = []

    while stack:
        current = stack.pop()
        full_path.append(current)
        visited.add(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:  # Other orders are fine too.
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(board, neighbour) and neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
    return full_path

def bfs(board, start, goal):
    queue = deque()
    queue.append(start)
    visited = set()
    full_path = []

    while queue:
        current = queue.popleft()
        full_path.append(current)
        visited.add(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(board, neighbour) and neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return full_path


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(board, start_pos, goal_pos):
    pq = PriorityQueue()
    pq.put(start_pos, 0)
    g_values = {}
    g_values[start_pos] = 0
    full_path = []

    while not pq.is_empty():
        current_cell_pos = pq.get()
        full_path.append(current_cell_pos)
        if current_cell_pos == goal_pos:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current_cell_pos[0] + row_offset, current_cell_pos[1] + col_offset)
            new_cost = g_values[current_cell_pos] + 1  # Would be edge weight in a weighted graph
            if is_legal_pos(board, neighbour):
                # Second check only applies to weighted graph.
                if neighbour not in g_values or new_cost < g_values[neighbour]:
                    g_values[neighbour] = new_cost
                    f_value = new_cost + heuristic(goal_pos, neighbour)
                    pq.put(neighbour, f_value)


def is_legal_pos(board, pos):
    i, j = pos
    rows = len(board)
    cols = len(board[0])
    return 0 <= i < rows and 0 <= j < cols and board[i][j] != config.OBSTACLE

