import re
from typing import Generator, Dict

from challenges.utils import todays_file

HAIR_COLOR_PATTERN = re.compile(r'#[\d a-f]{6}$')
PID_PATTERN = re.compile(r'^\d{9}$')
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

validators = {
    'byr': lambda x: between_values(1920, x, 2002),
    'iyr': lambda x: between_values(2010, x, 2020),
    'eyr': lambda x: between_values(2020, x, 2030),
    'hgt': lambda x: validate_hgt(x),
    'hcl': lambda x: re.match(HAIR_COLOR_PATTERN, x) is not None,
    'ecl': lambda x: x in EYE_COLORS,
    'pid': lambda x: re.match(PID_PATTERN, x) is not None,
}


def validate_hgt(value: str) -> bool:
    valid = False
    if 'cm' in value:
        valid = between_values(150, value[:-2], 193)
    elif 'in' in value:
        valid = between_values(59, value[:-2], 76)
    return valid


def between_values(lower: int, value: str, upper: int) -> bool:
    return lower <= int(value) <= upper


def get_passports() -> Generator[Dict[str, str], None, None]:
    with todays_file(4) as file:
        for line in file.read().split('\n\n'):
            passport = {}

            fields = line.strip().split()

            for field in fields:
                key, value = field.split(':')
                passport.update({key: value})

            yield passport


def part2():
    valid_passports = []
    for passport in get_passports():
        if all(key in passport and validator(passport[key]) for key, validator in validators.items()):
            valid_passports.append(passport)

    return len(valid_passports)


def part1():
    required_fields = {'hcl', 'iyr', 'hgt', 'byr', 'ecl', 'pid', 'eyr'}
    valid_passports = []

    for passport in get_passports():
        if required_fields <= set(passport.keys()):
            valid_passports.append(passport)

    return len(valid_passports)


if __name__ == '__main__':
    print(part1())
    print(part2())
