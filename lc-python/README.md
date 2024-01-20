# LeetCode python

## Prerequisites

```bash
pip install -U virtualenv
```

## Getting started

Create a virtual environment

```bash
python3 -m venv .env
source .env/bin/activate
```

Deactivate virtual environment when done

```shell
deactivate
```

Run unit tests via the helper script.

```shell
./run_tests.sh
```

## Project layout

Every problem has it's own file, which contains one or more solutions, a test file and a data file.

The general format is:

- script: `lc_0001_two_sum.py`
- test: `lc_0001_two_sum_test.py`
- data: `lc_0001_two_sum.data`

```shell
├── README.md
├── run_tests.sh
└── src
    ├── lc_0001_two_sum.dat
    ├── lc_0001_two_sum.py
    ├── lc_0001_two_sum_test.py
    ├── ...
    ├── lib.py
```

Each script is self-contained, meaning the solution can be copy-pasted directly into the Leetcode editor. The test uses the data file as input. The `lib.py` contains a bunch of reusable helper functions for parsing/reading files.
