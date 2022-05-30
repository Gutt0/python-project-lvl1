import sys
from math import gcd

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(number):
    if number < 2:
        return 'no'

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        
        divider += 1
    
    return 'yes'


def correct_answer():
    """Return result of the question."""
    run_num = rundom_number()
    result = is_prime(run_num)
    sys.stdout.write('Question: {0}\n'.format(run_num))
    return result