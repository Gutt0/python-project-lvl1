"""Ask, get reply from the user, check and collect three correct answers in the row.""" 
from random import randint

from brain_games import username

import sys

import prompt

FIRST_NUMBER = 1
SECOND_NUMBER = 99
INDEX = 3

def rundomnum():
    run_num = randint(FIRST_NUMBER, SECOND_NUMBER)
    if run_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(run_num), str(correct_answer)

def count_user_reply():
    i = 0
    user_reply = prompt.string('Your answer: ')
    while i <= INDEX:
        if user_reply == rundomnum[2]:
            i + 1
            print('correct!')
        else: 
            i = 0
            sys.strout.write("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {0}!".format(username))
            return
    sys.stdout.write('Congratulations, {0}\n'.format(username))

