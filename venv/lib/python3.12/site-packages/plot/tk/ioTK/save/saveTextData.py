"""
Save data array in text format
"""
from numpy import ndarray
import numpy


def saveTextData(file_name, data, fmt):
    """Save data array in text format

    Args:
        file_name (str): output file name
        data (ndarray): numpy ndarray data
        fmt (str): format string, e.g. "%.2e"
    """
    numpy.savetxt(file_name, data, fmt=fmt)
