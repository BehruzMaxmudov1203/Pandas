"""
Return an appropriate parser based on
file extension name.
"""
from typing import Callable, AnyStr, Dict
import re


def parser(file_name):
    # type: (AnyStr) -> Callable[[AnyStr],Dict]
    """Return a parser function

    Return a function can read user input file
    and return a dictionary.

    Args:
        file_name (str): input file name

    Returns:
        a dictionary containing the content
        of the file.
    """
    if re.match(".*\.json", file_name):
        import json
        return json.loads
    elif re.match(".*\.yaml", file_name):
        import yaml
        return lambda x: yaml.load(x, Loader=yaml.FullLoader)
    else:
        return lambda x: dict()
