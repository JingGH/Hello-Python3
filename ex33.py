i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

# def
def my_while(loops):  #step
    i = 0
    numbers = []
    while i < loops:
        print("At the top i is %d" %i)
        numbers.append(i)
        i += 1      #step
        print("Numbers now:",numbers)
        print("At the bottom is %d" %i)
        print("\n--------------------------")

my_while(6)
print("The numbers:")
for num in numbers:
    print(num)

#for &  range
numbers = []

for i in range(6):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")
    print("\n========================")

print("The numbers:")

for num in numbers:
    print(num)