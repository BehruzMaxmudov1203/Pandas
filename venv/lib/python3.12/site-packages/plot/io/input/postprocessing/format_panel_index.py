"""
Convert value of "which_panel" to proper format
"""
from typing import Dict
from ....tk.listTK import upgrade_index
import copy


def format_panel_index(params, dim=5):
    # type: (Dict, int) -> Dict
    """Convert the value of "panel_index" to proper format

    Example: [0, 0] will be changed to tuple(0, 0, 0, 0)

    Args:
        params (dict): internal parameter dictionary
        dim (int): dimension of the axis matrix

    Return:
        updated internal parameter dictionary
    """
    for k in params:
        if k == "which_panel":
            if params[k] == "_":
                # compute global axis index
                global_axis_index = upgrade_index([0, 0], dim)
                global_axis_index[-1] = 1
                params[k] = tuple(global_axis_index)
            elif params[k] is None:
                params[k] = tuple(upgrade_index([0, 0], dim))
            else:
                params[k] = tuple(upgrade_index(params[k], dim))
        elif isinstance(params[k], dict):
            params[k] = format_panel_index(params[k], dim)
        elif (isinstance(params[k], list) and
                len(params[k]) > 0 and
                isinstance(params[k][0], dict)):
            params[k] = [format_panel_index(obj, dim)
                         for obj in params[k]]
        else:
            continue
    return params
