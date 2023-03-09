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

winning = [
    {"1", "5", "9"},
    {"7", "5", "3"},
    {"1", "2", "3"},
    {"4", "5", "6"},
    {"7", "8", "9"},
    {"1", "4", "7"},
    {"2", "5", "8"},
    {"3", "6", "9"},
]


def play(moves):
    xs = set()
    os = set()
    for i, move in enumerate(moves):
        if i % 2 == 0:
            xs.add(move)
        else:
            os.add(move)

        for win in winning:
            if win.issubset(xs):
                return "x"
            if win.issubset(os):
                return "o"
    return "d"


x_wins = 0
o_wins = 0
draws = 0
for line in lines:
    match play(line.split(" ")):
        case "x":
            x_wins += 1
        case "o":
            o_wins += 1
        case "d":
            draws += 1

print(x_wins, o_wins, draws, "=", x_wins * o_wins * draws)
