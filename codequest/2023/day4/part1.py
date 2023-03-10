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

template = {
    "header": (
        bytes.fromhex(
            "FFFF000000000000000000000000000000000000000000000000000000000000"
        ),
        30,
    ),
    "sender": (
        bytes.fromhex(
            "0000FFFFFFFF0000000000000000000000000000000000000000000000000000"
        ),
        26,
    ),
    "seq": (
        bytes.fromhex(
            "000000000000FF00000000000000000000000000000000000000000000000000"
        ),
        25,
    ),
    "cksum": (
        bytes.fromhex(
            "00000000000000FF000000000000000000000000000000000000000000000000"
        ),
        24,
    ),
    "message": (
        bytes.fromhex(
            "0000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
        ),
        0,
    ),
}


def apply(bs, ms, shift):
    os = b""
    c = 0
    for i, m in enumerate(ms):
        if m != 0:
            c += 1
        os += (bs[i] & m).to_bytes(1)
    return os[(len(os) - c - shift) : (len(os) - shift)]


def valid(packet):
    if packet["header"] != b"UU":
        return False
    return sum(packet["message"]) % 256 == int.from_bytes(packet["cksum"])


ships = defaultdict(list)
for line in lines:
    packet_bytes = bytes.fromhex(line)
    packet = {
        k: apply(packet_bytes, mask, shift) for k, (mask, shift) in template.items()
    }
    if not valid(packet):
        continue
    ships[int.from_bytes(packet["sender"])].append(packet)

for sender, packets in ships.items():
    packets.sort(key=lambda p: int.from_bytes(p["seq"]))
    print(sender, "\t", "".join([p["message"].decode("utf8") for p in packets]))
