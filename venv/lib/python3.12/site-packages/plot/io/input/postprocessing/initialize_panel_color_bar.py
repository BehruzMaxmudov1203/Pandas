"""
Initialize the internal panel color bar
"""
from typing import Dict
from ....tk.arrayTK import all_indexes


def initialize_panel_color_bar(params):
    # type: (Dict) -> Dict
    """Initialize the internal panel color bar

    Args:
        params(dict): plotting parameters

    Returns:
        updated params
    """
    params['internal']['panel']['color_bar'] = dict()
    for p in params['data']:
        if p['color_bar']['show']:
            k = p['color_bar']['which_panel']
            params['internal']['panel']['color_bar'][k] = []
        else:
            pass
    return params
