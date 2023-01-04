"""Advent of Code 2022, Day 10:
https://adventofcode.com/2022/day/10
"""
from collections import deque
from pathlib import Path


def main():
    file = Path('input.txt')
    with open(file, 'r') as f:
        lines = deque(f.readlines())

    x_list = [1]
    cycles = [1]
    while lines:
        match lines.popleft().split():
            case ['noop']:
                cycles.append(cycles[-1] + 1)
                x_list.append(x_list[-1])

            case ['addx', value]:
                cycles.append(cycles[-1] + 1)
                x_list.append(x_list[-1])

                cycles.append(cycles[-1] + 1)
                x_list.append(x_list[-1] + int(value))

            case _:
                raise ValueError("There shouldn't be other cases!")

    signal_strength = [x * c for (x, c) in zip(x_list, cycles)]
    sum_of_strengths = sum(ss for (ss, c) in zip(signal_strength, cycles) if c in [20, 60, 100, 140, 180, 220])
    print("Part 1:", sum_of_strengths)

    CRT = []
    for cycle, sprite_pos in zip(cycles, x_list):
        if (cycle-1) % 40 in [sprite_pos-1, sprite_pos, sprite_pos+1]:
            CRT.append('#')
        else:
            CRT.append('.')

    CRT = ''.join(CRT)
    for i in range(len(CRT) // 40 + 1):
        print(CRT[(i - 1) * 40:i * 40])


if __name__ == '__main__':
    main()
