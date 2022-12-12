"""Advent of Code 2022, Day 3:
https://adventofcode.com/2022/day/3
"""

from pathlib import Path

import numpy as np

file = Path('input.txt')


def main():
    # Part 1

    # A mapping that converts letters (items) to their priorities
    priority_mapping = {item: priority
                        for priority, item in
                        enumerate('abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}

    # Find items that appear in both compartments:
    with open(file, 'r') as f:
        sum_of_priorities = 0
        for line in f:
            item = find_matching_letter(line.strip())
            priority = priority_mapping[item]
            print(item, priority, '\n')
            sum_of_priorities += priority
        print(sum_of_priorities)


def find_matching_letter(sack: str) -> str:

    compartment_size = len(sack) // 2
    front, back = sack[:compartment_size], sack[compartment_size:]
    front = set(front)
    back = set(back)
    matching_letters = front.intersection(back)

    print(sack)
    print(front, back)

    return matching_letters.pop()[0]


if __name__ == '__main__':
    main()
