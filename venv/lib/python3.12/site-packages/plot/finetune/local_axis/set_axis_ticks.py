"""
Set axis ticks
"""
from typing import Dict


def set_axis_ticks(params):
    # type: (Dict) -> Dict
    """Set the axis ticks

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
                new_ticks = p['tick'][m]['set'][k]
                if new_ticks is not None:
                    ax.set_ticks(new_ticks,  minor=(m == 'minor'))
                else:
                    pass

    return params
