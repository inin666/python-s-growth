salary = 10000
for worker in range(1,21):
    import  random
    num = random.randint(1,10)
    if salary > 0:
        print(f"{worker}的工资为:", end='')
        if num < 5:
            print("0")
        else:
            print("1000")
            salary -= 1000
    else:
        break
print("结束了")

