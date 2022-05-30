"""Game to define is the number prime or not."""
import sys

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


def is_prime(number):
    """Define is number prime or not.

    Args:
        number: checks for the number

    Returns:
        str
    """
    if number < 2:
        return 'no'

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return 'no'

        divider += 1

    return 'yes'


def correct_answer():
    """Return result of the question.

    Args:
    correct: correct answer
    rum_num: random number

    Returns:
        str
    """
    run_num = rundom_number()
    correct = is_prime(run_num)
    sys.stdout.write('Question: {0}\n'.format(run_num))

    return correct
