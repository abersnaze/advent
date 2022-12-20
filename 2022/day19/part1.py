#!python3

import fileinput
import re
from collections import defaultdict, Counter
from itertools import islice, product, repeat
from functools import reduce

lines = list(map(lambda x: x.strip(), fileinput.input()))
inventory = Counter(
    {
        "ore": 0,
        "clay": 0,
        "geode": 0,
        "obsidian": 0,
    }
)
robots = Counter(
    {
        "ore": 1,
        "clay": 0,
        "geode": 0,
        "obsidian": 0,
    }
)
blueprint_num = 1
all_blueprints = defaultdict(list)
for line in lines:
    blueprint = line[line.index(":") + 7 : -1]
    for recipe in blueprint.split(". Each "):
        if " and " in recipe:
            (
                kind,
                _,
                _,
                amount1,
                thing1,
                _,
                amount2,
                thing2,
            ) = recipe.split(" ")
            all_blueprints[blueprint_num].append(({"ore": -4}, "ore"))
            all_blueprints[blueprint_num].append(
                ({thing1: -int(amount1), thing2: -int(amount2)}, kind)
            )
        else:
            kind, _, _, amount1, thing1 = recipe.split(" ")
            all_blueprints[blueprint_num].append(({thing1: -int(amount1)}, kind))
    blueprint_num += 1


def optimal(minute, blueprints, inventory, robots):
    if minute > 24:
        return inventory["geode"]
    # start with just wait for the robots to produce
    curr_best = 0
    for cost, robot in blueprints:
        next_inv = Counter(inventory)
        next_inv.update(cost)
        # blueprint costs too much
        if any(map(lambda v: v < 0, next_inv.values())):
            continue
        # current robots produce ore
        next_inv.update(robots)
        # new robot comes online
        next_robots = Counter(robots)
        next_robots[robot] = 1
        best_with = optimal(minute + 1, blueprints, next_inv, next_robots)
        if curr_best < best_with:
            curr_best = best_with
    if curr_best == 0:
        # current robots produce ore
        next_inv = Counter(inventory)
        next_inv.update(robots)
        curr_best = optimal(minute + 1, blueprints, next_inv, robots)
    return curr_best


for num, blueprints in all_blueprints.items():
    best = optimal(1, blueprints, Counter(inventory), Counter(robots))
    print(num, best)
