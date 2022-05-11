#!python3

import fileinput
import hashlib
import re
from collections import Counter, defaultdict, deque
from enum import Enum, unique
from functools import reduce
from itertools import islice, product
from typing import Dict, List, Set, Tuple
import math

lines = list(map(lambda x: x.strip(), fileinput.input()))


def hash(description, salt, prev_hash):
    h = hashlib.sha256()
    h.update(description.encode())
    h.update(b"|")
    h.update(salt.encode())
    h.update(b"|")
    h.update(prev_hash.encode())
    return h.digest().hex()


def mine(description, prev_hash):
    salt = 0
    next_hash = hash(description, str(salt), prev_hash)
    while not next_hash.startswith("000000"):
        salt += 1
        next_hash = hash(description, str(salt), prev_hash)
    return next_hash


def dump(description, salt, prev_hash, curr_hash, real_hash):
    print()
    print("desc:", description)
    print("salt:", salt)
    print("prev:", prev_hash)
    print("curr:", curr_hash)
    print("real:", real_hash)


corrected_hash = None
for line in lines:
    description, salt, prev_hash, curr_hash = line.split("|")
    real_hash = hash(description, salt, corrected_hash or prev_hash)
    dump(description, salt, prev_hash, curr_hash, real_hash)
    if real_hash != curr_hash:
        corrected_hash = mine(description, prev_hash)
        print("corr:", corrected_hash)
