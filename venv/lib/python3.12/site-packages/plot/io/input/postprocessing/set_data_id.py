"""
Set the order ID (zero-based) for each object to be plotted
within the context of each panel
"""
from typing import Dict
import copy


def set_data_id(params):
    # type: (Dict) -> Dict
    """Set the ID of reach data entry

    Set the order ID (zero-based) for each object to be plotted
    within the context of each panel

    Args:
        params (dict): internal plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    # counter for each line to be plotted
    # within each panel
    counter = dict()
    for p in params['data']:
        panel_id = p['which_panel']
        if panel_id not in counter:
            counter[panel_id] = 0
        else:
            counter[panel_id] += 1
        p['local_id'] = counter[panel_id]
    return params
