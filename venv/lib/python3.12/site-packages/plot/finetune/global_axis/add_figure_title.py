"""
Add figure title
"""
from typing import Dict
import matplotlib.pyplot as pyplot
from .add_figure_title_box import add_figure_title_box
from .set_figure_title_anchor import set_figure_title_anchor


def add_figure_title(params):
    # type: (Dict) -> Dict
    """Add labels to the global axis

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    if params['global']['figure']['title']['content'] is None:
        return params
    obj_figure = params['internal']['canvas']['global_axis']
    title_params = params['global']['figure']['title']
    font_properties = {
        'visible': title_params['visible'],
        "size": title_params['font']['size'],
        "weight": title_params['font']['weight'],
        "color": title_params['font']['color'],
        "alpha": title_params['font']['opacity'],
        "backgroundcolor": title_params['background_color'],
        "family": title_params['font']['family'],
        "style": title_params['font']['style'],
        "zorder": title_params['which_layer'],
        "rotation": title_params['rotation'],
        "linespacing": title_params['line_spacing']
    }

    obj_title = obj_figure.set_title(
        params['global']['figure']['title']['content'],
        loc=title_params['alignment']['horizontal'],
        )

    pyplot.setp(obj_title, **font_properties)
    add_figure_title_box(obj_title, title_params['box'])
    set_figure_title_anchor(obj_title, title_params['anchor'])
    return params
