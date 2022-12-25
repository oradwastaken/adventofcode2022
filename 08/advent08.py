"""Advent of Code 2022, Day 8:
https://adventofcode.com/2022/day/8
"""
from itertools import takewhile
from pathlib import Path

import numpy as np

file = Path('input.txt')
with open(file, 'r') as f:
    grid = np.array([[*line.strip()] for line in f]).astype(float)

# Example data:
# grid = np.array([
#     [3, 0, 3, 7, 3],
#     [2, 5, 5, 1, 2],
#     [6, 5, 3, 3, 2],
#     [3, 3, 5, 4, 9],
#     [3, 5, 3, 9, 0],
# ])

def main():
    # Part 1: Count trees visible from outside:
    num_rows, num_cols = grid.shape
    visible_trees = 2 * num_cols + 2 * num_rows - 4
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            if is_visible(grid, i, j):
                visible_trees += 1
    print("Part 1: ", visible_trees)

    # Part 2: Find tree with best view
    num_rows, num_cols = grid.shape
    scenic_scores = [calc_scenic_score(grid, i, j)
                     for i in range(1, num_rows - 1)
                     for j in range(1, num_cols - 1)]
    print("Part 2: ", max(scenic_scores))


def is_visible(grid, i: int, j: int) -> bool:
    tree = grid[i, j]
    for row_of_trees in [grid[i, j + 1:],
                         grid[i, :j],
                         grid[i + 1:, j],
                         grid[:i, j]]:
        if np.all(tree > row_of_trees):
            return True
    return False


def calc_scenic_score(grid, i: int, j: int) -> bool:
    tree_height = grid[i, j]
    row_score = [how_many_trees_can_you_see(tree_height, row_of_trees)
                 for row_of_trees in [grid[i, j + 1:],
                                      list(reversed(grid[i, :j])),
                                      grid[i + 1:, j],
                                      list(reversed(grid[:i, j])), ]
                 ]
    scenic_score = np.product(row_score)
    return scenic_score


def how_many_trees_can_you_see(tree_height, row_of_trees) -> int:
    if np.all(tree_height > row_of_trees):
        return len(row_of_trees)
    else:
        return len(list(takewhile(lambda x: tree_height > x, row_of_trees))) + 1


if __name__ == '__main__':
    main()
