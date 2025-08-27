"""
Transpose data
"""
from numpy import ndarray
import numpy


def transpose(data, act=True):
    # type:(ndarray) -> ndarray
    """Transpose data

    Args:
        data (ndarray): input data
        act=True (bool): whether to do the transposing

    Returns:
        a new ndarray
    """
    if act:
        return numpy.transpose(data)
    else:
        return data
