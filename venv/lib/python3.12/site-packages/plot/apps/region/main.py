"""
Draw regions
"""
from typing import List, Dict
from ...io.input.extract_data import extract_data
from ...io.input.extract_data_error_bar import extract_data_error_bar
from .draw_one_region import draw_one_region
from ...io.input.readFileOrList import readFileOrList
from .._tk import append_addon
import numpy


def main(obj_axis, p):
    # type: (Dict) -> Dict
    """Draw regions

    Args:
        obj_axis(object): axis for plotting
        p (dict): a complete parameter dictionary

    Returns:
        ("legend", object, legend_label)
    """
    data = readFileOrList(p['file'], p['values'], p['skip_rows'])
    if data is None:
        return (None, None, None)
    else:
        XY1Y2 = extract_data(data, p)
        return draw_one_region(
            obj_axis, XY1Y2, p)
