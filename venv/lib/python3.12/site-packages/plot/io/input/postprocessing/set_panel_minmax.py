"""
Set the min/max for each panel based on input data
"""
from typing import Dict
from ....tk.arrayTK import minmax
from ..readFileOrList import readFileOrList
import numpy


def set_panel_minmax(params):
    # type: (Dict) -> Dict
    """See the min/max for each panel

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    params['internal']['panel']['minmax'] = dict()
    p_minmax = params['internal']['panel']['minmax']

    def update(old, new):
        return {'x': min(old['x'], new['x']), 'y': max(old['y'], new['y'])}

    def aux(new_minmax_dict, panel_id):
        if panel_id in p_minmax:
            return update(new_minmax_dict, p_minmax[panel_id])
        else:
            return new_minmax_dict

    for p in params['data']:
        panel_id = p['which_panel']
        if p['file'] is None and p['values'] is None:
            continue
        else:
            data = readFileOrList(p['file'], p['values'], p['skip_rows'])
            row_count, column_count = numpy.shape(data)

            if row_count == 0 or column_count == 0:
                continue
            elif column_count == 1:
                print(p['file'])
                print("data.shape", data.shape)
                mm = [
                    [0, row_count - 1],
                    minmax(data[:, 0])
                ]
            else:
                mm = minmax(data[:, 0], data[:, 1])

            p_minmax[panel_id] = aux({'x': mm[0], 'y': mm[1]}, panel_id)
    return params
