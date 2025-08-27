"""
Create, draw and save figures based
on user input parameter dictionary.
"""
from typing import Dict
import matplotlib
import matplotlib.pyplot
from .matplotlibConfig import rcParams as new_rc_params
from .workflow import workflow


def work(params):
    # type: (Dict, bool) -> Dict
    """Create, draw, and save figures

    Args:
        params (dict): a dictionary that defines the figure

    Returns:
        updated params
    """
    matplotlib.rcParams.update(new_rc_params(params))
    return workflow(params)
