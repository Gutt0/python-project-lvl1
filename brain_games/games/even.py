"""Game to define is number even or not."""
import sys

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def correct_answer():
    """Return result of the question."""
    run_num = rundom_number()
    if run_num % 2 == 0:
        result = "yes"
    else:
        result = "no"
    sys.stdout.write('Question: {0}\n'.format(run_num))
    return result
