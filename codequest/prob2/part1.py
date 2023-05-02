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

prizes = {
    3: 1,
    4: 10,
    5: 100,
    6: 1000,
}

draws = list(map(int, lines.pop(0).split(" ")))
draws.sort()

winnings = []
for line in lines:
    picks = list(map(int, line.split(" ")))
    picks.sort()

    d = 0
    p = 0
    match = 0
    while p < 6 and d < 7:
        if picks[p] == draws[d]:
            match += 1
            p += 1
        elif picks[p] < draws[d]:
            p += 1
        else:
            d += 1

    if match in prizes:
        print("#", draws, picks, prizes[match])
        winnings.append(prizes[match])

print("winnings", winnings)
print("total", sum(winnings))
