"""
Generate a matplotlib.container.BarContainer object
"""
from typing import Dict
from numpy import ndarray


def bar_generator(
        obj_axis,   # type: object
        left,       # type: ndarray
        width,      # type: ndarray
        height,     # type: ndarray
        bottom,     # type: ndarray
        x_errors,   # type: ndarray
        y_errors,   # type: ndarray
        p_bars,     # type: Dict
        p_errors    # type: Dict
        ):
    # type: (...) -> object
    """Return a bar object
    Generate a matplotlib.container.BarContainer object

    Args:
        obj_axis (object): a matplotlib axis object
        left (ndarray): the left positions of the rectangles
        width (ndarray): the width of rectangles
        height (ndarray): the height of the rectangles
        bottom (ndarray): the bottom of the rectangles
        x_errors (ndarray): errors along x
        y_errors (ndarray): errors along y
        p_bars (dict): parameters for the bar plot
        p_errors (dict): parameters for the error bars

    Returns:
        a matplotlib.container.BarContainer object
    """
    error_bar_properties = {
        'capsize': p_errors['cap']['size'],
        'capthick': p_errors['cap']['thickness'],
        'elinewidth': p_errors['line']['width'],
        'ecolor': p_errors['color']['edge'],
        'errorevery': p_errors['resample_window_size']
    }
    return obj_axis.bar(
            left=left,
            width=width,
            height=height,
            bottom=bottom,
            xerr=x_errors,
            yerr=y_errors,
            color=p_bars['color']['face'],
            edgecolor=p_bars['color']['edge'],
            linewidth=p_bars['line']['width'],
            orientation=p_bars['orientation'],
            align=p_bars['align'],
            alpha=p_bars['opacity'],
            error_kw=error_bar_properties)
