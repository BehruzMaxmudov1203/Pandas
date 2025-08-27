@echo off

for %%x in (%1) do (
    echo %%x
    chdir %%x
    python ..\_yaml2json.py _all_.yaml
    chdir ..
)
python _yaml2json.py _all_.yaml