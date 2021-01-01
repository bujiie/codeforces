# Python Notes

## Reading files

### with open()

```python
with open('./path/to/file') as fp:
	# list of all lines in the file; each list item includes the trailing '\n'
	lines_as_list = fp.readlines()
	lines_as_list = list(map(lambda l: l.strip(), lines_as_list))
```

```python
	# reads file line by line; each time readline() is called, it reads the next line including the '\n'
	line = fp.readline()
	line = line.strip()
```

```python
	# if readline(size) size is specified, it will read 'size' number of characters up to the end of line.
	# it will not read from the next line even if the 'size' quota hasn't been met yet.
	# The '\n' is considered a character. Unlike lists, specifying -1 does not truncate the last character. Instead
	# it will read the entire line (including the '\n').
	# If the specified size does not encompass the entire line, the next call to readline() will continue
	# reading the same line. To get to the next line, you must complete reading a line.
	line = fp.readline(5)
```

```python
	# loops through all lines; each iteration includes the trailing '\n'
	for line in fp:
		line = line.strip()
```

```python
	# enumerates all the lines in a file; each iteration includes the trailing '\n'
	for i, line in enumerate(fp):
		line = line.strip()
```

### fileinput.input()
```python
	# assumes that the arguments to your run command are all files and will read all of them line by line.
	# each line includes the '\n'
	import fileinput
	for line in fileinput.input():
		line = line.strip()
```

```python
	# similar implementation to with open() if you have multiple files
	with fileinput.input(files=('file1','file2')) as fp:
		for line in fp:
			line = line.strip()
```


