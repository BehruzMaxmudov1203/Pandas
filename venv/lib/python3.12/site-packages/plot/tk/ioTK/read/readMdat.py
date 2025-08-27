"""
Read a mdat file (MessagePack) array
"""
from typing import AnyStr
from numpy import ndarray
import numpy
from ....deps import msgpack


def readMdat(file_name):
    # type: (AnyStr) -> ndarray
    """Read a mdat file and return a python list

    Args:
        file_name (str): input file name

    Returns:
        a numpy ndarray
    """
    with open(file_name, "rb") as IN:
        content = msgpack.unpackb(IN.read())
    return numpy.array(content)
