"""
Set the axis range
"""
from typing import Dict


def set_axis_range(params):
    # type: (Dict) -> Dict
    """Set the axis range

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id, p in params['local'].items():
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['x', 'y']:
            attr = "get_{}lim".format(k)
            minmax = list(getattr(obj_axis, attr)())
            new_min = p['axis']['range']['min'][k]
            new_max = p['axis']['range']['max'][k]

            if new_min is not None:
                minmax[0] = new_min
            else:
                pass

            if new_max is not None:
                minmax[1] = new_max
            else:
                pass

            method = "set_{}lim".format(k)
            getattr(obj_axis, method)(minmax)

    return params
