"""
Update the second dictionary with
the contents of the first dictionary.
"""
from typing import Dict
import copy


def update(src, target):
    """Recursively update.

    Update the target using
    content from the src.
    Items from src which are not in
    target will be discarded.
    A easy way to remember the priority
    is "1st argument has #1 priority".

    Args:
        src (dict | list): new information source
        target (dict | list): target dictionary to be updated

    Returns:
        a new dictionary with updated entries.
    """
    if (isinstance(target, list) and
            isinstance(src, list)):
        if len(target) == len(src):
            return [update(src[i], target[i])
                    for i in range(len(src))]
        else:
            return [update(src[i], target[0])
                    for i in range(len(src))]
    else:
        ooo = copy.deepcopy(target)
        for k in src.keys():
            if k in target.keys():  # update
                if (isinstance(target[k], dict) and
                        isinstance(src[k], dict)):
                    ooo[k] = update(src[k], target[k])
                elif (isinstance(target[k], list) and
                        isinstance(src[k], list) and
                        isinstance(target[k][0], dict)):
                    ooo[k] = update(src[k], target[k])
                else:
                    ooo[k] = src[k]
            else:   # irrelevant items from src
                print("Error hint: unknown key: ", k)
                continue
        return ooo
