"""
Set axis tick direction
"""
from typing import Dict


def set_axis_tick_direction(params):
    # type: (Dict) -> Dict
    """Set the axis direction

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id, p in params['local'].items():
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['x', 'y']:
            attr = "get_{}axis".format(k)
            ax = getattr(obj_axis, attr)()
            for m in ['major', 'minor']:
                ax.set_tick_params(
                    which=m,
                    direction=p['tick'][m]['direction'][k])

    return params
