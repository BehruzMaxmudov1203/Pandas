"""
import all sub-modules residing in a directory
and return a dictionary.
"""
from typing import List
import re
import os
import importlib


def subimportDict(path, parent_module):
    # type: (AnyStr, AnyStr) -> List
    """Import all sub-modules

    Import all sub-modules inside a directory

    Args:
        path (str): path to the target directory
        parent_module (str): absolute module name for that path

    Returns:
        a dictionary of modules
    """
    apps = {}
    for d in os.listdir(path):
        if (os.path.isdir(os.path.join(path, d)) and
                re.match("^[a-zA-Z]+.*$", d)):
            m = importlib.import_module(
                ".{}".format(d),
                package=parent_module)
            name = os.path.splitext(os.path.basename(d))[0]
            apps[name] = m
    return apps
