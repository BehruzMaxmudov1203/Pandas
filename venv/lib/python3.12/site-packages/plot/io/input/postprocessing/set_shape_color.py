"""
Set the color for each shape plots like bar and span
"""
from typing import Dict
import copy
from .choose_color import choose_color


def set_shape_color(params):
    # type: (Dict) -> Dict
    """Set the color for each shape plots like bar and span

    Args:
        params (dict): internal plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    # counter for each line to be plotted
    # within each panel
    counter = dict()
    p_types = ['bar', 'span']

    def aux(i, panel_id):
        if (panel_id in params['local'] and
                params['local'][panel_id]['colors'] is not None):
            return choose_color(i, params['local'][panel_id]['colors'])
        else:
            return choose_color(i, params['global']['colors'])

    for p in params['data']:
        for kind in p_types:
            for k in ['face', 'edge']:
                if p[kind]['color'][k] is None:
                    p[kind]['color'][k] = aux(p['local_id'], p['which_panel'])
                elif type(p[kind]['color'][k]) == int:
                    # this allows the user to specify
                    # which default color to use
                    p[kind]['color'][k] = aux(
                        p[kind]['color'], p['which_panel'])
                else:
                    pass  # keep user's color choice

    return params
