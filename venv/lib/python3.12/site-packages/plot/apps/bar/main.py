"""
Draw bars
"""
from typing import List, Dict
from ...io.input.extract_data import extract_data
from ...io.input.extract_data_error_bar import extract_data_error_bar
from ...io.input.readFileOrList import readFileOrList
from .draw_one_bar_series import draw_one_bar_series
from .._tk import append_addon
import numpy


def main(obj_axis, p):
    # type: (Dict) -> Dict
    """Draw lines

    Draw histogram-like bars with error bars if defined.

    Args:
        obj_axis(object): axis for plotting
        p (dict): parameters for one bar series

    Returns:
        ("legend", obj, legend_label)
    """
    data = readFileOrList(p['file'], p['values'], p['skip_rows'])
    if data is None:
        return (None, None)
    else:
        XY = extract_data(data, p)
        x_bars, y_bars = extract_data_error_bar(data, p)
        return draw_one_bar_series(
            obj_axis, XY, x_bars, y_bars, p)
