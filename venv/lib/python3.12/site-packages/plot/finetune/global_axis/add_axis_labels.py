"""
Add labels to the global axis
"""
from typing import Dict
from ...tk.matplotlibTK.axis.label import alter_axis_label


def add_axis_labels(params):
    # type: (Dict) -> Dict
    """Add labels to the global axis

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for k in ['x', 'y']:
        alter_axis_label(
            params['internal']['canvas']['global_axis'],
            k,
            params['global']['figure']['axis']['label']['content'][k],
            params['global']['figure']['axis']['label']['font_size'][k],
            params['global']['figure']['axis']['label']['padding'][k]
        )
    return params
