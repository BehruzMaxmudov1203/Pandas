"""
Return two arrays representing the error bars
"""
from numpy import ndarray
from typing import Dict


def extract_data_error_bar(data, params):
    # type: (ndarray, Dict) -> (ndarray, ndarray)
    """Return error bar arrays

    Return error bar arrays along X and Y

    Args:
        data (ndarray): input data
        params (dict): one entry of the 'data' parameter field

    Returns:
        (x_bars, y_bars) where x_bars and y_bars are 1-dimensional numpy arrays
    """
    plot_type = params['plot_type']
    row_begin = params[plot_type]['row_start']
    ooo = []
    for k in ['x', 'y']:
        j = params['error_bar']['data_column'][k]
        if j is None:
            ooo.append(None)
        else:
            ooo.append(data[row_begin:, j])
    return tuple(ooo)
