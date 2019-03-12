from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
#	以写模式 打开test.txt
#	w代表写模式打开文件
#	r代表读模式打开文件
#	wr代表读写模式打开文件
#	w+代表读写模式打开文件
#	r+代表读写模式打开文件
#	a+代表读写模式打开文件

print("Truncating the file. Goodbye!")
target.truncate()
# 清空text.txt文件

print("Now I'm going to ask you for three lines.")

line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finall, we close it.")
target.close()