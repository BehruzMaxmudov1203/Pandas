"""
Return a combine function of
all necessary operations for creating the figure
"""
from typing import Callable, Dict
from .tk.fnTK import compose
from .apps import draw
from .finetune import finetune
from .canvas import create as create_canvas
from .io.output import saveFigure


def workflow(params):
    # type: (Dict) -> Callable
    """Combine all necessary functions into one

    Args:
        params (dict): plotting parameter dictionary
    Returns:
        a function
    """
    aux = compose([
        create_canvas,
        draw,
        finetune,
        saveFigure
        ])
    return aux(params)
