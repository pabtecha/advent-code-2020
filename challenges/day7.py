import re
from collections import defaultdict
from typing import Dict

from challenges.utils import todays_file

CONTAINER_BAG_PATTERN = r'^(\w+\s\w+) bags contain'
CONTAINED_BAGS_PATTERN = r'(\d+) (\w+ \w+) bag'


def get_graph() -> Dict[str, Dict[str, int]]:
    graph = defaultdict(dict)
    with todays_file(7) as file:
        for line in file:
            container_bag = re.match(CONTAINER_BAG_PATTERN, line).groups()[0]
            for count, bag in re.findall(CONTAINED_BAGS_PATTERN, line):
                graph[container_bag][bag] = int(count)

    return graph


def part1():
    container_bags = set()
    graph = get_graph()

    def search(color: str) -> None:
        for bag, contained_bags in graph.items():
            if color in contained_bags:
                container_bags.add(bag)
                search(bag)

    search('shiny gold')
    return len(container_bags)


def part2():
    graph = get_graph()

    def search(color):
        count = 1
        for bag in graph[color]:
            multiplier = graph[color][bag]
            count += multiplier * search(bag)
        return count
    return search('shiny gold') - 1


if __name__ == '__main__':
    print(part1())
    print(part2())
