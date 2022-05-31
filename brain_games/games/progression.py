"""Game to find gcd."""
import sys
from random import randint

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'What number is missing in the progression?'


def correct_answer():
    """Return result of the question.

    Args:
    result: correct answer

    Returns:
        str
    """
    common_difference = rundom_number()
    start_num = rundom_number()
    length_of_the_list = randint(5, 10)
    list = []  # noqa: WPS125
    for _i in range(length_of_the_list):  # noqa: WPS122, WPS111
        list.append(start_num)
        start_num += common_difference

    element = rundom_number()
    # define element in the list that we will change on ".."
    while element > (length_of_the_list - 1):
        element = rundom_number()

    correct_reply = str(list[element])
    list[element] = '..'
    sys.stdout.write('Question: {0}\n'.format(' '.join(map(str, list))))  # noqa: WPS221, E501
    return correct_reply
