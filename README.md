# README

Yet Another LeetCode solutions repository

## Prerequisites

requires python3 and deno <https://deno.com/>

```shell
curl -fsSL https://deno.land/install.sh | sh
```

## Getting started

Run tests for a specific solution in python

```shell
➜  leetcode git:(main) ✗ ./bin/py.sh 100
Testing: ./lc-python/src/lc_0100_same_tree.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Run tests for a specific solution in typescript

```shell
➜  leetcode git:(main) ✗ ./bin/ts.sh 100
Testing: ./lc-typescript/src/lc_0100_same_tree.ts
running 1 test from ./lc-typescript/src/lc_0100_same_tree.ts
0100 Same Tree ... ok (0ms)
```

Run all the tests

```shell
➜  leetcode git:(main) ✗ ./bin/all.sh
...
```

Run postgresql solutions (no testing, only outputs result)

```shell
➜  leetcode git:(main) ✗ ./bin/sql.sh 0197
Testing: ./lc-sql/lc_0197_rising_temperature.sql
 id 
----
  2
  4
(2 rows)
```
