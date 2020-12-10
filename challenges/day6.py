from challenges.utils import todays_file


def part1() -> int:
    with todays_file(6) as file:
        count = 0
        for line in file.read().split('\n\n'):
            count += len(set(line.replace('\n', '')))

    return count


def part2() -> int:
    with todays_file(6) as file:
        count = 0
        for line in file.read().split('\n\n'):
            answers = [set(row) for row in line.split('\n')]
            count += len((answers[0].intersection(*answers)))

    return count


if __name__ == '__main__':
    print(part1())
    print(part2())
