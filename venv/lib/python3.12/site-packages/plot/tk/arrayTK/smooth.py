"""
Return a smoothed version of the input array
"""
from typing import Dict
from numpy import ndarray
import scipy.ndimage


def smooth(xs, params):
    # type: (ndarray, Dict) ->
    """Smooth 1D data array

    Return a smoothed version of the input array

    Args:
        xs (ndarray): a 1D numpy ndarray
        params (dict): parameter dictionary

    Returns:
        a new numpy ndarray object
    """
    return scipy.ndimage.uniform_filter1d(
        xs,
        size=params['window_size'],
        mode=params['mode'],
        cval=params['constant_value'],
        origin=params['origin']
        )
