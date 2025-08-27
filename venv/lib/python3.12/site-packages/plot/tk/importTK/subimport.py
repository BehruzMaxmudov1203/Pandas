"""
import all sub-modules residing in a directory
"""
from typing import List
import re
import os
import importlib


def subimport(path, parent_module):
    # type: (AnyStr, AnyStr) -> List
    """Import all sub-modules

    Import all sub-modules inside a directory

    Args:
        path (str): path to the target directory
        parent_module (str): absolute module name for that path

    Returns:
        a list of modules
    """
    apps = []
    for d in os.listdir(path):
        if (os.path.isdir(os.path.join(path, d)) and
                re.match("^[a-zA-Z]+.*$", d)):
            m = importlib.import_module(
                ".{}".format(d),
                package=parent_module)
            apps.append(m)
    return apps
