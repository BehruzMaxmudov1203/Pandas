"""
Refine the properties of legend
"""
from typing import Dict
from ...tk.matplotlibTK.legend import refine_legend


def finetune_legend(params):
    # type: (Dict) -> Dict
    """Refine legend properties

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id in params['internal']['panel']['legend']:
        if panel_id in params['local']:
            legend_params = params['local'][panel_id]['legend']
        else:
            legend_params = params['internal']['default']['local']['legend']

        handles_labels = params['internal']['panel']['legend'][panel_id]
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        refine_legend(obj_axis, handles_labels, legend_params)
    return params
