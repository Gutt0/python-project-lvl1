#!/usr/bin/env python
"""Script for calc."""

import sys

from brain_games.games import calc


def welcome():
    """Print welcome message."""
    sys.stdout.write('Welcome to the Brain Games!\n')


def main():
    """Output main."""
    welcome()
    calc.count_user_reply()


if __name__ == '__main__':
    main()