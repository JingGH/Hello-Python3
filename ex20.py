<<<<<<< HEAD
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end ="")

current_file = open(input_file)

print("First let's print the whole file:")

print_all(current_file)

print("\nNow let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line += 1
=======
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end ="")

current_file = open(input_file)

print("First let's print the whole file:")

print_all(current_file)

print("\nNow let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line += 1
>>>>>>> 4041cac322ac87664772dfca932f459134bcc71e
print_a_line(current_line,current_file)