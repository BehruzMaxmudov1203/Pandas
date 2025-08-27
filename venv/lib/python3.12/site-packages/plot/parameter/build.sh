
for x in "$@" ; do
    echo $x
    cd $x
    python ../_yaml2json.py _all_.yaml
    cd ..
done
python _yaml2json.py _all_.yaml
