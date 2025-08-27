"""
Read numpy npy data
"""
import numpy
from typing import AnyStr
from numpy import ndarray


def readNpy(file_name):
    # type: (AnyStr) -> ndarray
    """Ready numpy npy data file

    Args:
        file_name (str): input file name

    Returns:
        numpy ndarray data
    """
    return numpy.load(file_name)
