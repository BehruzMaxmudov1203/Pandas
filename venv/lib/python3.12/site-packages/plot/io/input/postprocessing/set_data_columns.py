"""
Set which data columns to use for line/bar objects
"""
from typing import Dict
from ..readDataFile import readDataFile
from ..readFileOrList import readFileOrList
import numpy


def set_data_columns(params):
    # type: (Dict) -> Dict
    """Set which data columns to user for line/bar objects

    If user specified the data columns, then
    no change will be made.

    If the data only has one column,
    then set the default y column is 0-th column.

    If the data has more than one columns,
    then set the x column to 0 and y column to 1.

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        updated params
    """
    for p in params['data']:
        if "data_column" not in p.keys():
            continue
        else:
            pass

        data = readFileOrList(p['file'], p['values'], p['skip_rows'])
        column_count = numpy.shape(data)[1]

        if p['data_column']['x'] is None:
            if column_count > 1:
                p['data_column']['x'] = 0
            else:
                p['data_column']['x'] = None
        else:
            pass

        if p['data_column']['y'] is None:
            if column_count == 1:
                p['data_column']['y'] = 0
            else:
                p['data_column']['x'] = 1
        else:
            pass

    return params
