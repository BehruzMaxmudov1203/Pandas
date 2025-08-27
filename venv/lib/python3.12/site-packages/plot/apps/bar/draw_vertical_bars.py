"""
Draw a vertical bar plot
"""
from typing import Dict
from numpy import ndarray
from .bar_generator import bar_generator


def draw_vertical_bars(
        obj_axis,      # type: object
        x,             # type: ndarray
        y,             # type: ndarray
        error_bars,    # type: ndarray
        p_bars,        # type: Dict
        p_errors       # type: Dict
        ):
    # type: (...) -> object
    """Draw a vertical bar plot

    Args:
        obj_axis (object): a matplotlib axis object
        x (numpy.ndarray): x array
        y (numpy.ndarray): y array
        error_bars (nummpy.ndarray): error bar data
        p_bars (numpy.ndarray): bar parameters
        p_errors (numpy.ndarray): error bar parameters

    Returns:
        a matplotlib.container.BarContainer object
    """
    p = p_bars
    bottom = p_bars['base_line_location']
    height = y
    left = x + p_bars['location_offset']
    width = p['width']
    return bar_generator(
        obj_axis, left, width, height, bottom,
        None, error_bars, p_bars, p_errors)
