"""
Return the shape of the input list
"""
from typing import Any, List


def shape(a):
    # type: (Any) -> List
    """Return the shape of the input list

    Args:
        a (list): input list

    Returns:
        a list containing the number elements
        along each dimension
    """
    def aux(a, accum):
        # type: (List, List) -> List
        if isinstance(a, list):
            if len(a) == 0:
                return accum + [0]
            else:
                return aux(a[0], accum + [len(a)])
        else:
            return accum

    if isinstance(a, list):
        return aux(a, [])
    else:
        return []
