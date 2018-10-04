#!/bin/sh
pip --version
pip install --target local_lib git+https://github.com/jaraco/path.py.git --upgrade --log install_path.log
python3 my_program.py


