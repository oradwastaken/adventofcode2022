"""Advent of Code 2022, Day 2:
https://adventofcode.com/2022/day/2
"""

from pathlib import Path

rps_file = Path('input02.txt')


def main():
    # Part 1
    rps_dict = {
        'A X\n': 3 + 1,  # Rock, you put Rock
        'A Y\n': 6 + 2,  # Rock, you put Paper
        'A Z\n': 0 + 3,  # Rock, you put scissor
        'B X\n': 0 + 1,  # Paper, you put Rock
        'B Y\n': 3 + 2,  # Paper, you put Paper
        'B Z\n': 6 + 3,  # Paper, you put scissor
        'C X\n': 6 + 1,  # Scissor, you put Rock
        'C Y\n': 0 + 2,  # Scissor, you put Paper
        'C Z\n': 3 + 3,  # Scissor, you put scissor
    }

    with open(rps_file, 'r') as f:
        total_score = sum(rps_dict[line] for line in f)
    print(total_score)

    # Part 2
    rps_dict = {
        'A X\n': 0 + 3,  # Rock, you need to lose (scissor)
        'A Y\n': 3 + 1,  # Rock, you need to draw (rock)
        'A Z\n': 6 + 2,  # Rock, you need to win (paper)
        'B X\n': 0 + 1,  # Paper, you need to lose (rock)
        'B Y\n': 3 + 2,  # Paper, you need to draw (paper)
        'B Z\n': 6 + 3,  # Paper, you need to win (scissor)
        'C X\n': 0 + 2,  # Scissor, you need to lose (paper)
        'C Y\n': 3 + 3,  # Scissor, you need to draw (scissor)
        'C Z\n': 6 + 1,  # Scissor, you need to win (rock)
    }

    with open(rps_file, 'r') as f:
        total_score = sum(rps_dict[line] for line in f)
    print(total_score)


if __name__ == '__main__':
    main()
