"""
Take many functions and compose
"""
from typing import List, Callable, Optional
from .reduce import reduce
from .compose2 import compose2


def compose(functions):
    # type: (List[Callable]) -> Callable
    """Compose functions

    Args:
        functions (list): a list of functions

    Returns:
        a new function with combined effects from all inputs
    """
    return reduce(compose2, functions, lambda a: a)
