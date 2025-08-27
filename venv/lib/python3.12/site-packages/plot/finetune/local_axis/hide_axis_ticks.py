"""
Hide axis ticks at top, bottom, left or right
"""
from typing import Dict


def hide_axis_ticks(params):
    # type: (Dict) -> Dict
    """SHide axis ticks at top, bottom, left or right

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
                if k == 'x':
                    ax.set_tick_params(
                        which=m,
                        top=p['tick'][m]['show']['top'],
                        bottom=p['tick'][m]['show']['bottom'])
                else:
                    ax.set_tick_params(
                        which=m,
                        left=p['tick'][m]['show']['left'],
                        right=p['tick'][m]['show']['right'])

    return params
