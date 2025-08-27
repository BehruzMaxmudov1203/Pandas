"""
A function returning a color string given an index
and a list of color options
"""
from typing import List, AnyStr


def choose_color(i, color_list):
    # type: (int, List[AnyStr]) -> AnyStr
    """Return a color

    Return a color given a integer index
    and a list of color options.
    If index is greater than the number of
    color options, periodicity will be applied.

    Args:
        i (int): index of the color
        color_list (list): a list of color strings

    Returns:
        a color string
    """
    if i < 0:
        return color_list[0]
    else:
        return color_list[i % len(color_list)]
