"""
Read a file or just a number.
This allow user to specify either a single number
or a file that contains a number
"""
import numpy


def readFileOrNumber(x):
    """Read a file or just a number

    Args:
        x: file name or just a number
    Returns:
        a number (float)
    """
    if isinstance(x, str):
        return numpy.loadtxt(x)
    else:
        return x
