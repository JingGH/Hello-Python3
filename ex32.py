the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'penniers', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# alse we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")




#----------------------tips:
# 1.range() 函数：
# range() 函数可以创建一个整数列表，一般用在 for 循环中。
# 语法：range(start,stop,step) 
# start：start 是计数开始，一般默认为0，例如 range(5)的意思就是 range(0, 5)；
# stop：stop 是计数结束，但不包含 stop，例如 range(0,5)是[0, 1, 2, 3, 4]，不包含[5]；
# step：step 是步长（就是两数之间间隔），一般默认为1，例如 range(0,5)的意思就是 range(0, 5, 1)；
# 实例： range(25) = range(0, 25) ：[0, 1, 2, 3, ...24]  此处修改，range()取上不取下，最后一个数值不会被取到 range(0,25,5)  ：[0, 5, 10, 15, 20]
# 然后我们还可以再 range()中取特定的值，比如取第3个值：x = range(0, 25, 5)   x[2]就是取第3个值了（10）；

# 2.append()函数：
# append() 函数可以在列表的尾部追加参数，例如：

"""
list = [1, 2, 'one', 'two']

list.append(3)
print(list)
>>>[1, 2, 'one', 'two', 3]

list.append('three')
print(list)
>>>[1, 2, 'one', 'two', 3, 'three']
"""
#append()  1次只能追加1个参数 ，它可以追加任何类型的参数；
#还有一个expend() 函数也可以在列表后追加参数，但是它追加的参数类型必须是list，也就是在原来的list的尾部追加list。