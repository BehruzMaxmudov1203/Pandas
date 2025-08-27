"""
Add local axis labels
"""
from typing import Dict
from ...tk.matplotlibTK.axis.label import alter_axis_label


def add_local_axis_labels(params):
    # type: (Dict) -> Dict
    """Add local axis labels

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id, p in params['local'].items():
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['x', 'y']:
            if p['axis']['label']['content'][k] is not None:
                alter_axis_label(
                    obj_axis,
                    k,
                    p['axis']['label']['content'][k],
                    p['axis']['label']['font']['size'][k],
                    p['axis']['label']['padding'][k]
                )
            else:
                pass

    return params
