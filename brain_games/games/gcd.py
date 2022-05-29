"""Game to find gcd."""
import sys
from math import gcd

from brain_games.common_logic import rundom_number

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def correct_answer():
    """Return result of the question."""
    run_num1 = rundom_number()
    run_num2 = rundom_number()
    result = str(gcd(run_num1, run_num2))
    sys.stdout.write('Question: {0} {1}\n'.format(run_num1, run_num2))
    return result