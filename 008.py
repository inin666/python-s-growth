import  random
num = random.randint(1,100)
num_guess = int(input("请输入文本:"))
i = 0
while num_guess !=num:
    i += 1
    if num_guess < num:
        print("小了")
    else:
        print("大了")
    num_guess = int(input("请输入文本:"))
print("运气而已","猜了",i,"次")