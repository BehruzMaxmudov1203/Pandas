"""
Add global axes to the entire figure.
"""
from typing import Dict
import matplotlib.pyplot
from ...tk.listTK import upgrade_index
from ...tk.listTK import append


def global_axis(params):
    # type: (Dict) -> Dict
    """Add global axes to the figure

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        an updated dictionary with a new field ['canvas']['global_axes']
    """
    dim = params['internal']['figure_dimension']
    obj_axis = params['internal']['canvas']['figure'].add_subplot(
                1, 1, 1,
            )

    # make axis background transparent
    obj_axis.patch.set_alpha(0)

    # turn off the extra axis's tick labels
    matplotlib.pyplot.setp(obj_axis.get_xticklabels(), visible=False)
    matplotlib.pyplot.setp(obj_axis.get_yticklabels(), visible=False)
    obj_axis.set_xticks([])
    obj_axis.set_yticks([])

    # Make the frame line transparent
    for child in obj_axis.get_children():
        if isinstance(child, matplotlib.spines.Spine):
            child.set_color((0, 0, 0, 0))

    # append the global axis to the first entry
    # and append None to the others
    axes = params['internal']['canvas']['axes']
    for i in range(params['global']['figure']['rows']):
        for j in range(params['global']['figure']['columns']):
            index = upgrade_index([i, j], dim)
            if i == 0 and j == 0:
                axes = append(axes, index, obj_axis)
            else:
                axes = append(axes, index, None)
    params['internal']['canvas']['global_axis'] = obj_axis
    return params
