"""
Make adjustments to figure axes
"""
from typing import Dict
from ..tk.fnTK import compose
from ..tk.importTK import subimport
import os


def finetune(params):
    # type: (Dict) -> Dict
    """Adjust figure/axes

    Adjust global and local axes.

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    here = os.path.dirname(os.path.realpath(__file__))
    modules = subimport(here, "plot.finetune")
    apps = [m.main for m in modules]
    aux = compose(apps)
    return aux(params)
