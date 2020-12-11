from enum import Enum
from typing import List, Tuple

from challenges.utils import todays_file


class Instructions(str, Enum):
    ACCUMULATE = 'acc'
    JUMP = 'jmp'
    NO_OPERATION = 'nop'


def load_program() -> List[str]:
    with todays_file(8) as file:
        return [instruction.strip('\n') for instruction in file]


def part1(program: List[str]) -> Tuple[int, bool]:
    accumulator = 0
    pointer = 0
    visited_instructions = set()
    has_loop = False
    while True:
        instruction, increment = program[pointer].split()
        increment = int(increment)
        if instruction == Instructions.ACCUMULATE:
            accumulator += increment
            pointer += 1
        elif instruction == Instructions.JUMP:
            pointer += increment
        else:
            pointer += 1

        if pointer in visited_instructions:
            has_loop = True
            break
        else:
            visited_instructions.add(pointer)

        if pointer >= len(program):
            break

    return accumulator, has_loop


def part2() -> int:
    program = load_program()

    for i, line in enumerate(program):
        if Instructions.JUMP in line:
            new_op = line.replace(Instructions.JUMP, Instructions.NO_OPERATION)
        elif Instructions.NO_OPERATION in line:
            new_op = line.replace(Instructions.NO_OPERATION, Instructions.JUMP)
        else:
            continue

        program_copy = program.copy()
        program_copy[i] = new_op

        accumulator, has_loop = part1(program_copy)

        if has_loop is False:
            return accumulator

    return -1


if __name__ == '__main__':
    print(part1(load_program()))
    print(part2())
