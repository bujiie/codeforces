# Codeforces

My solutions to Codeforces problems.

## Get Started

### TL;DR

```bash
./bootstrap.py https://codeforces.com/problemset/problem/4/A
```
```bash
cd {Problem_Name}_{LETTER}
```
code your solution in `main.py`
```bash
./check.sh

Test 1...OK
Test 2...OK
...
Test n...OK
```
If everything passed, upload your `main.py` file to Codeforces.

### Bootstrapping a new problem

```bash
./bootstrap.py https://codeforces.com/problemset/problem/4/A
```

The following is created.

```
./{Problem_Name}_{LETTER}
	1.in
	1.out
	2.in
	2.out
	...
	main.py  // chmod +x
	check.sh // chmod +x
	README.md
```

### Sample Files `*.in`/`*.out`

The sample inputs/outputs found on the problem page are written to files `1.in/1.out`, `2.in/2.out`, etc.

Additional inputs/outputs can be added and will get picked up by the `check.sh` script as long as the following conditions are met.

    * Resides in the same directory as the other `*.in` and `*.out` files
    * Has both a `{filename}.in` and a `{filename}.out` file

### Solution file `main.py`

The solution file `main.py` is a copy of the `__template.py` file in the project's root folder. If you want to have a different starting template for problems moving forward, modify the `__template.py` file. Otherwise, write your solution in the `main.py` file found in the `{Problem_Name}_{LETTER}` folder.

### Checking your solution with `check.sh`

```bash
./check.sh
```

If you haven't move any of the files since bootstrapping the problem, you should be able to run the `./check.sh` script as is.

The script will find all the `*.in` files in the problem folder, execute your `main.py` script for each `.in` file and compare its output to the corresponding `*.out` file.



