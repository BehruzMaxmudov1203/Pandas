"""
Set matrix extent (min/max along x/y)
"""
from typing import Dict
import matplotlib.pyplot as pyplot
import copy
import numpy
from .set_x_extent import set_x_extent
from .set_y_extent import set_y_extent


def set_axis_extent(obj_mat, p):
    # type: (object, Dict) -> object
    """Draw a matrix

    Args:
        obj_mat (object): a matplotlib.image.AxesImage object
        p (dict): a properties of the matrix plot

    Returns:
        same as inputs
    """
    set_x_extent(obj_mat, p)
    set_y_extent(obj_mat, p)
    return
