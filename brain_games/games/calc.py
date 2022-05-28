"""Game to calculate."""
import sys
from random import choice

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'What is the result of the expression?'
MARKS_LIST = ['+', '-', '*']


def correct_answer():
    """Return result of the question."""
    run_num1 = rundom_number()
    run_num2 = rundom_number()
    run_mark = choice(MARKS_LIST)
    if run_mark == '+':
        result = str(int(run_num1) + int(run_num2))
    elif run_mark == '-':
        result = str(int(run_num1) - int(run_num2))
    else:
        result = str(int(run_num1) * int(run_num2))
    sys.stdout.write('Question: {0} {1} {2}\n'.format(run_num1, run_mark, run_num2))
    return result
