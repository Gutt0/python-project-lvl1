"""Game to define is number even or not."""
import sys

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def correct_answer():
    """Return result of the question.

    Args:
    correct: correct answer

    Returns:
        str
    """
    run_num = rundom_number()
    if run_num % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    sys.stdout.write('Question: {0}\n'.format(run_num))
    return correct
