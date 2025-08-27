"""
Fine-tune matrix plot aspect ratio
"""
from typing import Dict


def set_aspect_ratio(obj_axis):
    # type: (Tuple) -> object
    """Fine-tune matrix plot aspect ratio

    Args:
        obj_axis (object): a matplotlib axis object

    Returns:
        same as inputs
    """
    obj_axis.set_aspect(
        'auto', adjustable="box-forced", anchor="SW")
    return
