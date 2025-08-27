"""
Read a data file and return the content as array.
"""
from typing import AnyStr
import numpy
from numpy import ndarray
from ...tk.ioTK import read as R
from ...tk.arrayTK import transpose as array_transpose


def readDataFile(
        file_name,       # type: AnyStr
        skip_rows=0,     # type: int
        dtype="float",   # type: str
        transpose=False  # type: bool
        ):
    # type: (...) -> ndarray
    """Read a data file

    Read a data file and return its content as ndarray.

    Args:
        file_name (str): file name
        dtype='float' (str): input data type
            (only relevant if input is text)
        skip_rows=0 (int): number of rows to skip
            (only for text data file)
        transpose=False (bool): whether to transpose the data

    Returns:
        a numpy.ndarray object
    """
    data = R.readDataFile(
        file_name,
        dtype=dtype,
        skiprows=skip_rows)

    if len(numpy.shape(data)) == 0:
        return numpy.array([])
    elif len(numpy.shape(data)) == 1:
        return array_transpose(
            data[:, numpy.newaxis], transpose)
    else:
        return array_transpose(data, transpose)
