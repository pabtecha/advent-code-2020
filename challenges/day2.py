import re
from typing import Callable

from challenges.utils import todays_file

pattern = re.compile(r'(\d+)-(\d+)\s+(\w):\s(\w+)')


def validation1(min_num: str, max_num: str, req_char: str, password: str) -> bool:
	occurrences = list(password).count(req_char)
	return int(min_num) <= occurrences <= int(max_num)


def validation2(min_num: str, max_num: str, req_char: str, password: str) -> bool:
	p1 = int(min_num) - 1
	p2 = int(max_num) - 1

	return password[p1] != password[p2] and (password[p1] == req_char or password[p2] == req_char)


def main(validation: Callable) -> int:
	with todays_file(2) as file:
		count = 0
		for line in file:
			min_num, max_num, req_char, password = re.match(pattern, line).groups()
			if validation(min_num, max_num, req_char, password):
				count += 1

		return count


if __name__ == '__main__':
	print(main(validation1))
	print(main(validation2))
