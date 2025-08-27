"""
Set axis tick width
"""
from typing import Dict


def set_axis_tick_width(params):
    # type: (Dict) -> Dict
    """Set the axis width

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
                    width=p['tick'][m]['width'][k])

    return params
