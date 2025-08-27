"""
Draw a single line
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray
from ...tk.matplotlibTK.legend import format_legend_label


def draw_one_line(
        obj_axis,         # type: object
        xy,               # type: List
        x_bars,           # type: ndarray
        y_bars,           # type: ndarray
        p                 # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a single line

    Draw a single line with error bars if specified.

    Args:
        obj_axis (object): matplotlib.axis.Axis object
        xy (list): a list containing either 1 or 2 data arrays
        x_bars (ndarray): data to be used as x error bars
        y_bars (ndarray): data to be used as y error bars
        p (dict): data parameters

    Returns:
        a matplotlib.lines.line2D object
    """
    line, error_bar_caps, error_bar_lines = obj_axis.errorbar(
            *xy, xerr=x_bars, yerr=y_bars, axes=obj_axis,
            color=p['line']['color'],
            linewidth=p['line']['width'],
            linestyle=p['line']['style'],
            alpha=p['line']['opacity'],
            ecolor=p['error_bar']['color']['edge'],
            elinewidth=p['error_bar']['line']['width'],
            capsize=p['error_bar']['cap']['size'],
            capthick=p['error_bar']['cap']['thickness'],
            errorevery=p['error_bar']['resample_window_size'],
            marker=p['marker']['style'],
            markersize=p['marker']['size'],
            zorder=p['line']['which_layer'],
     )

    return ("legend", line, format_legend_label(p['legend']['content']))
