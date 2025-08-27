"""
Tighten the axis range to match data
"""
from typing import Dict


def tighten_panel_axis_range(params):
    # type: (Dict) -> Dict
    """Tighten the axis range to match data

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id, p in params['local'].items():
        panel_id = p['which_panel']
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['x', 'y']:
            if p['axis']['range']['tight'][k] is True:
                prop = "set_{}lim".format(k)
                if panel_id in params['internal']['panel']['minmax']:
                    values = params['internal']['panel']['minmax'][panel_id][k]
                    getattr(obj_axis, prop)(*values)
                else:
                    pass
    return params
