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

print("a", bin(int("8000", 16)).zfill(20))
count = 0
total = 0
for line in lines:
    n = int(line)
    if bin(n).count("1") % 2 == 0:
        count += 1
        m = n & ~int("8000", 16)
        print(f"n {bin(n).zfill(20)} {n}")
        print(f"m {bin(m).zfill(20)} {m}")
        total += m
        print()

print(total, count)
print(round(total / count))
