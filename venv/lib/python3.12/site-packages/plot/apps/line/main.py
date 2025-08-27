"""
Draw lines (with error bars if defined)
"""
from typing import List, Dict
from ...io.input.extract_data import extract_data
from ...io.input.extract_data_error_bar import extract_data_error_bar
from .draw_one_line import draw_one_line
from ...io.input.readFileOrList import readFileOrList
from .._tk import append_addon
import numpy


def main(obj_axis, p):
    # type: (Dict) -> Dict
    """Draw lines

    Draw lines, with error bars if defined.

    Args:
        obj_axis (object): matplotlib Axis object
        p (dict): parameters for one line

    Returns:
        ("legend", line_object, legend_label)
    """
    data = readFileOrList(p['file'], p['values'], p['skip_rows'])
    if data is None:
        return (None, None)
    else:
        XY = extract_data(data, p)
        x_bars, y_bars = extract_data_error_bar(data, p)
        return draw_one_line(
            obj_axis, XY, x_bars, y_bars, p)
