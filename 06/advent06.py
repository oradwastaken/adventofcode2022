"""Advent of Code 2022, Day 6:
https://adventofcode.com/2022/day/6
"""

from pathlib import Path

file = Path('input.txt')
signal = file.read_text()


def main():
    # For part 1:
    msg_len = 4
    for i in range(0, len(signal)):
        num_unique_chars = unique_char_num(signal[i:i + msg_len])
        if num_unique_chars == msg_len:
            print('Part 1:', i + msg_len)
            break

    # For part 2:
    msg_len = 14
    for i in range(0, len(signal)):
        num_unique_chars = unique_char_num(signal[i:i + msg_len])
        if num_unique_chars == msg_len:
            print('Part 2:', i + msg_len)
            break


def unique_char_num(string: str) -> int:
    return len(set(string))


if __name__ == '__main__':
    main()
