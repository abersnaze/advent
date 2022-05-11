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

window = [0]
out_of_range = 0
for temp in map(int, lines):
    window.append(temp)
    if len(window) > 60:
        window.pop(0)
        rollavg = sum(window) / 60
        if rollavg < 1500 or 1600 < rollavg:
            out_of_range += 1

print("out_of_range", out_of_range)
