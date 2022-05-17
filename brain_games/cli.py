"""This script welcome the user and ask for his name."""
import sys

import prompt


def welcome_user():
    """Welcome string and ask for the user name."""
    name = prompt.string('May I have your name? ')

    sys.stdout.write('Hello, {0}!\n'.format(name))
