import math
from dataclasses import dataclass
from typing import List


TREE_CHAR = '#'


@dataclass
class Slope:
    x: int
    y: int


def get_map() -> List[List[str]]:
    _map = []
    with open('../inputs/day3.txt', 'r') as file:
        for row in file:
            _map.append(row)
    return _map


def crashes_tree(char: str) -> int:
    if char == TREE_CHAR:
        return 1
    return 0


def count_trees(slope: Slope):
    problem_map = get_map()
    start_row = problem_map[0]
    repetition_length = len(start_row) - 1
    current_position = 0
    trees = crashes_tree(start_row[current_position])
    for row in problem_map[slope.y::slope.y]:
        print(row)
        current_position = (current_position + slope.x) % repetition_length
        trees += crashes_tree(row[current_position])

    return trees


def main(slopes: List[Slope]) -> int:
    counts = [count_trees(slope) for slope in slopes]
    print(counts)
    return math.prod(counts)


if __name__ == '__main__':
    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
    print(main(slopes))
