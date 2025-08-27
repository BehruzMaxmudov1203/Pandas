"""
Return all the indexes for an array
"""
from typing import List, Tuple
import numpy


def all_indexes(shape):
    # (Tuple) -> List[Tuple]
    """Return all the indexes for an array

    Args:
        shape (tuple): a tuple representing array shape

    Returns:
        a list of all possible indexes (tuples)
    """
    def tail(xs): return xs[1:]

    def aux(shape, accum):
        # type: (Tuple, List) -> List
        if len(shape) == 0:
            return accum
        else:
            return aux(
                tail(shape),
                [xs + [j] for xs in accum
                 for j in range(shape[0])])
    return [tuple(x) for x in aux(shape, [[]])]
