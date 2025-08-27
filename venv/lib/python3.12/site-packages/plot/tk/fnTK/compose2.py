"""
Compose two function with single argument into one function
"""


def compose2(f1, f2):
    """Compose two function with single argument into one function

    Args:
        f1 (object): function 1
        f2 (object): function 2

    Returns:
        another function f2(f1(_))
    """
    return lambda x: f2(f1(x))
