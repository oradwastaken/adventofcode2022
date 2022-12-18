"""Advent of Code 2022, Day 5:
https://adventofcode.com/2022/day/5
"""
from collections import namedtuple
from pathlib import Path

file = Path('moves.txt')
lines = file.read_text().split(sep='\n')

Instruction = namedtuple("Instruction", "number from_crate to_crate")

stacks = {
    1: ['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
    2: ['H', 'F', 'R'],
    3: ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
    4: ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
    5: ['P', 'S', 'M', 'J', 'H'],
    6: ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
    7: ['P', 'T', 'H', 'N', 'M', 'L'],
    8: ['F', 'D', 'Q', 'R'],
    9: ['D', 'S', 'C', 'N', 'L', 'P', 'H'],
}


def main():
    for line in lines:
        instruction = parse_instructions(line)
        make_move_part1(stacks, instruction)

    print(''.join([stack.pop() for stack in stacks.values()]))


def make_move_part1(stacks: dict[int, list[str]], instruction: Instruction):
    for _ in range(instruction.number):
        stacks[instruction.to_crate].append(stacks[instruction.from_crate].pop())


def make_move_part2(stacks: dict[int, list[str]], instruction: Instruction):
    collected_boxes = [stacks[instruction.from_crate].pop() for _ in range(instruction.number)]
    stacks[instruction.to_crate].extend(reversed(collected_boxes))


def parse_instructions(instruction: str):
    instruction_parts = instruction.split()
    num_crates = int(instruction_parts[1])
    from_crate = int(instruction_parts[3])
    to_crate = int(instruction_parts[5])
    return Instruction(num_crates, from_crate, to_crate)


if __name__ == '__main__':
    main()
