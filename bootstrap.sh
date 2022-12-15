#!/bin/bash

year=$1
day=$2

mkdir -p "$1/data"

touch "$1/data/day$2-final.txt"
touch "$1/data/day$2-sample.txt"

cp template.py "$1/day$2.py"

sed -i '' -e "s/__DAY__/$2/g" "$1/day$2.py"