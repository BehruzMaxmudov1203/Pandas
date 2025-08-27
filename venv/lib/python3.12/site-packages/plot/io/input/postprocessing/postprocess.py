"""
Postprocess the internal parameter dictionary
"""
from typing import Dict
from ....tk.fnTK import compose
from .make_local_dict import make_local_dict
from .format_panel_index import format_panel_index
from .set_data_id import set_data_id
from .set_color import set_color
from .set_data_columns import set_data_columns
from .set_panel_minmax import set_panel_minmax
from .initialize_panel_legend import initialize_panel_legend
from .initialize_panel_color_bar import initialize_panel_color_bar


def postprocess(params):
    # type: (Dict) -> Dict
    """Postprocess the internal parameter dictionary

    Args:
        params(dict): internal parameter dictionary

    Returns:
        enhanced internal parameter dictionary
    """
    aux = compose([
        format_panel_index,
        make_local_dict,
        set_data_id,
        set_color,
        set_data_columns,
        set_panel_minmax,
        initialize_panel_legend,
        initialize_panel_color_bar
        ])
    return aux(params)
