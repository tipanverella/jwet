"""
    Game Parameters:
    - Audio
    - Font
    - Graphics
"""

from pathlib import Path
from enum import Enum


class AudioAssets(Enum):
    """Constant Audio assets"""

    JUMP = Path("assets/audio/jump.mp3")
    SOUNDTRACK = Path("assets/audio/music.wav")


class FontAssets(Enum):
    """Game font"""

    TEXT = Path("assets/font/Pixeltype.ttf")


class GraphicAssets(Enum):
    """Images"""

    FLY = {
        "1": Path("assets/graphics/Fly/fly1.png"),
        "2": Path("assets/graphics/Fly/fly2.png"),
    }

    SNAIL = {
        "1": Path("assets/graphics/Snail/snail1.png"),
        "2": Path("assets/graphics/Snail/snail2.png"),
    }

    PLAYER = {
        "stand": Path("assets/graphics/Player/player_stand.png"),
        "jump": Path("assets/graphics/Player/player_stand.png"),
        "walk_1": Path("assets/graphics/Player/player_stand.png"),
        "walk_2": Path("assets/graphics/Player/player_stand.png"),
    }

    CANVAS = {
        "ground": Path("assets/graphics/ground.png"),
        "sky": Path("assets/graphics/sky.png"),
    }


class Dimension(Enum):
    """Some dimensional constants"""

    DISPLAY_SIZE = (800, 400)
    FONT_SIZE = 50
    PLAYER_STARTING_POSITION = (80, 300)
    GAME_NAME_POSITION = (400, 80)
    GAME_MESSAGE_POSITION = (400, 330)
    SPAWNING_WAIT_MILLI_SECOND = 1500
    GROUND_LEVEL = 300
    GAME_CLOCK_SPEED = 60
    FLYING_LEVEL = 210


class Color(Enum):
    """Standard colors for the game"""

    GAME_NAME_MESSAGE = (111, 196, 169)
    SCREEN_FILL = (94, 129, 162)
