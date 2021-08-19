#!/bin/bash

awk '{s[$2] += $1} END {for(i in s){print i, s[i]}}' "$@"

