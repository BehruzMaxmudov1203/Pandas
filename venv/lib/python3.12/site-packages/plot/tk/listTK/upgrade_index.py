"""
upgrade a low dimensional index to a higher one
"""
from typing import List


def upgrade_index(index, new_dim):
    # type: (List, int) -> List
    """Upgrade a low dimensional index to a higher one

    Args:
        index (List): a list of integers
        new_dim (int): the new dimension

    Returns:
        a new index list
    """
    if len(index) >= new_dim:
        return index
    else:
        return upgrade_index(index + [0], new_dim)
