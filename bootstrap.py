#!/usr/bin/env python3

import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from re import search, findall
from pathlib import Path
from os import chmod, chdir
from shutil import copyfile


def get_html(url, encoding='utf-8'):
    try:
        response = urlopen(url)
        return response.read().decode(encoding)
    except URLError as e:
        print(f'error with the  URL: {url} provided.')
    except HTTPError as e:
        print(f'request failed with error code: {e.code}', e)


def parse_problem_title(html):
    regex = r'<div class=\"header\"><div class=\"title\">(.*?)</div>'
    results = search(regex, html)
    return results.group(1) if results is not None else None


def transform_title_to_dirname(title):
    letter, name = list(map(lambda s: s.strip(), title.split('.')))
    name = format_for_xml(name)
    return f'{name}_{letter}'
   

def format_for_xml(subject):
    return subject.replace(' ', '_') 
   

def parse_sample_tests(html):
    regex = r'<div class=\"input\"><div class=\"title\">Input</div><pre>(.*?)(?:<br />)?</pre></div><div class=\"output\"><div class=\"title\">Output</div><pre>(.*?)(?:<br />)?</pre>'
    return findall(regex, html)


def create_folder(dirpath):
    Path(dirpath).mkdir(parents=True, exist_ok=True)


def write_new_file(filepath, lines=[]):
    with open(filepath, 'w') as fp:
        for line in lines:
            fp.write(line)
        fp.close()

 
if __name__ == '__main__':
    # URL to specific problem.
    url = sys.argv[1]

    html = get_html(url)

    title = parse_problem_title(html)
    dirname = transform_title_to_dirname(title)
    problem_dir = f'./{dirname}'
    create_folder(problem_dir)
    
    tests = parse_sample_tests(html)
    for i, test in enumerate(tests):
        t_in, t_out = test
        write_new_file(f'{problem_dir}/{i+1}.in', [t_in])
        write_new_file(f'{problem_dir}/{i+1}.out', [t_out])

    write_new_file(f'{problem_dir}/README.md', [
        f'# {title}\n\n',
        f'[{url}]({url})\n\n'
    ]) 

    chdir(f'{problem_dir}')
    copyfile(f'../__template.py', f'main.py')
    copyfile(f'../check.sh', f'check.sh')
    chmod(f'./main.py', 0o755)
    chmod(f'./check.sh', 0o755)

