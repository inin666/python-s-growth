

money = 5000000
name = "周结论"

#查询余额函数
def inquire_money():
    global money
    print(money)
    control_panel()
#存款函数
def store_money():
    add = int(input("输入存入金额:"))
    global money
    money += add
    print(money)
    control_panel()
#取款函数
def withdraw_money():
    draw = int(input(f"输入取款金额"))
    global money
    money -= draw
    print(money)
    control_panel()
#主菜单函数
def control_panel():
    if name == input("请输入姓名："):
        print("验证成功，请继续操作")
        print("inquire_money()\nstore_money()\nwithdraw_money()\n")

        if input("请选择服务：")== inquire_money():
            inquire_money()

        elif input("请选择服务：")== store_money():
            store_money()

        elif input("请选择服务：")== withdraw_money():
            withdraw_money()

    else:
        control_panel()
#启动程序
control_panel()