"""
Add a box surrounding the figure title
"""
from typing import Dict
import matplotlib.pyplot as pyplot


def add_figure_title_box(obj_title, box_params):
    # type: (object, Dict) -> object
    """Add a box surrounding the title

    Args:
        obj_title (object): a matplotlib Text object
        box_params (dict): box parameter dict
    Returns:
        same as input
    """
    if box_params['visible'] is False:
        return obj_title
    else:
        bbox_properties = {
            'visible': True,
            'edgecolor': box_params['color']['edge'],
            'facecolor': box_params['color']['face'],
            'linestyle': box_params['line']['style'],
            'linewidth': box_params['line']['width'],
            'zorder': box_params['which_layer'],
            'fill': box_params['fill'],
            'joinstyle': box_params['join_style'],
            'clip_on': box_params['tight'],
            'capstyle': box_params['cap_style']
        }
        pyplot.setp(obj_title, bbox=bbox_properties)
        return obj_title
