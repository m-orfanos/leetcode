#!/bin/bash
deno test lc-typescript/src/*
python -m unittest discover -s lc-python/src -p "*.py" -v