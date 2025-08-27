"""
Combine all yaml files listed in _all_.yaml
into one file: all.yaml and all.json

usage: python _yaml2json.py _all_.yaml

Author: Yuhang(Steven) Wang
Date: 11-11-2016
"""
import json
import yaml
import sys
import copy
from plot.tk.fnTK import reduce
from plot.tk.dictTK import merge


def read_yaml(file):
    with open(file, "r") as IN:
        content = IN.read()
    return yaml.load(content)


def save_json(output, d, indent=2):
    """save a dict to json file"""
    with open(output, "w") as OUT:
        OUT.write(json.dumps(d, sort_keys=True, indent=indent))
    return True


def save_yaml(output, d):
    """save a dict to yaml file"""
    with open(output, "w") as OUT:
        OUT.write(yaml.dump(d))
    return True


def add_internal_key(d, key=None):
    """Add internal keyword field "__" """
    if isinstance(d, list):
        return [add_internal_key(x) for x in d]
    else:
        ooo = copy.deepcopy(d)
        if key is not None and "__" not in d:
            ooo["__"] = "_".join(key.split())
        for k in d.keys():
            if isinstance(d[k], dict):
                ooo[k] = add_internal_key(d[k], k)
            elif isinstance(d[k], list) and isinstance(d[k][0], dict):
                ooo[k] = add_internal_key(d[k])
            else:
                continue
        return ooo


def convert(file):
    d = add_internal_key(read_yaml(file))
    save_json(file.replace(".yaml", ".json"), d)
    return d


def suffix(name, ext="yaml"):
    return "{}.{}".format(name, ext)


def main(all_yaml):
    with open(all_yaml, "r") as IN:
        yaml_files = list(map(suffix, yaml.load(IN.read())))
    all_dict = reduce(merge, list(map(convert, yaml_files)), dict())
    save_json("all.json", all_dict)
    save_yaml("all.yaml", all_dict)


if __name__ == '__main__':
    main(sys.argv[1])
