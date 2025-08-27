"""
Concatenate many data files into one big array
"""
import os
import numpy
from .readDataFile import readDataFile


def readDataFiles(inputs, dtype, skiprows=0):
    """Read many inputs and return a concatenated array

    Args:
        inputs (list): a list of file names
        dtype (str): input data type

    Returns:
        an ndarray
    """
    data_list = []
    for f in inputs:
        data_list.append(readDataFile(f, dtype, skiprows))
    return numpy.concatenate(data_list, axis=0)
