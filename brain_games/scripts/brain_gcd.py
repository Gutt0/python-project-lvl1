#!/usr/bin/env python
"""Script for even."""

from brain_games.common_logic import game_engine
from brain_games.games import gcd


def main():
    """Output main."""
    game_engine(gcd)


if __name__ == '__main__':
    main()
