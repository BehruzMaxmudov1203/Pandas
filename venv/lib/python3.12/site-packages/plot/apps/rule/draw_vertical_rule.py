"""
Draw a vertical rule
"""
from typing import Dict


def draw_vertical_rule(obj_axis, p, p_rule):
    # type: (object, Dict) -> object
    """Draw a vertical rule

    Args:
        obj_axis (object): a matplotlib axis object
        p (dict): parameters
        p_rule (dict): styles of the rule

    Returns:
        a matplotlib.patches.Polygon object
    """
    return obj_axis.axvline(
        p['at'],
        ymin=p['min'],
        ymax=p['max'],
        alpha=p_rule['opacity'],
        color=p_rule['color'],
        linestyle=p_rule['line']['style'],
        linewidth=p_rule['line']['width'],
        zorder=p_rule['which_layer']
        )
