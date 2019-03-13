<<<<<<< HEAD
from sys import argv

scripy, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

=======
from sys import argv

scripy, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

>>>>>>> 4041cac322ac87664772dfca932f459134bcc71e
print(txt_again.read())