"""
Add grids to the local axes
"""
from typing import Dict
from ...tk.matplotlibTK.grid import add_grid


def add_grid_lines(params):
    # type: (Dict) -> Dict
    """Add grids to the local axes

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    obj_figure = params['internal']['canvas']['figure']
    for panel_id, p in params['local'].items():
        if p['grid']['show'] is True:
            obj_axis = params['internal']['canvas']['axes'][panel_id]
            add_grid(
                obj_axis, obj_figure, True,
                which_ticks=p['grid']['which_ticks'],
                which_axis=p['grid']['which_axis'],
                grid_line_style=p['grid']['line']['style'],
                grid_line_width=p['grid']['line']['width'],
                grid_line_color=p['grid']['line']['color'],
                grid_line_opacity=p['grid']['line']['opacity'],
                grid_z_order=p['grid']['which_layer']
            )
        else:
            continue
    return params
