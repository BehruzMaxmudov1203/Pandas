"""
Upgrade from a low-dimensional list to a high-dimensional list
"""
from typing import List, Any
from .shape import shape
from .wrap import wrap


def upgrade_dimension(a, new_dim):
    # type: (List, int) -> List
    """Return a higher dimensional list

    Args:
        a (list): input list
        new_dim (int): new number of dimension

    Returns:
        a new list with dimension: new_dim
    """
    if not isinstance(a, list):
        return a
    else:
        a_shape = shape(a)
        diff = new_dim - len(a_shape)
        if diff < 0:
            return a
        else:
            if len(a) == 0:
                return wrap(a, diff)
            elif isinstance(a[0], list):
                return [upgrade_dimension(a[i], new_dim - 1)
                        for i in range(len(a))]
            else:
                return [wrap(a[i], diff) for i in range(len(a))]
