"""
Adjust the global figure axis
"""
from typing import Dict
from ...tk.fnTK import compose
from .add_axis_labels import add_axis_labels
from .add_figure_title import add_figure_title
from .add_text import add_text


def main(params):
    # type: (Dict) -> Dict
    """Adjust global parameters

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    aux = compose([
        add_axis_labels,
        add_figure_title,
        add_text,
        ])
    return aux(params)
