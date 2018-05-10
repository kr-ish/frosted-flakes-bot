#! /bin/bash

echo  # blank line
date  # print date
DIR=$(dirname "${BASH_SOURCE[0]}")
cd $DIR
~/anaconda2/envs/frosted/bin/python frosty.py
