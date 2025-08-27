"""
Set the color for each line data entry.
"""
from typing import Dict
import copy
from .choose_color import choose_color


def set_color(params):
    # type: (Dict) -> Dict
    """
    Set the color for each line data entry.
    Convert integers to their corresponding default colors
    if necessary

    Args:
        params (dict): internal plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    # counter for each line to be plotted
    # within each panel
    counter = dict()
    fields = ['line']

    def get_color(i: int, panel_id: list):
        if (panel_id in params['local'] and
                params['local'][panel_id]['colors'] is not None):
            return choose_color(i, params['local'][panel_id]['colors'])
        else:
            return choose_color(i, params['global']['colors'])

    def set_color(val, local_id: int, which_panel: list):
        if val is None:
            return get_color(local_id, which_panel)
        elif isinstance(val, int):
            return get_color(val, which_panel)
        elif isinstance(val, list):
            return tuple(val)
        else:
            return val

    def aux(d: dict, local_id: int, which_panel: list):
        for k in d.keys():
            if k == "color":
                if isinstance(d["color"], dict):
                    for item in d["color"].keys():
                        d["color"][item] = set_color(
                            d["color"][item], local_id, which_panel)
                else:
                    d["color"] = set_color(d["color"], local_id, which_panel)
            else:
                if isinstance(d[k], dict):
                    d[k] = aux(d[k], local_id, which_panel)
                elif isinstance(d[k], list) and isinstance(d[k][0], dict):
                    d[k] = [aux(x, local_id, which_panel) for x in d[k]]
                else:
                    continue
        return d

    for p in params['data']:
        p = aux(p, p["local_id"], p["which_panel"])

    return params
