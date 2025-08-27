
"""
Draw span regions
"""
from typing import List, Dict
from .draw_horizontal_span import draw_horizontal_span
from .draw_vertical_span import draw_vertical_span
from .._tk import append_addon
from ...tk.matplotlibTK.legend import format_legend_label
from ...io.input.readFileOrNumber import readFileOrNumber


def main(obj_axis, p):
    # type: (Dict) -> Dict
    """Draw span regions
    Args:
        obj_axis(object): axis for plotting
        p (dict): parameters

    Returns:
        same as input
    """
    fn = {"horizontal": draw_horizontal_span, "vertical": draw_vertical_span}
    for k in ['horizontal', 'vertical']:
        if ((p['span'][k]['center'] is None) or
                (p['span'][k]['radius'] is None)):
            pass
        else:
            center = readFileOrNumber(p['span'][k]['center'])
            h = readFileOrNumber(p['span'][k]['radius'])
            p['span'][k]['min'] = center - h
            p['span'][k]['max'] = center + h

        if (p['span'][k]['min'] is None) or (p['span'][k]['max'] is None):
            continue
        else:
            obj_span = fn[k](obj_axis, p['span'][k], p['span'])
            legend_label = format_legend_label(p['legend']['content'])
            return ("legend", obj_span, legend_label)
    return (None, None, None)
