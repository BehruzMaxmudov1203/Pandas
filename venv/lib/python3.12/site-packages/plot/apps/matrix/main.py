"""
Draw matrices
"""
from typing import List, Dict
from .draw_matrix import draw_matrix
from ...io.input.readFileOrList import readFileOrList
import numpy
from .._tk import append_addon


def main(obj_axis, p):
    # type: (Dict) -> Dict
    """Draw matrices

    Draw matrices

    Args:
        obj_axis(object): axis for plotting
        p (dict): parameters

    Returns:
        ("color_bar", obj, legend_label)
    """
    data = readFileOrList(
        p['file'], p['values'], p['skip_rows'],
        transpose=p['matrix']['transpose'])
    if data is None:
        return (None, None, None)
    else:
        obj_matrix = draw_matrix(obj_axis, data, p)
        if p['color_bar']['show']:
            label = p['color_bar']['content']
            return ("color_bar", obj_matrix, label)
        else:
            return (None, None, None)
