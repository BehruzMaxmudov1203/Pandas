"""
reduce
"""
from .tail import tail


def reduce(merge, collection, base):
    """reduce

    Args:
        merge (function): a function that merges two objects
        collection (list): a list of objects
        base (object): a base object
    Returns:
        a reduced object
    """
    if len(collection) == 0:
        return base
    else:
        return reduce(merge, tail(collection), merge(base, collection[0]))
