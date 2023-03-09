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

inv = defaultdict(lambda: 0)
total = 1
for line in lines:
    code, amount, kind = line.split(" ")
    inv[kind] += int(amount)

print(inv)
for amount in inv.values():
    remainder = amount % 100
    print(remainder)
    total *= remainder

print(total)
