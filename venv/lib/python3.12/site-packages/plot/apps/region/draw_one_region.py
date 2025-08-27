"""
Draw a single region
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray
from ...tk.matplotlibTK.legend import format_legend_label


def draw_one_region(
        obj_axis,         # type: object
        xy1y2,            # type: List
        p                 # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a single region

    Args:
        obj_axis (object): matplotlib.axis.Axis object
        xy1y2 (list): a list containing
        p (dict): data parameters

    Returns:
        ("legend", object, legend_label)
    """
    x, y1, y2 = xy1y2

    obj_edges = obj_axis.plot(
        x, y1, x, y2,
        color=p['region']['edge']['color'],
        linewidth=p['region']['edge']['width'],
        alpha=p['region']['edge']['opacity']
        )

    obj_axis.fill_between(
        x, y1, y2,
        where=y2 >= y1,
        linewidth=p['region']['edge']['width'],
        facecolor=p['region']['color']['positive'],
        alpha=p['region']['opacity']['positive'],
        interpolate=p['region']['interpolate']['positive']
        )

    obj_axis.fill_between(
        x, y1, y2,
        where=y2 <= y1,
        linewidth=p['region']['edge']['width'],
        facecolor=p['region']['color']['negative'],
        alpha=p['region']['opacity']['negative'],
        interpolate=p['region']['interpolate']['negative']
        )

    return ("legend",
            obj_edges[0],
            format_legend_label(p['legend']['content']))
