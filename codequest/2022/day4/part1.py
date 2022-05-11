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


def get(b, r, c):
    if c < 0 or 6 < c:
        return 0
    col = b[c]
    if r < 0 or len(col) - 1 < r:
        return " "
    return col[r]


def win_dir(b, p, row, col, dr, dc):
    rs = list(
        range(row - 3 * dr, row + 4 * dr, dr)
        if dr != 0
        else [row, row, row, row, row, row, row]
    )
    cs = list(
        range(col - 3 * dc, col + 4 * dc, dc)
        if dc != 0
        else [col, col, col, col, col, col, col]
    )
    run = 0
    for r, c in zip(rs, cs):
        if get(b, r, c) == p:
            run += 1
        else:
            run = 0
        if run == 4:
            return True
    return False


def win(b, p, r, c):
    return (
        False
        or win_dir(b, p, r, c, -1, +1)  # diagonal left
        or win_dir(b, p, r, c, +1, +1)  # diagonal right
        or win_dir(b, p, r, c, +1, +0)  # vertical
        or win_dir(b, p, r, c, +0, +1)  # horizontal
    )


def dump(b):
    for r in range(6, -1, -1):
        for c in range(7):
            print(get(b, r, c), end="")
        print()


x = 0
wins = [0, 0, 0, 0]
for game, line in enumerate(lines):
    board = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    winner = 0
    for move, col in enumerate(map(int, line)):
        player = move % 3 + 1
        board[col - 1].append(player)
        row = len(board[col - 1]) - 1
        # dump(board)
        # if move > 28:
        #     x += 1

        if win(board, player, row, col - 1):
            winner = player
            break

    print(f"Game {game} winner {winner}")
    wins[winner] += 1
    dump(board)


print(wins)
print(wins[1] * wins[2] * wins[3])
