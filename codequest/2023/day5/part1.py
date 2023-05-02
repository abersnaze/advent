#!python3

import fileinput
import re
from collections import Counter, defaultdict, deque
from enum import Enum, unique
from functools import reduce
from itertools import islice, product
from typing import Dict, List, Set, Tuple
import math

lines = list(map(lambda x: x.strip(), fileinput.input()))

pixels = defaultdict(lambda: ".")

min_x = math.inf
min_y = math.inf
max_x = -math.inf
max_y = -math.inf

for line in lines:
    x, y, w, h = map(int, line.split(" "))
    print(x, y, w, h)
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x + w - 1, max_x)
    max_y = max(y + h - 1, max_y)

    for i in range(x, x + w):
        for j in range(y, y + h):
            pixels[(i, j)] = "#" if pixels[(i, j)] == "." else "."

for j in range(min_y - 1, max_y + 2):
    for i in range(min_x - 1, max_x + 2):
        print(pixels[(i, j)], end="")
    print()
