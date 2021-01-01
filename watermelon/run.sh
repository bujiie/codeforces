#!/usr/bin/env bash

input_type=$1

if [[ "$input_type" == "s" ]]
then
	./main.py input/sample.in
else
	./main.py input/problem.in
fi
