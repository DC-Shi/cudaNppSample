#!/usr/bin/env bash
make clean build

make run ARGS="-input=data/Lena.pgm"


if [ $? -eq 0 ]; then
    echo OK, converting pgm files into png for easier view.
    python3 ConvertImageToPng.py --folder ./data
else
    echo Run failed.
fi