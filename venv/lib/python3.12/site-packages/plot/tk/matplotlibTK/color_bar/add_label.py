"""
Add color bar label
"""


def add_label(obj, label):
    """Add color bar label

    Args:
        obj (object): a ``matplotlib.colorbar.Colorbar`` object
        label (str): label for the color bar
    Returns:
        same as input
    """
    if label is not None:
        obj.set_label(label)
    return obj
