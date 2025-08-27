"""
Read a file or just convert an alternative list to numpy array
"""
from typing import AnyStr, List
from numpy import ndarray
from .readDataFile import readDataFile
import numpy
from ...tk.arrayTK import transpose as array_transpose


def readFileOrList(
        file_name,       # type: AnyStr
        data_list,       # type: ndarray
        skip_rows=0,     # type: int
        dtype='float',   # type: AnyStr
        transpose=False  # type: bool
        ):
    # type: (AnyStr, List) -> ndarray
    """Read a file or just convert an alternative list to numpy array

    If both file_name and data_list are given
    then the content of the data file will be returned.

    Args:
        file_name (str): input file name
        data_list (list): a list of numbers
        skip_rows=0 (int): number of rows to skip
        dtype="float" (str): data type of the input
        transpose=False (bool): whether to transpose data

    Returns:
        a numpy ndarray
    """
    if file_name is not None:
        return readDataFile(
            file_name, skip_rows, dtype, transpose)
    elif data_list is not None:
        return array_transpose(numpy.array(data_list), transpose)
    else:
        return None
