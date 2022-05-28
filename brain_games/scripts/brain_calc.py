#!/usr/bin/env python
"""Script for calc."""

from brain_games.common_logic import game_engine
from brain_games.games import calc


def main():
    """Output main."""
    game_engine(calc)


if __name__ == '__main__':
    main()
