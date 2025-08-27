"""
Save a numpy ndarray into an npy file
"""
import numpy


def saveNpy(file_name, data):
    """Save a numpy ndarray into an npy file

    Args:
        file_name (str): output file name
        data (ndarray): a numpy ndarray
    """
    numpy.save(file_name, data)
