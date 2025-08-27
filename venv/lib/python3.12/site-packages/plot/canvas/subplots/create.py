"""
Create a figure object
"""
from typing import Dict
import copy
import matplotlib.pyplot
from .subplot_spacing import subplot_spacing
from .global_axis import global_axis
from ...tk.fnTK import compose
from ...tk.listTK import upgrade_dimension
import numpy

def create(params):
    # type: (Dict) -> Dict
    """Create a new figure object

    Args:
        params (dict): plotting parameters

    Returns:
        a parameter dict with a new field "figure"
        which contains the new figure object
    """
    dim = params['internal']['figure_dimension']
    fig, axes = matplotlib.pyplot.subplots(
                nrows=params['global']['figure']['rows'],
                ncols=params['global']['figure']['columns'],
                figsize=(params['global']['figure']['width'],
                         params['global']['figure']['height']),
                sharex=params['global']['figure']['axis']['share']['x'],
                sharey=params['global']['figure']['axis']['share']['y'],
                squeeze=False,
            )
    params['internal']['canvas']['figure'] = fig
    params['internal']['canvas']['axes2D'] = axes
    params['internal']['canvas']['axes'] = upgrade_dimension(
        axes.tolist(), dim)
    params['internal']['canvas']['axes'] = numpy.array(
        params['internal']['canvas']['axes'])

    layout = params['global']['figure']['layout']
    if layout['tight'] is True:
        fig.tight_layout(
            pad=layout['padding']['figure'],
            h_pad=layout['padding']['vertical'],
            w_pad=layout['padding']['horizontal'],
            rect=layout['padding']['rectangle'],
        )

    tweek = compose([subplot_spacing, global_axis])
    tweek(params)

    # change axis spine line width
    # [x.set_linewidth(0) for a in axes for x in a.intervalues() ]
    for i in range(params['global']['figure']['rows']):
        for j in range(params['global']['figure']['columns']):
            for k in ['left', 'right', 'top', 'bottom']:
                axes[i,j].spines[k].set_linewidth(
                    params['global']['figure']['spine']['line']['width'])
    return params
