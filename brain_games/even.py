"""Ask, get reply, check and collect correct answers in a row."""
import sys
from random import randint

import prompt

FIRST_NUMBER = 1
SECOND_NUMBER = 99
INDEX = 3


def username():
    """Return username."""
    name = prompt.string('May I have your name? ')
    sys.stdout.write('Hello, {0}!\n'.format(name))
    sys.stdout.write('Answer "yes" if the number is even, otherwise answer "no".\n')
    return name


def rundomnum():
    """Return rundom number."""
    run_num = randint(FIRST_NUMBER, SECOND_NUMBER)
    if run_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(run_num), str(correct_answer)


def count_user_reply():
    """Make game logic."""
    name = username()
    count = 1
    while count <= INDEX: # qty of the correct answers
        run_num, correct_answer = rundomnum()
        sys.stdout.write('Question: {0}\n'.format(run_num))
        user_reply = prompt.string('Your answer: ')
        if user_reply == correct_answer:
            count += 1
            sys.stdout.write('Correct!\n')
        else: 
            count = 1
            sys.stdout.write("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!\n".format(user_reply, correct_answer, name))
    sys.stdout.write('Congratulations, {0}\n'.format(name))

