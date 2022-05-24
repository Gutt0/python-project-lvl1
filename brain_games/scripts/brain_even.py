#!/usr/bin/env python
"""Script for even."""

import sys

from brain_games import even


def welcome():
    """Print welcome message."""
    sys.stdout.write('Welcome to the Brain Games!\n')


def main():
    """Output main."""
    welcome()
    even.count_user_reply()


if __name__ == '__main__':
    main()
