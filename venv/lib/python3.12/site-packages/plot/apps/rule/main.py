"""
Draw straight lines
"""
from typing import List, Dict
from .draw_horizontal_rule import draw_horizontal_rule
from .draw_vertical_rule import draw_vertical_rule
from .._tk import append_addon
from ...tk.matplotlibTK.legend import format_legend_label
import numpy


def main(obj_axis, p):
    # type: (Dict) -> Dict
    """Draw straight lines

    Args:
        obj_axis(object): object for plotting
        p (dict): parameters
    Returns:
        ("legend", object, legend_label)
    """
    fn = {"horizontal": draw_horizontal_rule, "vertical": draw_vertical_rule}
    for k in ['horizontal', 'vertical']:
        if p['rule'][k]['at'] is None:
            continue
        else:
            if isinstance(p['rule'][k]['at'], str):
                p['rule'][k]['at'] = numpy.loadtxt(p['rule'][k]['at'])
            obj_span = fn[k](obj_axis, p['rule'][k], p['rule'])
            legend_label = format_legend_label(p['legend']['content'])
            return ("legend", obj_span, legend_label)
    return (None, None, None)
