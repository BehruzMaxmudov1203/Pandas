"""
Append a new legend
"""


def append_addon(addon, handle, label, pid, params):
    # type: (object, AnyStr, Dict) -> Dict
    """Append a new legend

    Args:
        addon (str): name of the add-on, eg 'legend'
        handle (obj): a matplotlib object
            e.g. matplotlib.line.Line2D
        label (str): add-on label
        pid (tuple): add-on panel index
        params (dict): plotting parameters
    Returns:
        updated parameters
    """
    p = params['internal']['panel'][addon]
    if pid is not None:
        p[pid].append([handle, label])
    else:
        pass
