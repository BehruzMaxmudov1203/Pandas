"""
Plot executable
AUTHOR: YUHANG(STEVEN) WANG
DATE: 13-11-2016
Usage: plot my.json  or plot my.yaml
"""
import sys
from plot.run import run

def main():
    user_config_file = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--no-preview":
        preview = False
    else:
        preview = True
    return run(user_config_file, preview)
