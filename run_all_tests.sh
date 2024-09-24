#!/bin/bash
deno test lc-typescript/src/*
python3 -m unittest discover -s lc-python/src -p "*.py" -v
