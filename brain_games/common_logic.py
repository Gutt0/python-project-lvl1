"""Logic of the game engines."""
import sys
from random import randint

import prompt

FIRST_NUMBER = 1
SECOND_NUMBER = 9
INDEX = 3


def rundom_number():
    """Retun rundom number, run_num."""
    run_num = randint(FIRST_NUMBER, SECOND_NUMBER)
    return run_num


def username():
    """Return username: name - return."""
    sys.stdout.write('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    sys.stdout.write('Hello, {0}!\n'.format(name))
    return name


def game_engine(game):
    """Make game logic. name of the game - "str(game)"."""
    name = username()
    sys.stdout.write('{0}\n'.format(game.GAME_DESCRIPTION))
    count = 1
    while count <= INDEX:  # collecting correct answers
        right_num = game.correct_answer()
        user_reply = prompt.string('Your answer: ')
        if user_reply == right_num:
            count += 1
            sys.stdout.write('Correct!\n')
        else:
            count = 1
            sys.stdout.write("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!\n".format(user_reply, right_num, name))
    sys.stdout.write('Congratulations, {0}!\n'.format(name))
