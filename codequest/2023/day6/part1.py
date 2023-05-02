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

w, h, start, cross = map(int, lines.pop(0).split(" "))

space = defaultdict(lambda: ".")
asteroids = []


def dump():
    for y in range(h):
        for x in range(w):
            print(space[(x, y)], end="")
        print()
    print()


for line in lines:
    x, y, dx, dy = map(float, line.split(" "))
    # teleport the asteroid to the start
    asteroid = (x + (dx * start), y + (dy * start), dx, dy)
    print(x, y, dx, dy, "\t->\t", *asteroid)
    asteroids.append(asteroid)

for t in range(cross + 1):
    # plot
    for x, y, dx, dy in asteroids:
        space[(math.floor(x), math.floor(y))] = "X"
    if t == 0 or t == 10:
        dump()
    # move
    asteroids = [(x + dx, y + dy, dx, dy) for x, y, dx, dy in asteroids]

dump()

for y in range(h):
    for x in range(w):
        if space[(x, y)] == ".":
            print(f"open {x}:{y}")
