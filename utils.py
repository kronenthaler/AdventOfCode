import functools
import math
import re
import numpy as np


def add(a: tuple, b: tuple) -> tuple:
    return tuple(map(lambda i, j: i + j, a, b))


Steps2D = [(0, 1), (-1, 0), (0, -1), (1, 0)]
Steps2DDiagonal = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
Steps2DAll = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
