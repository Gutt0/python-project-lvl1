#!/usr/bin/env python
"""Main programm."""

import sys

from brain_games import cli


def welcome():
    """Print welcome message."""
    sys.stdout.write('Welcome to the Brain Games!\n')


def main():
    """Output main."""
    welcome()
    cli.welcome_user()


if __name__ == '__main__':
    main()
