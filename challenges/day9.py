from typing import List

from challenges.utils import todays_file


def xmas_encyrpted_numbers() -> List[int]:
    with todays_file(9) as file:
        return [int(num) for num in file]


def is_sum_of(preamble: List[int], num: int) -> bool:
    for i, first in enumerate(preamble):
        for second in preamble[i:]:
            if first + second == num:
                return True

    return False


def part1() -> int:
    preamble_length = 25
    xmas_numbers = xmas_encyrpted_numbers()
    preamble = xmas_numbers[:25]

    for i, num in enumerate(xmas_numbers[25:]):
        if i < preamble_length:
            preamble.append(num)
        elif is_sum_of(preamble, num):
            preamble[i % preamble_length] = num
        else:
            return num

    return -1


def part2() -> int:
    goal = part1()
    xmas_numbers = xmas_encyrpted_numbers()

    count = 0
    for i, _ in enumerate(xmas_numbers):
        for j, num in enumerate(xmas_numbers[i:]):
            count += num
            if count == goal:
                sequence = xmas_numbers[i:i + j]
                return min(sequence) + max(sequence)

            if count > goal:
                break

        count = 0

    return -1


if __name__ == '__main__':
    print(part1())
    print(part2())
