"""
Draw a horizontal rule
"""
from typing import Dict


def draw_horizontal_rule(obj_axis, p, p_rule):
    # type: (object, Dict) -> object
    """Draw a horizontal rule

    Args:
        obj_axis (object): a matplotlib axis object
        p (dict): parameters
        p_rule (dict): styles of the rule

    Returns:
        a matplotlib.patches.Polygon object
    """
    return obj_axis.axhline(
        p['at'],
        xmin=p['min'],
        xmax=p['max'],
        alpha=p_rule['opacity'],
        color=p_rule['color'],
        linestyle=p_rule['line']['style'],
        linewidth=p_rule['line']['width'],
        zorder=p_rule['which_layer']
        )
