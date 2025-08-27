"""
Draw a single series of bars
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray
from .draw_vertical_bars import draw_vertical_bars
from .draw_horizontal_bars import draw_horizontal_bars
from ...tk.matplotlibTK.legend import format_legend_label


def draw_one_bar_series(
        obj_axis,         # type: object
        xy,               # type: List
        x_error_bars,     # type: ndarray
        y_error_bars,     # type: ndarray
        p_data,           # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a single line

    Draw a single line with error bars if specified.

    Args:
        obj_axis (object): matplotlib.axis.Axis object
        xy (list): a list containing either 1 or 2 data arrays
        x_error_bars (ndarray): data to be used as x error bars
        y_error_bars (ndarray): data to be used as y error bars
        p_data (dict): data parameters

    Returns:
        ("legend", bar_object, legend_name)
    """
    p_bars = p_data['bar']
    p_errors = p_data['error_bar']
    if p_bars['orientation'] == 'vertical':
        bar = draw_vertical_bars(
            obj_axis, *xy, x_error_bars, p_bars, p_errors)
    else:
        bar = draw_horizontal_bars(
            obj_axis, *xy, y_error_bars, p_bars, p_errors)

    return ("legend", bar, format_legend_label(p_data['legend']['content']))
