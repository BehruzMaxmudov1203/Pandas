"""
Read data in text format
"""
from typing import AnyStr
from numpy import ndarray
import numpy


def readTextData(file_name, dtype_str, skip_rows=0):
    # type: (AnyStr, AnyStr) -> ndarray
    """Read data in text format and return an array

    Supported dtype: "int", "float"

    Args:
        file_name (str): input file name
        dtype_str (str): data type as string
        skip_rows (int): number of rows to skip
            (default: 0)

    Returns:
        a numpy ndarray
    """
    return numpy.loadtxt(
        file_name,
        dtype=eval(dtype_str),
        skiprows=skip_rows)
