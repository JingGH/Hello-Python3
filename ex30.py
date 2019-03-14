people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# ----------------
scores = int(input("请输入成绩！"))
 
if scores >= 95:
	print("优秀！")
elif scores >= 80:
	print("良好！")
elif scores >= 60:
	print("合格！")
else:
	print("不及格！")

# -----------------