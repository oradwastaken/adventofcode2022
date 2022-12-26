"""Advent of Code 2022, Day 9:
https://adventofcode.com/2022/day/9
"""
from collections import namedtuple
from copy import deepcopy
from dataclasses import dataclass, field, astuple
from pathlib import Path

file = Path('input.txt')
with open(file, 'r') as f:
    lines = f.readlines()

Instruction = namedtuple('Instruction', ['direction', 'num'])
instructions = []
for line in lines:
    direction, num = line.split()
    instructions.append(Instruction(direction, int(num)))


def main():
    # Part 1:
    rope = Rope()
    for instruction in instructions:
        rope.run_instr(instruction)
    print("Part 1: ", len(set(astuple(coord) for coord in rope.tail_log)))

    # Part 2:
    chain = Chain(9)
    for instruction in instructions:
        chain.run_instr(instruction)
    print("Part 2: ", len(set(astuple(coord) for coord in chain.ropes[-1].tail_log)))


@dataclass
class Coord:
    x: int
    y: int


@dataclass
class Rope:
    H: Coord = field(default_factory=lambda: Coord(0, 0))
    T: Coord = field(default_factory=lambda: Coord(0, 0))
    head_log: list[Coord] = field(default_factory=lambda: [Coord(0, 0)])
    tail_log: list[Coord] = field(default_factory=lambda: [Coord(0, 0)])

    @property
    def distance(self):
        return ((self.H.x - self.T.x) ** 2 + (self.H.y - self.T.y) ** 2) ** (1 / 2)

    @staticmethod
    def new_tile_loc(old_tile: Coord, direction: str) -> Coord:
        new_tile = deepcopy(old_tile)
        match direction:
            case 'R':
                new_tile.x += 1
            case 'L':
                new_tile.x -= 1
            case 'U':
                new_tile.y += 1
            case 'D':
                new_tile.y -= 1
        return new_tile

    def run_instr(self, instr: Instruction):
        for _ in range(instr.num):
            self.move_head(self.new_tile_loc(self.H, instr.direction))
            self.tail_follow()

    def move_head(self, new_tile):
        self.H = new_tile
        self.log_head()

    def tail_follow(self):
        if self.distance >= 2:
            self.T = deepcopy(self.head_log[-2])
            self.log_tail()

    def log_head(self):
        self.head_log.append(self.H)

    def log_tail(self):
        self.tail_log.append(self.T)


@dataclass
class Chain:
    num_links: int = 1
    ropes: list[Rope] = None

    def __post_init__(self):
        if self.ropes is None:
            self.ropes = [Rope() for _ in range(self.num_links)]

    def run_instr(self, instr: Instruction):
        for _ in range(instr.num):
            for i, rope in enumerate(self.ropes):
                if i == 0:
                    new_head = Rope.new_tile_loc(rope.H, instr.direction)
                else:
                    new_head = last_tail
                rope.move_head(new_head)
                rope.tail_follow()
                last_tail = deepcopy(rope.T)


if __name__ == '__main__':
    main()
