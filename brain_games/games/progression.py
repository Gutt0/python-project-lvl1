"""Game to find gcd."""
import sys

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def correct_answer():
    """Return result of the question."""
    common_difference = rundom_number()
    start_num = rundom_number() + 10
    length_of_the_list = 1    
    while length_of_the_list < 5:
        length_of_the_list = rundom_number()

    list = []  # make list with progression by "common_difference"
    for i in range(length_of_the_list):
        list.append(start_num)
        start_num = start_num + common_difference

    element = rundom_number()  # define element in the list that we will change on ".."
    while element > (length_of_the_list - 1):
        element = rundom_number()

    result = str(list[element])
    list[element:element + 1] = ['..']
    sys.stdout.write('Question: {0}\n'.format(list))
    return result
