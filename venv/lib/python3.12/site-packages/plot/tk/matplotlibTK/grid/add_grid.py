"""
Add grids to a plot
"""
from typing import AnyStr
import matplotlib.pyplot


def add_grid(
        obj_axis,           # type: object
        obj_figure,         # type: object
        show_grid,          # type: bool
        which_ticks,        # type: AnyStr
        which_axis,         # type: AnyStr
        grid_line_style,    # type: AnyStr
        grid_line_width,    # type: int
        grid_line_color,    # type: AnyStr
        grid_line_opacity,  # type: float
        grid_z_order        # type: int
        ):
    """Add grids to a plot

    Args:
        obj_axis (object): matplotlib Axes object
        obj_figure (object): matplotlib figure object
        show_grid (bool): whether to show the grid
        which_ticks (str): "major", "minor" or "both"
        which_axis (str): "both", "x", or "y"
        grid_line_style (str): "-", "--", "-.", ":", "None", " " or ""
        grid_line_opacity (float): opacity
        grid_z_order (int): layer order

    Returns:
        True
    """
    object_old_axis = obj_figure.gca()
    obj_figure.sca(obj_axis)  # switch current axis to new axis object

    matplotlib.pyplot.grid(
        show_grid,
        which_ticks,
        which_axis,
        axes=obj_axis,
        figure=obj_figure,
        linestyle=grid_line_style,
        linewidth=grid_line_width,
        color=grid_line_color,
        alpha=grid_line_opacity,
        zorder=grid_z_order
    )

    obj_figure.sca(object_old_axis)  # switch back to old axis
    return True
