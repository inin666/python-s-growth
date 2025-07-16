company_name = "传播智客"
stock_price = 19.99
stock_code = "003032"
print(f"公司：{company_name}，股票代码：{stock_code}，当前股价：19.99")
num1 = 1.2
num2 = 7
num3 = stock_price*num1**num2
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (num1, num2, num3))