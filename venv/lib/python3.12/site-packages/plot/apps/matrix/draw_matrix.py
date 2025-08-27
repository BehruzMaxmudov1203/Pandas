"""
Draw a matrix
"""
from typing import Dict
from numpy import ndarray
import matplotlib.pyplot as pyplot
from .set_aspect_ratio import set_aspect_ratio
from .set_axis_extent import set_axis_extent
from matplotlib.colors import LogNorm


def draw_matrix(
        obj_axis,         # type: object
        data,             # type: ndarray
        p                 # type: Dict
        ):
    # type: (...) -> object
    """Draw a matrix

    Args:
        obj_axis (object): a matplotlib axis object
        data (ndarray): a numpy ndarray object
        p (dict): a python dictionary

    Returns:
        a `matplotlib.image.AxesImage` object
    """
    if p['matrix']['normalize'] == "log":
        obj = obj_axis.matshow(
            data,
            interpolation=p['matrix']['interpolation'],
            origin=p['matrix']['origin'],
            cmap=pyplot.get_cmap(p['matrix']['color_map']),
            norm=LogNorm(
                vmin=p['matrix']['vertical']['min'],
                vmax=p['matrix']['vertical']['max']
                )
            )
    else:
        obj = obj_axis.matshow(
            data,
            vmin=p['matrix']['vertical']['min'],
            vmax=p['matrix']['vertical']['max'],
            interpolation=p['matrix']['interpolation'],
            origin=p['matrix']['origin'],
            cmap=pyplot.get_cmap(p['matrix']['color_map']))
    set_aspect_ratio(obj_axis)
    set_axis_extent(obj, p)
    obj_axis.xaxis.set_ticks_position('bottom')
    return obj
