"""
Save data to a file
"""
import os
import numpy
from .saveTextData import saveTextData
from .saveNpy import saveNpy
from .saveMdat import saveMdat


def saveData(output_file, data, fmt):
    """Save data into an output file
    The format will be determined by file extension

    Args:
        output_file (str): output file name
        data (ndarray): numpy ndarray data
        fmt (str): format string
            (used only if the output is a text file)
    """
    _, ext = os.path.splitext(output_file)
    if ext == ".npy":
        saveNpy(output_file, data)
    elif ext == ".mdat":
        saveMdat(output_file, data)
    else:
        saveTextData(output_file, data, fmt)
