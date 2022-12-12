"""Advent of Code 2022, Day 3:
https://adventofcode.com/2022/day/3
"""

from collections import deque
from pathlib import Path

file = Path('input.txt')
lines = deque(file.read_text().split())


def main():
    # A mapping that converts letters (items) to their priorities
    priority_mapping = {item: priority
                        for priority, item in
                        enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}

    # Part 1: Find items that appear in both compartments:
    sum_of_priorities = sum(priority_mapping[find_matching_letter(line)] for line in lines)
    print(f"Part 1: {sum_of_priorities}")

    # Part 2: Find items that 3 consecutive bags have in common:
    sum_of_priorities = 0
    while lines:
        bag_1 = set(lines.popleft())
        bag_2 = set(lines.popleft())
        bag_3 = set(lines.popleft())

        matching_letter = bag_1.intersection(bag_2).intersection(bag_3).pop()
        sum_of_priorities += priority_mapping[matching_letter]
    print(f"Part 2: {sum_of_priorities}")


def find_matching_letter(sack: str) -> str:
    compartment_size = len(sack) // 2
    front, back = sack[:compartment_size], sack[compartment_size:]
    front = set(front)
    back = set(back)
    matching_letters = front.intersection(back)
    matching_letter = matching_letters.pop()[0]

    # print(sack)
    # print(front, back, matching_letter)

    return matching_letter


if __name__ == '__main__':
    main()
