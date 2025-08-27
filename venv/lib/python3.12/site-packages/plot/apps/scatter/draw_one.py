"""
Draw a scatter series
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray
from ...tk.matplotlibTK.legend import format_legend_label


def draw_one(
        obj_axis,         # type: object
        xy,               # type: List
        p                 # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a scatter series

    Args:
        obj_axis (object): matplotlib.axis.Axis object
        xy (list): a list containing either 1 or 2 data arrays
        p (dict): data parameters

    Returns:
        ("legend", object, legend_label)
    """
    obj = obj_axis.scatter(
            *xy,
            axes=obj_axis,
            marker=p['scatter']['marker']['style'],
            s=p['scatter']['marker']['size'],
            c=p['scatter']['marker']['color'],
            linewidths=p['scatter']['edge']['width'],
            edgecolors=p['scatter']['edge']['color'],
            alpha=p['scatter']['opacity'],
     )

    return ("legend", obj, format_legend_label(p['legend']['content']))
