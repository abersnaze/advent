#!python3

import fileinput
import re
from collections import defaultdict, Counter
from enum import Enum
from itertools import islice, product

class Them(Enum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissors

class Counter(Enum):
    X = {Them.A: 3, Them.B: 1, Them.C: 2} # Lose
    Y = {Them.A: 1, Them.B: 2, Them.C: 3} # Draw
    Z = {Them.A: 2, Them.B: 3, Them.C: 1} # Win

lines = map(lambda x: x.strip(), fileinput.input())

my_scores = []
for line in lines:
    t, u = line.split(" ")
    t = Them[t]
    u = Counter[u]
    if u == Counter.X:
        my_scores.append(u.value[t])
    elif u == Counter.Y:
        my_scores.append(u.value[t] + 3)
    else:
        my_scores.append(u.value[t] + 6)

print(my_scores)
print(sum(my_scores))
