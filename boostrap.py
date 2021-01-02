#!/usr/bin/env python3

import sys
from urllib.request import urlopen
from re import search, findall
from pathlib import Path
from shutil import copyfile
from os import chmod, chdir

problem_url = sys.argv[1]

def error_and_exit(message):
	print(f'ERROR: {message}')
	sys.exit()

def format_for_xml(string):
	return string.replace(' ', '_')
	
if problem_url is None:
	error_and_exit('No problem URL found.')

response = urlopen(problem_url)
data = response.read().decode('utf-8')

title_regex = r'class=\"header\"><div class=\"title\">([\w\.\s\-\+\=\"\']+)</div>.*'
title_search_results = search(title_regex, data)

if title_search_results is None or len(title_search_results.group(1)) == 0:
	error_and_exit(f'No problem title found for URL: {problem_url}')

problem_title_full = title_search_results.group(1)
[letter, problem_title] = list(map(lambda s: s.strip(), problem_title_full.split('.')))
problem_title_xml = format_for_xml(problem_title)

formatted_problem_title = f'{problem_title_xml}_{letter}'


inout_regex = r'(?:<div class=\"input\"><div class=\"title\">Input</div><pre(?: id=\"[\w\d\-]+\")?>([\w\d\-\s]+)(?:<br />)?</pre></div>)|(?:<div class=\"output\"><div class=\"title\">Output</div><pre(?: id=\"[\w\d\-]+\")?>([\w\d\-\s]+)(?:<br />)?</pre></div>)'
inout_search_results = findall(inout_regex, data)

if inout_search_results is None:
	error_and_exit('No input/output found.')

# Results of regex findall returns tuples that alternate sides containing an
# empty string ('a', ''), ('', 'b')...
# I'm not sure why, but it's good enough and can be cleaned up with the following
# loop.
samples = []
while len(inout_search_results) > 0:
	[i,o,*inout_search_results] = inout_search_results
	samples.append((i[0], o[1]))


problem_dir = formatted_problem_title
problem_input_dir = f'./{problem_dir}/input'

# Create problem and input directories
Path(problem_input_dir).mkdir(parents=True, exist_ok=True)

# Create README.md with link to the problem
fp = open(f'{problem_dir}/README.md', 'w')
fp.write(f'# {problem_title_full}\n\n')
fp.write(f'[{problem_url}({problem_url})\n')
fp.close()

# Fetch the samples from the problem page and write the input and output to
# separate files.:1

for i, sample in enumerate(samples):
	fip = open(f'{problem_input_dir}/sample{i}.in', 'w')
	fip.write(sample[0])
	fip.close()

	fop = open(f'{problem_input_dir}/sample{i}.out', 'w')
	fop.write(sample[1])
	fop.close()

# Copy starter python script template to problem directory
copyfile(f'./__template.py', f'./{problem_dir}/main.py')
# Make main.py executable
chdir(f'./{problem_dir}')
chmod(f'./main.py', 0o755)
		
