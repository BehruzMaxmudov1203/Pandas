"""
Wrap an object by n layers of list
"""
from typing import Any, List


def wrap(x, n):
    # type: (Any, int) -> List
    """Wrap any object by n layers of list
    """
    if n > 0:
        return wrap([x], n - 1)
    elif n == 0:
        return x
    else:
        return x
