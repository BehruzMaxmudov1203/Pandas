"""
Read the input and start working
"""
from typing import Dict, AnyStr
import os
import plot.work
import plot.parameter
import matplotlib.pyplot


def run(user_config_file, preview):
    # type: (AnyStr, bool) -> bool
    """Read input and start working

    Args:
        user_config_file (str): file name of user configuration file
        preview (bool): whether to show the preview window

    Returns:
        True of succeeds
    """
    params = plot.parameter.update(user_config_file)

    if len(params.keys()) == 0:
        raise Exception(
            "ERROR HINT: invalid input "
            "configuration file {}".format(user_config_file)
            )
        exit()

    plot.work(params)

    if preview:
        matplotlib.pyplot.show()

    return True
