"""
Append an item to an entry in a multidimensional list
"""


def append(L, index, new_item):
    # type: (List, list, object)
    """Append an item to a list
    Args:
        L (list): input list
        index (list): index
        new_item (object): new object
    """
    def tail(xs): return xs[1:]

    if not isinstance(L, list):
        return L
    else:
        if len(index) == 0:
            return L + [new_item]
        if len(index) == 1:
            i = index[0]
            if i == 0:
                return [L[0], new_item] + L[1:]
            else:
                return L[0:(i-1)] + [L[i], new_item] + L[(i+1):]
        else:
            i = index[0]
            L[i] = append(L[i], tail(index), new_item)
            return L
