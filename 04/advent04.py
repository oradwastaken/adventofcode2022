"""Advent of Code 2022, Day 4:
https://adventofcode.com/2022/day/4
"""

from collections import deque
from pathlib import Path

file = Path('input.txt')
lines = deque(file.read_text().split())


def main():
    # For part 1:
    number_of_containing_pairs = 0

    # For part 2:
    number_of_overlapping_pairs = 0

    for line in lines:
        elf1_IDs, elf2_IDs = line.split(sep=',')

        elf1_IDs = convert_ID_range_to_set(elf1_IDs)
        elf2_IDs = convert_ID_range_to_set(elf2_IDs)

        if elf1_IDs.issubset(elf2_IDs) or elf2_IDs.issubset(elf1_IDs):
            number_of_containing_pairs += 1

        if elf1_IDs.intersection(elf2_IDs):
            number_of_overlapping_pairs += 1

    print("Part 1:", number_of_containing_pairs)
    print("Part 2:", number_of_overlapping_pairs)


def convert_ID_range_to_set(section_range: str) -> set[int]:
    """Converts ranges represented as strings into sets of integers:
    e.g.,
    >>> convert_ID_range_to_set('7-9')
    {7, 8, 9}
    """
    IDs = section_range.split(sep='-')
    IDs = [int(ID) for ID in IDs]
    first_ID = min(IDs)
    last_ID = max(IDs)
    return set(range(first_ID, last_ID + 1))


if __name__ == '__main__':
    main()
