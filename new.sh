#!/usr/bin/env bash

problem_name=$1
problem_link=$2
sample_input="sample.in"
problem_input="problem.in"
code_file="main.py"
run_file="run.sh"
readme_file="README.md"

mkdir -p "${problem_name}/input"
cp ./__template.py "${problem_name}/${code_file}"
cp ./__template.sh "${problem_name}/${run_file}"
touch "${problem_name}/input/${sample_input}"
touch "${problem_name}/input/${problem_input}"
echo -e "# $problem_name\n\n[$problem_link]($problem_link)\n" > "${problem_name}/${readme_file}"

cd $problem_name
chmod 755 $code_file
chmod 755 $run_file



