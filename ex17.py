from sys import argv
from os.path import exists

# tips:文件编码应该为utf-8
# echo "This is a test file." > test.txt 在win下不可用
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# indata = open(from_file).read()
in_file = open(from_file)
print(">>>>in_file = ", repr(in_file))
indata = in_file.read()


# 打印indata字符数
print(f"The input file is {len(indata)} bytes long")
# exists判断文件和文件夹是否存在
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#  以写模式 打开copied.txt
#  w代表写模式打开文件
#  r代表读模式打开文件
#  wr代表读写模式打开文件
#  w+代表读写模式打开文件
#  r+代表读写模式打开文件
#  a+代表读写模式打开文件
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()