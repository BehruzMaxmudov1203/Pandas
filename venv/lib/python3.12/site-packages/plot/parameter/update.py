"""
Return an updated parameter dictionary based on
user input dictionary.
"""
from typing import AnyStr, Dict
import os
from ..io.input.parse import parse


def update(user_config_file):
    # type: (AnyStr) -> Dict
    """Return an updated parameter dictionary

    Parse user configuration file and use the information
    to update the default parameter dictionary.

    Args:
        user_config_file (str): user configuration file name

    Returns:
        an updated parameter dictionary
    """
    here = os.path.dirname(os.path.realpath(__file__))
    default_config_file = os.path.join(here, "all.json")
    return parse(user_config_file, default_config_file)
