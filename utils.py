import functools
import math
import re
import numpy as np
from queue import PriorityQueue


def add(a: tuple, b: tuple) -> tuple:
    return tuple(map(lambda i, j: i + j, a, b))


Steps2D = [(0, 1), (-1, 0), (0, -1), (1, 0)]
Steps2DDiagonal = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
Steps2DAll = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

EAST = 0; NORTH = 1; WEST = 2; SOUTH = 3
DirsToString = ['E', 'N', 'W', 'S']
DirsToArrows = ['>', '^', '<', 'v']
DirFromArrow = {'>': Steps2D[EAST], '^': Steps2D[NORTH], 'v': Steps2D[SOUTH], '<': Steps2D[WEST]}
Dirs = [EAST, NORTH, WEST, SOUTH]