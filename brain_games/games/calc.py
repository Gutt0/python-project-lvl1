"""Ask, get reply, check and collect correct answers in a row."""
import sys
from random import randint, randrange

import prompt

FIRST_NUM = 1
SECOND_NUM = 99
INDEX = 3
MARKS_LIST = ['+', '-', '*']


def username():
    """Return username."""
    name = prompt.string('May I have your name? ')
    sys.stdout.write('Hello, {0}!\n'.format(name))
    sys.stdout.write('What is the result of the expression?\n')
    return name

def rundom_num():
    """Return rundom number."""
    run_num = randint(FIRST_NUM, SECOND_NUM)
    if run_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(run_num), str(correct_answer)

def rundom_two_nums():
    run_num1 = randint(FIRST_NUM, SECOND_NUM)
    run_num2 = randint(FIRST_NUM, SECOND_NUM)
    return str(run_num1), str(run_num2)

def count_user_reply():
    """Make game logic."""
    name = username()
    count = 1
    while count <= INDEX: # qty of the correct answers
        run_num1, run_num2 = rundom_two_nums()
        run_mark = randrange(len(MARKS_LIST))
        if run_mark == '+':
            sum = int(run_num1) + int(run_num2)
        elif run_mark == '-':
            sum = int(run_num1) - int(run_num2)
        else:
            sum = int(run_num1) * int(run_num2)
        sys.stdout.write('Question: {0} {1} {2}\n'.format(run_num1, run_mark, run_num2))
        user_reply = prompt.string('Your answer: ')
        if int(user_reply) == sum:
            count += 1
            sys.stdout.write('Correct!\n')
        else: 
            count = 1
            sys.stdout.write("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!\n".format(user_reply, sum, name))
    sys.stdout.write('Congratulations, {0}!\n'.format(name))

