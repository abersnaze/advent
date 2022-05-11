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

legs = []

prev_coords = [0, 0, 0]
for line in lines:
    next_coords = list(map(int, line.split(" ")))
    legs.append(
        math.floor(
            math.hypot(*list(map(lambda c: c[0] - c[1], zip(prev_coords, next_coords))))
        )
    )
    prev_coords = next_coords

print("legs", legs)
print("total", sum(legs))
