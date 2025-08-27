"""
Return a properly formated legend label
"""
from typing import AnyStr
import matplotlib.pyplot


def format_legend_label(legend_label):
    # type: (AnyStr) -> AnyStr
    """Return a properly formated legend label

    Args:
        legend_label (str): list of legend labels (strings)

    Returns:
        the input axis object
    """
    if legend_label is not None:
        return legend_label
    else:
        # legend labels staring with '_' are ignored
        #  see matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
        return None
