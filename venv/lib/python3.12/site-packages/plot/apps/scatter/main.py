"""
Draw many scatter series
"""
from typing import List, Dict
from ...io.input.extract_data import extract_data
from ...io.input.extract_data_error_bar import extract_data_error_bar
from .draw_one import draw_one
from ...io.input.readFileOrList import readFileOrList
from .._tk import append_addon
import numpy


def main(obj_axis, p):
    # type: (Dict) -> Dict
    """Draw a scatter plot

    Args:
        obj_axis(object): axis for plotting
        p (dict): parameters

    Returns:
        same as input
    """
    data = readFileOrList(p['file'], p['values'], p['skip_rows'])
    if data is None:
        return (None, None, None)
    else:
        XY = extract_data(data, p)
        return draw_one(obj_axis, XY, p)
