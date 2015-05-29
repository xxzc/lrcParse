#!/bin/bash
sort $1 -r -n -t $'\t' -k 2 -o $2
