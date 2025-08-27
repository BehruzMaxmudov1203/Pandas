"""
Parse the user input configuration file,
update the default configuration dictionary
with the user-defined values and
return the updated dictionary.
"""
from typing import Dict, AnyStr
from .parser import parser
from .readAll import readAll
from ... import tk
from .preprocessing import preprocess
from .postprocessing import postprocess


def parse(user_config_file, default_config_file):
    # type: (AnyStr, AnyStr) -> (Dict)
    """Return an updated configuration file

    Read a user configuration file and
    a default configuration file.
    Use the values in the user configuration
    file to update the default configuration file.
    Finally return an updated configuration dictionary.

    Args:
        user_config_file (str): user configuration file

    Returns:
        an updated configuration dictionary
    """
    fn_parser1 = parser(user_config_file)
    fn_parser2 = parser(default_config_file)
    user_dict = fn_parser1(readAll(user_config_file))
    default_dict = tk.dictTK.default(fn_parser2(readAll(default_config_file)))
    ooo = {}

    for k in ['global', 'local', 'data', 'internal']:
        if k in user_dict:
            if isinstance(user_dict[k], list):
                ooo[k] = [preprocess(user_dict[k][i], default_dict[k])
                          for i in range(len(user_dict[k]))]
            else:
                ooo[k] = preprocess(user_dict[k], default_dict[k])
        elif k not in user_dict and k in ['data', 'local']:
            ooo[k] = []
        else:
            ooo[k] = preprocess(dict(), default_dict[k])
    # add internal-default-local
    ooo['internal']['default']['local'] = (
            preprocess(dict(), default_dict['local']))
    return postprocess(ooo)
