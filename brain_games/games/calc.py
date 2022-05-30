"""Game to calculate."""
import sys
from random import choice

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'What is the result of the expression?'
MARKS_LIST = ['+', '-', '*']  # noqa: WPS407


def correct_answer():
    """Return result of the question.

    Args:
    correct: correct answer

    Returns:
        str
    """
    run_num1 = rundom_number()
    run_num2 = rundom_number()
    run_mark = choice(MARKS_LIST)
    if run_mark == '+':
        correct = str(int(run_num1) + int(run_num2))
    elif run_mark == '-':
        correct = str(int(run_num1) - int(run_num2))
    else:
        correct = str(int(run_num1) * int(run_num2))
    sys.stdout.write('Question: {0} {1} {2}\n'.format(run_num1, run_mark, run_num2))  # noqa: E501
    return correct
