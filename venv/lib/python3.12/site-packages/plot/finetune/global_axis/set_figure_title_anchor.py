"""
Set the anchor properties of the figure title
"""
from typing import Dict
import matplotlib.pyplot as pyplot


def set_figure_title_anchor(obj_title, anchor_params):
    # type: (object, Dict) -> object
    """Set the anchor properties of the figure title

    Args:
        obj_title (object): a matplotlib Text object
        anchor_params (dict): anchor parameter dict
    Returns:
        same as input obj_title
    """
    if anchor_params['x'] is not None:
        pyplot.setp(obj_title, x=anchor_params['x'])
    else:
        pass

    if anchor_params['y'] is not None:
        pyplot.setp(obj_title, y=anchor_params['y'])
    else:
        pass

    return obj_title
