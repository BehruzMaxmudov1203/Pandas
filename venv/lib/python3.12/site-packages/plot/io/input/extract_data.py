"""
Return two arrays based on input data and input parameters
"""
from numpy import ndarray
from typing import Dict
from ...tk.arrayTK import smooth


def extract_data(data, params):
    # type: (ndarray, Dict) -> (ndarray, ndarray)
    """Separate the input data into separate arrays
    Smoothen the data if params['smooth']['window_size'] is set

    Args:
        data (ndarray): input data
        params (dict): one entry of the 'data' parameter field

    Returns:
        [X, Y] if params['data_column'] is ['x', 'y']
        [X, Y1, Y2] if params['data_column'] is ['x', 'y1', 'y2']
    """
    plot_type = params['plot_type']
    row_start = params[plot_type]['row_start']
    ooo = []

    p = params[plot_type]['data_column']
    for k in sorted(p.keys()):
        j = p[k]
        if j is None:
            continue
        else:
            ooo.append(data[row_start:, j])

    if params['smooth']['window_size'] is not None:
        for i in range(1, len(ooo)):
            ooo[i] = smooth(ooo[i], params['smooth'])

    return ooo
