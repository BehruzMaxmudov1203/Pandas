"""
Convert a user configuration dictionary to
an internal parameter dictionary.
"""
from typing import Dict
import copy


def convert_to_internal(params):
    # type: (Dict) -> Dict
    """Convert to "plot" internal dictionary.

    use the internal key defined by params["__"]
    as the new key.

    Args:
        params (dict | list): user configuration dictionary/list

    Returns:
        A new dictionary with new keys.
    """
    if isinstance(params, list):
        return [convert_to_internal(x) for x in params]
    else:
        ooo = dict()
        for k in params.keys():
            if k == "v":
                return params["v"]
            elif isinstance(params[k], dict):
                new_key = params[k]["__"]
                ooo[new_key] = convert_to_internal(params[k])
            elif (isinstance(params[k], list) and
                    isinstance(params[k][0], dict)):
                ooo[k] = convert_to_internal(params[k])
            else:
                continue
        return ooo
