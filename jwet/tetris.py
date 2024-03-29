"""
    Tetris an Python
    inspired from:
    https://medium.com/gitconnected/writing-tetris-in-python-2a16bddb5318
"""

from enum import Enum
from random import choice


class Colors(Enum):
    """
    Allowed colors for the pieces in the game.
    Color definitions are from:
    - https://sashamaps.net/docs/resources/20-colors/
    """

    RED = (230, 25, 75)
    ORANGE = (245, 130, 48)
    YELLOW = (255, 225, 25)
    GREEN = (60, 180, 75)
    BLUE = (0, 130, 200)
    PURPLE = (145, 30, 180)
    GREY = (128, 128, 128)


def random_color() -> Colors:
    """returns a random allowable piece color"""
    return choice(list(Colors))
