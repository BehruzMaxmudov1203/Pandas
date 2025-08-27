"""
Draw a horizontal bar plot
"""
from typing import Dict
from numpy import ndarray
from .bar_generator import bar_generator


def draw_horizontal_bars(
        obj_axis,      # type: object
        x,             # type: ndarray
        y,             # type: ndarray
        error_bars,    # type: ndarray
        p_bars,        # type: Dict
        p_errors       # type: Dict
        ):
    # type: (...) -> object
    """Draw a horizontal bar plot

    Args:
        obj_axis (object): a matplotlib axis object
        x (numpy.ndarray): x array
        y (numpy.ndarray): y array
        error_bars (nummpy.ndarray): error bars
        p_bars (numpy.ndarray): bar parameters
        p_errors (numpy.ndarray): error bar parameters

    Returns:
        a matplotlib.container.BarContainer object
    """
    p = p_bars
    left = p_bars['base_line_location']
    width = y
    bottom = x + p_bars['location_offset']
    height = p['width']
    return bar_generator(
        obj_axis, left, width, height, bottom,
        error_bars, None, p_bars, p_errors)
