#!/bin/sh

# Save the current directory and the script's directory, since build must be run from the project root
pwd=$(pwd)
dirname=$(dirname $0)

# Back up the old PYTHONPATH so it can be restored later
old_pythonpath=$PYTHONPATH

# Build the program
cd $dirname/..
PYTHONPATH=
pip3 install -r requirements.txt
python3 setup.py build

# Restore the old PYTHONPATH and move back to the original directory
cd $pwd
PYTHONPATH=$old_pythonpath

# Pass ubuntu22 param to build for Ubuntu22 else build will be for other linux distribution