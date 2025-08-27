"""
Convert the "local" field to a dictionary
"""
from typing import Dict
from ....tk import dictTK


def make_local_dict(params):
    # type: (Dict) -> Dict
    """Convert the "local" field to a dictionary

    Args:
        params (dict): plotting parameters

    Returns:
        an updated params
    """
    new_local = dict()
    for p in params['local']:
        k = p['which_panel']
        new_local[k] = p
    params['local'] = new_local
    return params
