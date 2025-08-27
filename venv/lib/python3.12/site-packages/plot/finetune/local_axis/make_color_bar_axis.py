"""
Make an axis for plotting color bar.
It will match the size of the host axis.
"""
from typing import Dict
from mpl_toolkits.axes_grid1 import make_axes_locatable


def make_color_bar_axis(obj_axis, p):
    # type: (object, Dict) -> object
    """Make an axis for plotting the color bar

    Args:
        obj_axis (object): a matplotlib axis object
            i.e. the host axis
        p (dict): parameters for the color bar
    Returns:
        a ``matplotlib.axes._axes.Axes`` object
    """
    divider = make_axes_locatable(obj_axis)
    return divider.append_axes(
        p['location'],
        size=p['fraction'],
        pad=p['padding']['color_bar_and_panel']
        )
