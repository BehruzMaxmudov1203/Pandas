"""
Save the matplotlib 'Figure' object into
an image file.
"""
from matplotlib.figure import Figure


def saveFigure(params):
    # type:(Dict) -> bool
    """Save figure

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    obj_figure = params['internal']['canvas']['figure']
    p = params['global']['figure']['save']
    for f_out in params['global']['figure']['outputs']:
        obj_figure.savefig(
            f_out,
            bbox_inches=p['bounding_box'],
            dpi=p['dpi'],
            pad_inches=p['padding'],
            transparent=p['transparent'],
        )
    return params
