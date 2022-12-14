"""Advent of Code 2022, Day 7:
https://adventofcode.com/2022/day/7
"""

from pathlib import Path

file = Path('input.txt')


def main():
    # Construct the full paths for the files
    cwd = []
    filelist = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(('dir', '$ cd /', '$ ls')):
                pass
            elif line.startswith('$ cd ..'):
                cwd.pop()
            elif line.startswith('$ cd'):
                *_, directory = line.split()
                cwd.append(directory)
            else:
                filesize, filename = line.split()
                filepath = Path(*cwd) / filename
                filelist.append((filepath, int(filesize)))

    # Calculate the size of each directory
    directory_sizes = {}
    for filepath, filesize in filelist:
        filepath = filepath.parent
        while filepath != Path('.'):
            directory_sizes[filepath] = directory_sizes.get(filepath, 0) + filesize
            filepath = Path(filepath).parent

    # Part 1:
    sum_of_sizes = sum(directory_size for directory_size in directory_sizes.values() if directory_size <= 100_000)
    print('Part 1: ', sum_of_sizes)

    # Part 2:
    total_disk_space = 70_000_000
    used_space = sum(size for path, size in directory_sizes.items() if '/' not in str(path))
    free_space = total_disk_space - used_space
    need_to_free = 30_000_000 - free_space
    possible_dirs = {dirpath: directory_size for dirpath, directory_size in directory_sizes.items()
                     if directory_size >= need_to_free}

    smallest_dir = min(possible_dirs, key=possible_dirs.get)

    print(f"Need to free up: {need_to_free}")
    print('Part 2: ', possible_dirs[smallest_dir])


if __name__ == '__main__':
    main()
