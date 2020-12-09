from typing import List


def get_expenses() -> List[int]:
	with open('../inputs/day1.txt', 'r') as file:
		return [int(expense) for expense in file]


def part1() -> int:
	expenses = get_expenses()
	for i, expense in enumerate(expenses):
		for next_expense in expenses[i:]:
			if expense + next_expense == 2020:
				return expense * next_expense


def part2() -> int:
	expenses = get_expenses()
	for i, first_expense in enumerate(expenses):
		for j, second_expense in enumerate(expenses[i:]):
			for third_expense in expenses[j:]:
				if first_expense + second_expense + third_expense == 2020:
					return first_expense * second_expense * third_expense


if __name__ == '__main__':
	print(part1())
	print(part2())
