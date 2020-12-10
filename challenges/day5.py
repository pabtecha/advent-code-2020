from dataclasses import dataclass
from math import floor, ceil

from challenges.utils import todays_file


@dataclass
class Region:
    lower: int
    upper: int

    def calc_half(self) -> float:
        return (self.lower + self.upper) / 2


@dataclass()
class RegionIndicator:
    lower: str
    upper: str


ROW_INDICATOR = RegionIndicator('F', 'B')
SEAT_INDICATOR = RegionIndicator('L', 'R')


def traverse(region: Region, directions: str, region_indicator: RegionIndicator) -> int:
    result = region.lower
    for direction in directions:
        half = region.calc_half()
        if direction == region_indicator.lower:
            region.upper = floor(half)
            result = region.lower
        else:
            region.lower = ceil(half)
            result = region.upper
    return result


def get_seat_number(line: str) -> int:
    rows = Region(0, 127)
    seats = Region(0, 7)
    return traverse(rows, line[:7], ROW_INDICATOR) * (seats.upper + 1) + traverse(seats, line[-3:], SEAT_INDICATOR)


def part1() -> int:
    seats = []
    with todays_file(5) as file:
        for line in file:
            seats.append(get_seat_number(line.strip()))

    return max(seats)


def part2() -> int:
    seats = []
    with todays_file(5) as file:
        for line in file:
            seats.append(get_seat_number(line.strip()))

    sorted_seats = sorted(seats)
    for i, seat in enumerate(sorted_seats[:-1]):
        if sorted_seats[i + 1] != seat + 1:
            return seat + 1


if __name__ == '__main__':
    print(part1())
    print(part2())
