"""
Set y axis extent
"""
from typing import Dict
import matplotlib.pyplot as pyplot
import copy
import numpy


def set_y_extent(obj_mat, p):
    # type: (object, Dict) -> object
    """Set y axis extent

    Args:
        obj_mat (object): a matplotlib.image.AxesImage object
        p (dict): a properties of the matrix plot

    Returns:
        same as inputs
    """
    old_extent = list(pyplot.getp(obj_mat, "extent"))
    old_x_extent = old_extent[0:2]
    old_y_extent = old_extent[2:4]
    new_min = p['matrix']['extent']['min']['y']
    new_max = p['matrix']['extent']['max']['y']

    if new_min is None and new_max is None:
        return
    else:
        new_y_extent = copy.deepcopy(old_y_extent)
        if new_min is not None:
            new_y_extent[0] = new_min
        else:
            pass

        if new_max is not None:
            new_y_extent[1] = new_max
        else:
            pass

        new_extent = old_x_extent + new_y_extent
        pyplot.setp(obj_mat, extent=new_extent)
        return
