"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
os.chdir(r'src')

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE


def open_file(data):
    with open(data, 'r') as doc:
        content = doc.read()
        print(content)
        doc.closed


open_file('foo.txt')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE


def write_file():
    l = ['pear\n', 'apple\n', 'orange\n',
         'mandarin\n', 'watermelon\n', 'pomegranate\n']
    with open('pascal.txt', 'w') as doc:
        for item in l:
            doc.write(item)
        doc.closed


write_file()
open_file('pascal.txt')
