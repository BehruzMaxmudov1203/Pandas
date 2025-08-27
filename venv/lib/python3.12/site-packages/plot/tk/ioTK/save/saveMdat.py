"""
Save a ndarray into an mdat file
"""
from ....deps import msgpack
import numpy


def saveMdat(file_name, data):
    """Save data into mdat file

    Args:
        file_name (str): output file name
        data (ndarray): ndarray
    """
    content = msgpack.packb(data.tolist())
    with open(file_name, "wb") as OUT:
        OUT.write(content)
