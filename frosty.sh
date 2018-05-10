#! /bin/bash

echo  # blank line
date  # print date
DIR=$(dirname "${BASH_SOURCE[0]}")
cd $DIR

# If you're using a virtual / conda environment
~/anaconda2/envs/frosted/bin/python frosty.py

# If you're not
# python frosty.py
