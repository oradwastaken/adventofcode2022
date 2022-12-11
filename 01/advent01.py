"""Advent of Code 2022, Day 1:
https://adventofcode.com/2022/day/1
"""

from pathlib import Path

calories_file = Path('input01.txt')


def main():
    with open(calories_file, 'r') as f:
        elf_calories = []
        elf = 0
        for line in f:
            if line == '\n':
                elf_calories.append(elf)
                elf = 0
            else:
                elf = elf + int(line)

    # Part 1: most calories
    elf_calories = sorted(elf_calories, reverse=True)
    print(elf_calories[0])

    # Part 2: total of top 3 elves:
    print(sum(elf_calories[0:3]))


if __name__ == '__main__':
    main()
