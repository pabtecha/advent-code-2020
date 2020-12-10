from contextlib import contextmanager
from typing import Generator, TextIO


@contextmanager
def todays_file(day: int) -> Generator[TextIO, None, None]:
    with open(f'../inputs/day{day}.txt', 'r') as file:
        yield file
