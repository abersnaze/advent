#!python3

import fileinput
import re
from collections import defaultdict, Counter
from enum import Enum
from itertools import islice, product, repeat
from math import inf
from functools import reduce

def Cost:
    
lines = list(map(lambda x: x.strip(), fileinput.input()))
blueprint_num = 1
all_blueprints = defaultdict(dict)
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
            all_blueprints[blueprint_num][kind] = {
                thing1: int(amount1),
                thing2: int(amount2),
            }
        else:
            kind, _, _, amount1, thing1 = recipe.split(" ")
            all_blueprints[blueprint_num][kind] = {thing1: int(amount1)}
    blueprint_num += 1


class State:
    def __init__(
        self,
        minute = 1,
        ore = 0,
        clay = 0,
        obsidian = 0,
        geode = 0,
        ore_robot = 1,
        clay_robot = 0,
        obsidian_robot = 0,
        geode_robot = 0,
    ) -> None:
        self.minute = minute
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
        self.ore_robot = ore_robot
        self.clay_robot = clay_robot
        self.obsidian_robot = obsidian_robot
        self.geode_robot = geode_robot

    def tick(self):
        return State(
            self.minute + 1,
            self.ore,
            self.clay,
            self.obsidian,
            self.geode,
            self.ore_robot,
            self.clay_robot,
            self.obsidian_robot,
            self.geode_robot,
        )

    def tock(self):
        return State(
            self.minute,
            self.ore + self.ore_robot,
            self.clay + self.clay_robot,
            self.obsidian + self.obsidian_robot,
            self.geode + self.geode_robot,
            self.ore_robot,
            self.clay_robot,
            self.obsidian_robot,
            self.geode_robot,
        )

    

def optimal(blueprints, limit):
    best = State()
    queue = set([best])
    while len(queue):
        state = queue.pop()
        if state.minute == limit and state.geode > best.geode:
            best = state
        state = state.tick()
        if state.can_afford(blueprints[""])
    return best.geode


for num, blueprints in all_blueprints.items():
    best = optimal(blueprints, 24)
    print(num, best)
