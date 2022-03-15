#!/bin/bash
cd ../src

python3 run.py $1 0 none full False AMB 200000 5000
python3 run.py $1 0 none random False rmb 200000 5000
python3 run.py $1 0 none random False FRGB 200000 5000
python3 run.py $1 0 none random False RMB 200000 5000
python3 run.py $1 0 none random False AMB 200000 5000

python3 run.py $1 0 none gaussian False rmb 200000 5000
python3 run.py $1 0 none gaussian False FRGB 200000 5000
python3 run.py $1 0 none gaussian False RMB 200000 5000
python3 run.py $1 0 none gaussian False AMB 200000 5000

python3 run.py $1 0 none full False rmb 200000 5000
python3 run.py $1 0 none full False FRGB 200000 5000
python3 run.py $1 0 none full False RMB 200000 5000

python3 run.py $1 0 none random True rmb 200000 5000
python3 run.py $1 0 none random True FRGB 200000 5000
python3 run.py $1 0 none random True RMB 200000 5000
python3 run.py $1 0 none random True AMB 200000 5000

python3 run.py $1 0 none gaussian True rmb 200000 5000
python3 run.py $1 0 none gaussian True FRGB 200000 5000
python3 run.py $1 0 none gaussian True RMB 200000 5000
python3 run.py $1 0 none gaussian True AMB 200000 5000

python3 run.py $1 0 none full True rmb 200000 5000
python3 run.py $1 0 none full True FRGB 200000 5000
python3 run.py $1 0 none full True RMB 200000 5000
python3 run.py $1 0 none full True AMB 200000 5000
