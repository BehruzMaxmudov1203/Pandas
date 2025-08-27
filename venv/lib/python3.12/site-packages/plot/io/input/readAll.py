"""
Read all the content of a file
and return one big string.
"""
from typing import AnyStr


def readAll(file_name):
    # type: (AnyStr) -> AnyStr
    """Return the file content

    Return the content of a file as string.

    Args:
        file_name (str): name of the input file

    Returns:
        a string which is the content of the file
    """
    with open(file_name, "r") as IN:
        return IN.read()
