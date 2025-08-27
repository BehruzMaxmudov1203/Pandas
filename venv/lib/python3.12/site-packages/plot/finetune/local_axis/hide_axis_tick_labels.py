"""
Hide axis tick labels at top, bottom, left or right
"""
from typing import Dict


def hide_axis_tick_labels(params):
    # type: (Dict) -> Dict
    """SHide axis tick labels at top, bottom, left or right

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
                        labeltop=p['tick_label'][m]['show']['top'],
                        labelbottom=p['tick_label'][m]['show']['bottom'])
                else:
                    ax.set_tick_params(
                        which=m,
                        labelleft=p['tick_label'][m]['show']['left'],
                        labelright=p['tick_label'][m]['show']['right'])

    return params
