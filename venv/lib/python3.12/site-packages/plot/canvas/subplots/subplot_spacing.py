"""
Adjust the spacing between subplots.
"""
from typing import Dict


def subplot_spacing(params):
    # type: (Dict) -> Dict
    """Adjust subplot plots' inter-spacing

    Args:
        params (dict): parameter dictionary

    Returns:
        a new dictionary whose ['canvas']['figure']
        has updated horizontal and vertical spacing
        between subplots
    """
    params['internal']['canvas']['figure'].subplots_adjust(
        hspace=params['global']['figure']['subplot']['spacing']['vertical'],
        wspace=params['global']['figure']['subplot']['spacing']['horizontal'])
    return params
