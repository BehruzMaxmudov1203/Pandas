"""
Read one data file
"""
import os
import numpy
from .readTextData import readTextData
from .readNpy import readNpy
from .readMdat import readMdat


def readDataFile(file_name, dtype="float", skiprows=0):
    """Read one data file

    Return a numpy array

    Args:
        inputs (str): file name
        dtype (str): input data type
            default: "float"

    Returns:
        an ndarray
    """
    _, ext = os.path.splitext(file_name)
    if ext == ".npy":
        return readNpy(file_name)
    elif ext == ".mdat":
        return readMdat(file_name)
    else:
        return readTextData(file_name, dtype, skiprows)
