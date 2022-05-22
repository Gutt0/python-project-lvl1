#!/usr/bin/env python
"""Second script."""

import sys

import prompt

from brain_games import even 

from brain_games import username 


def welcome():
    """Print welcome message."""
    sys.stdout.write('Welcome to the Brain Games!\n')

def welcome_user():
    """Welcome string and ask for the user name."""
    sys.stdout.write('Hello, {0}!\n'.format(username))

def condition():
    """Print condition message."""
    sys.stdout.write('Answer "yes" if the number is even, otherwise answer "no".\n')


    

def main():
    """Output main."""
    welcome()
    username()
    welcome_user()
    condition()
    even()


if __name__ == '__main__':
    main()
