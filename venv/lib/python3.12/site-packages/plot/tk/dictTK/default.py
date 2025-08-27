"""
Replace all the "v" field of
the input dictionary with the
default value (i.e. the first entry of the  list).

Example:
{"k": {"v": [1,2,3]}} will be changed to {"k": {"v": 1}}
"""
from typing import Dict
import copy


def default(d):
    # type: (Dict) -> Dict
    """Return a new dictionary with default values

    Assuming the dictionary has "v" field value [v1, v2, ...],
    the returned dictionary will have value "v": v1

    Args:
        d (dict): input dictionary with structure like {"k": {"v": [1,2,3]}}

    Returns:
        a new dictionary with default values.
    """
    ooo = copy.deepcopy(d)
    for k in d.keys():
        if k == "v":
            ooo["v"] = d[k][0]
        elif isinstance(d[k], dict):
            ooo[k] = default(d[k])
        elif (isinstance(d[k], list) and
                isinstance(d[k][0], dict)):
            ooo[k] = [default(x) for x in d[k]]
        else:
            continue
    return ooo
