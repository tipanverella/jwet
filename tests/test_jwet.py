from jwet.tetris import Colors, random_color


def test_random_color():
    """checks that 100 generated colors are all allowable"""
    palette = [random_color() for _ in range(100)]
    for _color in palette:
        assert _color in Colors
