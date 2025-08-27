"""
Wrap the value of a nested dictionary
with a new field {"v": value}
"""
from typing import Dict
import copy


def wrap_value(d):
    # type: (Dict) -> Dict
    """Wrap the value field

    Add a new field "v", which
    contains the actual value
    under the key.

    Args:
        d (dict): input dictionary

    Returns:
        a new dictionary with values wrapped
        inside "v" fields
    """
    ooo = copy.deepcopy(d)
    for k in d.keys():
        if isinstance(d[k], dict):
            ooo[k] = wrap_value(d[k])
        elif (isinstance(d[k], list) and
                isinstance(d[k][0], dict)):
            ooo[k] = [wrap_value(x) for x in d[k]]
        else:
            ooo[k] = {"v": d[k]}
    return ooo
