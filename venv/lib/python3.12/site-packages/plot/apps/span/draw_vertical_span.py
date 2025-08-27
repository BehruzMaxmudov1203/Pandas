"""
Draw a vertical span
"""
from typing import Dict


def draw_vertical_span(obj_axis, p, p_span):
    # type: (object, Dict) -> object
    """Draw a vertical span

    Args:
        obj_axis (object): a matplotlib axis object
        p (dict): parameters for locations of the span
        p_span (dict): styles of the span

    Returns:
        a matplotlib.patches.Polygon object
    """
    return obj_axis.axvspan(
        p['min'], p['max'],
        ymin=p['bottom'],
        ymax=p['top'],
        alpha=p_span['opacity'],
        facecolor=p_span['color']['face'],
        edgecolor=p_span['color']['edge'],
        linestyle=p_span['line']['style'],
        linewidth=p_span['line']['width'],
        fill=p_span['filled'],
        zorder=p_span['which_layer']
        )
