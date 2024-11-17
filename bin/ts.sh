#!/bin/bash
# check if arguments exist
if [ $# -lt 1 ]; then
  echo 1>&2 "$0: missing problem number"
  exit 1
fi

# validate arguments
re='^[0-9]+$'
if ! [[ $1 =~ $re ]] ; then
   echo "error: argument must be an positive integer" >&2
   exit 1
fi

problem_file=$(find ./lc-typescript/src -type f -name "lc_*"$1"_*")
echo "Testing:" $problem_file
deno test $problem_file
