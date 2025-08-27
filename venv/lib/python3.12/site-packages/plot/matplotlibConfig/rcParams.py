"""
A new set of rcParams for matplotlib
"""
from typing import Dict


def rcParams(params):
    # type: (Dict) -> Dict
    """Return a new set of rcParams"""

    ooo = {
        "font.family": "sans-serif",
        "mathtext.fontset": "stixsans",
        "xtick.major.size": 5,
        "ytick.major.size": 5,
        "xtick.major.width": 2,
        "ytick.major.width": 2,
        "xtick.minor.size": 2,
        "ytick.minor.size": 2,
        "xtick.minor.width": 2,
        "ytick.minor.width": 2,
        "xtick.labelsize": 25,
        "ytick.labelsize": 25,
    }
    if params['global']['deps']['latex'] is True:
        ooo['text.usetex'] = True
        ooo['text.latex.unicode'] = True
        ooo['text.latex.preamble'] = ['\\boldmath']
    return ooo
