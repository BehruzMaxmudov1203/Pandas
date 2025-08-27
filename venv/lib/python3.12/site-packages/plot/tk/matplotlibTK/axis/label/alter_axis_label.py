"""
Alter the axis label
"""
from typing import AnyStr, Any


def alter_axis_label(
        obj_axis,         # type: object
        which_axis,       # type: AnyStr
        label_content,    # type: AnyStr
        label_font_size,  # type: int
        label_padding     # type: int
        ):
    # type: (...) -> Tuple[bool, AnyStr]
    """Alter the axis label

    Args:
        obj_axis (object): matplotlib axis object

    Returns:
        (True, "") if succeeded
        (False, "error message") if not
    """
    if which_axis == "x":
        obj_axis.set_xlabel(
            label_content,
            fontsize=label_font_size,
            labelpad=label_padding)
    elif which_axis == "y":
        obj_axis.set_ylabel(
            label_content,
            fontsize=label_font_size,
            labelpad=label_padding)
    else:
        msg = "ERROR HINT: 'axis_name' argument should be 'x' or 'y'\n"
        msg += "\tYour 'axis_name' = \"{0}\"".format(axis_name)
        return (False, msg)

    return (True, "")
